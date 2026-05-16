from typing import Self
import libvterm as _vt


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
