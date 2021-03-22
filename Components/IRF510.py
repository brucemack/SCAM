# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class IRF510(Compound):
    """
    This is the input side of the IRF510
    """
    pitch_mm = 2.54

    def line(self, start, end):
        start_point = rotate((start[0] * self.pitch_mm, start[1] * self.pitch_mm), self.rotation_ccw)
        end_point = rotate((end[0] * self.pitch_mm, end[1] * self.pitch_mm), self.rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def square(self, start, size):
        self.line(start, (start[0] + size[0], start[1]))
        self.line((start[0], start[1] + size[1]), (start[0] + size[0], start[1] + size[1]))
        self.line((start[0], start[1]), (start[0], start[1] + size[1]))
        self.line((start[0] + size[0], start[1]), (start[0] + size[0], start[1] + size[1]))

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        self.square((0, 0), (6, 1))
        self.square((2, 1), (4, 3))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               text="IRF510",
                               angle=self.rotation_ccw,
                               fill='#00ff00')
