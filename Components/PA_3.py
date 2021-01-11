# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class PA_3(Compound):

    pitch_mm = 5

    def line(self, start, end):
        start_point = rotate((start[0] * self.pitch_mm, start[1] * self.pitch_mm), self.rotation_ccw)
        end_point = rotate((end[0] * self.pitch_mm, end[1] * self.pitch_mm), self.rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines
        self.line((6, 0), (7, 0))
        self.line((6, 1), (7, 1))
        self.line((2.5, 1.5), (5, 1.5))
        self.line((6, 1.5), (7, 1.5))
        self.line((1.5, 2.5), (5, 2.5))
        self.line((6, 2.5), (8.5, 2.5))
        self.line((0, 3.5), (1, 3.5))
        self.line((2, 3.5), (5, 3.5))
        self.line((6, 3.5), (7.5, 3.5))
        self.line((0, 4.5), (1, 4.5))
        self.line((2.5, 4.5), (5, 4.5))
        self.line((6, 4.5), (7, 4.5))
        self.line((6, 5), (7, 5))
        self.line((6, 6), (7, 6))

        # Track ends
        self.line((1.5, 7.5), (2, 7.5))
        self.line((7.5, 7.5), (8.5, 7.5))

        # Vertical
        self.line((0, 3.5), (0, 4.5))
        self.line((1, 3.5), (1, 4.5))

        # Left Track
        self.line((1.5, 2.5), (1.5, 7.5))
        self.line((2, 3.5), (2, 7.5))

        self.line((2.5, 1.5), (2.5, 2.5))
        self.line((2.5, 3.5), (2.5, 4.5))
        self.line((5, 1.5), (5, 4.5))

        self.line((6, 0), (6, 1))
        self.line((6, 1.5), (6, 4.5))
        self.line((6, 5), (6, 6))
        self.line((7, 0), (7, 1))
        self.line((7, 1.5), (7, 2.5))
        self.line((7, 3.5), (7, 4.5))
        self.line((7, 5), (7, 6))
        # Right track
        self.line((7.5, 3.5), (7.5, 7.5))
        self.line((8.5, 2.5), (8.5, 7.5))


    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               text="PA_3",
                               angle=self.rotation_ccw,
                               fill='#00ff00')
