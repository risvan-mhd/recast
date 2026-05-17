from dataclasses import dataclass
from typing import Any, Generator
from pathlib import Path
import json

from terminal import Terminal


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

    with Terminal(header.height, header.width) as term:
        for body in body_stream:
            term.feed(body.text)

            for row in range(term.rows):
                for col in range(term.cols):
                    print(term.cell(row, col))


if __name__ == "__main__":
    main()
