from subprocess import DEVNULL, Popen, PIPE
from dataclasses import dataclass
from typing import Annotated, Any, Generator
from pathlib import Path
import json

from PIL import ImageFont
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)
import typer

from terminal import Terminal
from terminal_renderer import TerminalRenderer


@dataclass(frozen=True)
class CastHeader:
    width: int
    height: int


@dataclass(frozen=True)
class CastBody:
    time: float
    text: str


app = typer.Typer()
console = Console()
err_console = Console(stderr=True)


def read_header(path: str | Path) -> tuple[CastHeader, int]:
    with open(path, "r") as f:
        line = f.readline()
        bytes_read = len(line.encode("utf-8"))
        data: dict[str, Any] = json.loads(line)

        for key in {"version", "width", "height"}:
            if key not in data:
                raise ValueError("Invalid file: could not find required param")

        assert data["version"] == 2
        return (
            CastHeader(width=data["width"], height=data["height"]),
            bytes_read,
        )


def read_body(path: str | Path) -> Generator[tuple[CastBody, int], None, None]:
    with open(path, "r") as f:
        f.readline()
        for line in f:
            bytes_read = len(line.encode("utf-8"))
            data: list = json.loads(line)
            assert len(data) == 3

            time, type_, text = data
            assert isinstance(time, float)
            assert isinstance(type_, str)
            assert isinstance(text, str)

            assert type_ == "o"

            yield CastBody(time, text), bytes_read


def render(input_path: Path, output_path: Path) -> None:
    # input_path = Path("./.recordings/16-05-2026_18-31-55.cast")
    header, bytes_read = read_header(input_path)

    file_size = input_path.stat().st_size
    total_render_bytes = file_size - bytes_read

    font_path = Path(
        "~/.fonts/JetBrainsMonoNerdFontMono-Regular.ttf"
    ).expanduser()
    font = ImageFont.truetype(font_path, 20)
    fps = 30

    with Terminal(header.height, header.width) as term:
        renderer = TerminalRenderer(term, font)
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-loglevel",
            "quiet",
            # input
            "-f",
            "rawvideo",
            "-vcodec",
            "rawvideo",
            "-pix_fmt",
            "rgb24",
            "-s",
            f"{renderer.width}x{renderer.height}",
            "-r",
            str(fps),
            "-i",
            "-",
            # output
            "-c:v",
            "libx264",
            "-crf",
            "16",
            "-preset",
            "veryfast",
            "-tune",
            "animation",
            "-pix_fmt",
            "yuv420p",
            str(output_path),
        ]
        with Progress(
            TextColumn("[bold blue]🎬 Recast Rendering[/bold blue]"),
            BarColumn(
                bar_width=40,
                complete_style="green",
                finished_style="bold green",
            ),
            TaskProgressColumn(),
            TimeRemainingColumn(),
        ) as progress:
            task_id = progress.add_task("rendering", total=total_render_bytes)

            with Popen(
                ffmpeg_cmd,
                stdin=PIPE,
                stdout=DEVNULL,
            ) as ffmpeg:
                for body, bytes_read in read_body(input_path):
                    term.feed(body.text)
                    frame = renderer.render()

                    assert ffmpeg.stdin
                    ffmpeg.stdin.write(frame.tobytes())
                    progress.update(task_id, advance=bytes_read)


def print_err(msg: str) -> None:
    err_console.print(f"[bold red]Error:[/bold] {msg}")


def render_file(input: Path, force: bool) -> None:
    output = input.with_suffix(".mp4")
    if output.exists():
        if not output.is_file():
            print_err(
                f"output file already exists and is not a file. Path: {output.as_posix()!r}"
            )
            raise typer.Exit(1)

        if not force:
            typer.confirm(
                f"Output path {output.as_posix()!r} already exists. Overwrite?",
                abort=True,
            )

    console.print(
        f"[blue]Rendering {input.as_posix()!r} to {output.as_posix()!r}[/blue]"
    )
    render(input, output)
    console.print(
        f"[bold green]Rendered[/bold] {input.as_posix()!r} to {output.as_posix()!r}[green]"
    )


def render_dir(input: Path, force: bool) -> None:
    console.print(f"[bold blue]Rendering from {input.as_posix()!r}[/bold bluw]")
    for file in input.iterdir():
        if not file.is_file():
            continue

        output = file.with_suffix(".mp4")
        if output.exists() and output.is_file():
            console.print(
                f"Output file for {file.as_posix()!r} already exists. Path: {output.as_posix()!r}"
            )
            console.print(
                f"[bold blue]Skipping[/bold] {output.as_posix()!r}[/blue]"
            )
            continue

        render_file(file, force)


@app.command()
def main(
    input: Annotated[
        Path,
        typer.Argument(
            resolve_path=True, exists=True, file_okay=True, dir_okay=True
        ),
    ],
    force: Annotated[bool, typer.Option("--force", "-f")] = False,
) -> None:
    if input.is_file():
        render_file(input, force)
        return

    render_dir(input, force)


if __name__ == "__main__":
    app()
