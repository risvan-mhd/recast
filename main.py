from subprocess import DEVNULL, Popen, PIPE
from dataclasses import dataclass
from typing import Any, Generator
from pathlib import Path
import json

from PIL import ImageFont
from rich.progress import (
    BarColumn,
    Progress,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)

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


def main():
    cast_file = Path("./.recordings/16-05-2026_18-31-55.cast")
    header, bytes_read = read_header(cast_file)

    file_size = cast_file.stat().st_size
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
            "output.mp4",
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
                for body, bytes_read in read_body(cast_file):
                    term.feed(body.text)
                    frame = renderer.render()

                    assert ffmpeg.stdin
                    ffmpeg.stdin.write(frame.tobytes())
                    progress.update(task_id, advance=bytes_read)


if __name__ == "__main__":
    main()
