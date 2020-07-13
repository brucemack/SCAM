# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line


class Grid(Compound):
    # A common component used to create the layout for a grid pattern.

    pitch_mm = 6

    def __init__(self, cols, rows):
        super().__init__()
        self.cols = cols
        self.rows = rows
        # Horizontal
        for row in range(self.rows + 1):
            self.add(self.NO_OFFSET, Line(0, row * self.pitch_mm, self.cols * self.pitch_mm, 0))
        # Vertical
        for col in range(self.cols + 1):
            self.add(self.NO_OFFSET, Line(col * self.pitch_mm, 0, 0, self.rows * self.pitch_mm))

    def render(self, canvas, origin_x_mm, origin_y_mm, height, color, scaling):
        # Normal rendering process
        super().render(canvas, origin_x_mm, origin_y_mm, height, color, scaling)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, scaling),
                               height - self.u2px(origin_y_mm, scaling),
                               anchor=tk.SW,
                               text=str(self.cols) + "x" + str(self.rows) + " " + str(self.pitch_mm) + "mm",
                               fill='#00ff00')

