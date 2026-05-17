from dataclasses import dataclass
from typing import Generator, Self
from ctypes import byref

import libvterm as _vt


@dataclass(frozen=True)
class Cell:
    row: int
    col: int

    char: str


class Terminal:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols

        self._closed = False

        self._vt = _vt.vterm_new(rows, cols)
        self._screen = _vt.vterm_obtain_screen(self._vt)
        _vt.vterm_screen_reset(self._screen, 1)

    def __del__(self) -> None:
        try:
            if hasattr(self, "_closed") and not self._closed:
                _vt.vterm_free(self._vt)
                self._closed = True

        except Exception:
            pass

    def _ensure_open(self) -> None:
        if self._closed:
            raise RuntimeError("Terminal has been closed")

    def close(self) -> None:
        self._ensure_open()

        _vt.vterm_free(self._vt)
        self._closed = True

    def __enter__(self) -> Self:
        self._ensure_open()
        return self

    def __exit__(self, *_) -> None:
        self.close()

    def feed(self, text: str) -> None:
        self._ensure_open()

        data = text.encode("utf-8")
        _vt.vterm_input_write(self._vt, data, len(data))
        _vt.vterm_screen_flush_damage(self._screen)

    def cell(self, row: int, col: int) -> Cell:
        self._ensure_open()

        if not (0 <= row < self.rows):
            raise IndexError(f"row out of range: {row}")

        if not (0 <= col < self.cols):
            raise IndexError(f"col out of range: {col}")

        pos = _vt.VTermPos(row=row, col=col)
        raw_cell = _vt.VTermScreenCell()

        _vt.vterm_screen_get_cell(
            self._screen,
            pos,
            byref(raw_cell),
        )

        char = "".join(chr(cp) for cp in raw_cell.chars if cp != 0) or " "
        return Cell(
            row=row,
            col=col,
            char=char,
        )

    def __iter__(self) -> Generator[Cell, None, None]:
        self._ensure_open()

        for row in range(self.rows):
            for col in range(self.cols):
                yield self.cell(row, col)
