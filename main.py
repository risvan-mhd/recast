from dataclasses import dataclass
from typing import Any, TextIO
from pathlib import Path
import json


@dataclass(frozen=True)
class CastHeader:
    width: int
    height: int


def read_header(file: TextIO) -> CastHeader:
    data: dict[str, Any] = json.loads(file.readline())

    for key in {"version", "width", "height"}:
        if key not in data:
            raise ValueError("Invalid file: could not find required param")

    assert data["version"] == 2
    return CastHeader(width=data["width"], height=data["height"])


def main():
    case_file = Path("./.recordings/16-05-2026_18-31-55.cast")
    with open(case_file, "r") as f:
        header = read_header(f)
        print(header)


if __name__ == "__main__":
    main()
