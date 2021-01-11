# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class PA_4(Compound):
    """
    This is the output side of the IRF510 push-pull PA
    """
    pitch_mm = 5

    def line(self, start, end):
        start_point = rotate((start[0] * self.pitch_mm, start[1] * self.pitch_mm), self.rotation_ccw)
        end_point = rotate((end[0] * self.pitch_mm, end[1] * self.pitch_mm), self.rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines
        self.line((5, 0), (10, 0))
        self.line((5, 1), (8, 1))
        self.line((0, 1.5), (7, 1.5))
        self.line((0, 3.5), (7, 3.5))
        self.line((0, 4), (7, 4))
        self.line((0, 6), (7, 6))
        self.line((5, 6.5), (8, 6.5))
        self.line((5, 7.5), (8, 7.5))

        self.line((5, 0), (5, 1))
        self.line((5, 6.5), (5, 7.5))
        self.line((8, 1), (8, 6.5))
        self.line((8, 7.5), (8, 10))
        self.line((10, 0), (10, 10))

        self.line((0, 1.5), (0, 3.5))
        self.line((0, 4), (0, 6))
        self.line((7, 1.5), (7, 3.5))
        self.line((7, 4), (7, 6))



    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               text="PA_4",
                               angle=self.rotation_ccw,
                               fill='#00ff00')
