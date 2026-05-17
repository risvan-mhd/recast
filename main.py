from subprocess import Popen, PIPE
from dataclasses import dataclass
from typing import Any, Generator
from pathlib import Path
import json

from PIL import ImageFont

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


def read_header(path: str | Path) -> CastHeader:
    with open(path, "r") as f:
        data: dict[str, Any] = json.loads(f.readline())

        for key in {"version", "width", "height"}:
            if key not in data:
                raise ValueError("Invalid file: could not find required param")

        assert data["version"] == 2
        return CastHeader(width=data["width"], height=data["height"])


def read_body(path: str | Path) -> Generator[CastBody, None, None]:
    with open(path, "r") as f:
        f.readline()
        for line in f:
            data: list = json.loads(line)
            assert len(data) == 3

            time, type_, text = data
            assert isinstance(time, float)
            assert isinstance(type_, str)
            assert isinstance(text, str)

            assert type_ == "o"

            yield CastBody(time, text)


def read_cast(
    path: str | Path,
) -> tuple[CastHeader, Generator[CastBody, None, None]]:
    return read_header(path), read_body(path)


def main():
    case_file = Path("./.recordings/16-05-2026_18-31-55.cast")
    header, body_stream = read_cast(case_file)

    font_path = Path(
        "~/.fonts/JetBrainsMonoNerdFontMono-Regular.ttf"
    ).expanduser()
    font = ImageFont.truetype(font_path, 20)
    fps = 30

    with Terminal(header.height, header.width) as term:
        renderer = TerminalRenderer(term, font)
        with Popen(
            [
                "ffmpeg",
                "-y",
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
                "-pix_fmt",
                "yuv420p",
                "output.mp4",
            ],
            stdin=PIPE,
        ) as ffmpeg:
            for body in body_stream:
                term.feed(body.text)
                frame = renderer.render()

                assert ffmpeg.stdin
                ffmpeg.stdin.write(frame.tobytes())


if __name__ == "__main__":
    main()
