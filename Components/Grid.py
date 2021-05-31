# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class Grid(Compound):
    """ A common component used to create the layout for a grid pattern.
    """
    def __init__(self, cols, rows, rotation_ccw=0, pitch_mm=6):
        super().__init__()
        self.cols = cols
        self.rows = rows
        self.rotation_ccw = rotation_ccw
        self.pitch_mm = pitch_mm
        # Horizontal
        for row in range(self.rows + 1):
            start_point = 0, row * self.pitch_mm
            end_point = self.cols * self.pitch_mm, row * self.pitch_mm
            self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))
        # Vertical
        for col in range(self.cols + 1):
            start_point = col * self.pitch_mm, 0
            end_point = col * self.pitch_mm, self.rows * self.pitch_mm
            self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal rendering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text=str(self.cols) + "x" + str(self.rows) + " " + str(self.pitch_mm) + "mm",
                               fill='#00ff00')

