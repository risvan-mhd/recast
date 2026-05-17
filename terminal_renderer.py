from PIL.ImageFont import FreeTypeFont
from PIL import Image, ImageDraw

from terminal import Terminal


class TerminalRenderer:
    def __init__(self, term: Terminal, font: FreeTypeFont) -> None:
        self.term = term
        self.font = font

        self.cell_width, self.cell_height = self.cell_size()
        self.width, self.height = self.image_size()

        self.frame = Image.new("RGB", (self.width, self.height), self.term.bg_color.to_tuple())  # type: ignore

    def cell_size(self) -> tuple[int, int]:
        left, _, right, _ = self.font.getbbox("M")
        ascent, descent = self.font.getmetrics()

        cell_width = right - left
        cell_height = ascent + descent

        return cell_width, cell_height

    def image_size(self) -> tuple[int, int]:
        width = self.term.cols * self.cell_width
        height = self.term.rows * self.cell_height

        return width, height

    def render(self) -> Image.Image:
        frame = self.frame.copy()
        draw = ImageDraw.Draw(frame)
        for cell in self.term:
            x = cell.col * self.cell_width
            y = cell.row * self.cell_height

            if cell.bg != self.term.bg_color:
                draw.rectangle(
                    (x, y, x + self.cell_width, y + self.cell_height),
                    cell.bg.to_tuple(),
                )

            if cell.char != " ":
                draw.text((x, y), cell.char, cell.fg.to_tuple(), font=self.font)

        return frame
