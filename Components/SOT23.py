# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ
#
# This is the SC70 package
#
import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class SOT23(Compound):

    pitch_mm = 5.0

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines from bottom up
        start_point = rotate((0.0 * self.pitch_mm, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.pitch_mm,   0.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.0 * self.pitch_mm, 1.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.pitch_mm,   1.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.0 * self.pitch_mm, 2.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.pitch_mm,   2.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((1.0 * self.pitch_mm, 0.5 * self.pitch_mm), rotation_ccw)
        end_point = rotate((2.0 * self.pitch_mm,   0.5 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((1.0 * self.pitch_mm, 1.5 * self.pitch_mm), rotation_ccw)
        end_point = rotate((2.0 * self.pitch_mm,   1.5 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical lines from left to right
        start_point = rotate((0.0 * self.pitch_mm, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0.0 * self.pitch_mm,   2.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((1.0 * self.pitch_mm, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.pitch_mm,   2.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((2.0 * self.pitch_mm, 0.5 * self.pitch_mm), rotation_ccw)
        end_point = rotate((2.0 * self.pitch_mm,   1.5 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="SOT23",
                               fill='#00ff00')
