from dataclasses import dataclass
from typing import Generator, Self
from ctypes import byref

import libvterm as _vt


@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

    def to_tuple(self) -> tuple[int, int, int]:
        return (
            self.r,
            self.g,
            self.b,
        )


@dataclass(frozen=True)
class Cell:
    row: int
    col: int

    char: str
    fg: Color
    bg: Color


class Terminal:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols

        self.bg_color = rgb("#1e1e2e")
        self.fg_color = rgb("#cdd6f4")
        self.indexed_colors = [
            # Catppuccin Mocha
            rgb("#45475a"),
            rgb("#f38ba8"),
            rgb("#a6e3a1"),
            rgb("#f9e2af"),
            rgb("#89b4fa"),
            rgb("#f5c2e7"),
            rgb("#94e2d5"),
            rgb("#bac2de"),
            rgb("#585b70"),
            rgb("#f38ba8"),
            rgb("#a6e3a1"),
            rgb("#f9e2af"),
            rgb("#89b4fa"),
            rgb("#f5c2e7"),
            rgb("#94e2d5"),
            rgb("#a6adc8"),
        ]
        levels = (0, 95, 135, 175, 215, 255)
        self.indexed_colors.extend(
            Color(r, g, b)
            for r in levels
            for g in levels
            for b in levels  # XTerm RGB cube
        )
        self.indexed_colors.extend(
            Color(level, level, level)
            for level in range(8, 239, 10)  # Grayscale
        )

        self._closed = False

        self._vt = _vt.vterm_new(rows, cols)
        _vt.vterm_set_utf8(self._vt, 1)
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

    def _color(self, c) -> Color:
        match c.type:
            case 0:  # RGB:
                r = c.rgb.red
                g = c.rgb.green
                b = c.rgb.blue
                return Color(r, g, b)

            case 1:  # Indexed ANSI Color
                return self.indexed_colors[c.indexed.idx]

            case 2:
                return self.fg_color

            case 4:
                return self.bg_color

            case _:
                raise ValueError(f"Unknown color type: {c.type}")

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

        raw_chars_list = [raw_cell.chars[i] for i in range(6)]
        # print(
        #     f"DEBUG [{row},{col}]: width={getattr(raw_cell, 'width', 'N/A')}, raw_chars={raw_chars_list}"
        # )

        # import ctypes
        #
        # cell_address = ctypes.addressof(raw_cell)
        # raw_bytes = ctypes.string_at(
        #     cell_address, 24
        # )  # read just the chars array bytes
        #
        # print("RAW BYTES IN MEMORY (HEX):", raw_bytes.hex())
        #
        # # 2. Let's see what integers Python actually pulls out of the array slots
        # for i in range(6):
        #     print(
        #         f"Slot {i} integer: {raw_cell.chars[i]} (Hex: {hex(raw_cell.chars[i])})"
        #     )

        fg = self._color(raw_cell.fg)
        bg = self._color(raw_cell.bg)

        char = "".join(chr(cp) for cp in raw_cell.chars if cp != 0) or " "
        return Cell(
            row=row,
            col=col,
            char=char,
            fg=fg,
            bg=bg,
        )

    def __iter__(self) -> Generator[Cell, None, None]:
        self._ensure_open()

        for row in range(self.rows):
            for col in range(self.cols):
                yield self.cell(row, col)


def rgb(hex: str) -> Color:
    hex = hex.lstrip("#")
    return Color(*tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4)))
