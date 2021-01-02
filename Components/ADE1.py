# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class ADE1(Compound):
    # A common component used to create the layout for an ADE-1 mixer.

    pitch_mm = 2.54
    width_mm = 25

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines
        start_point = rotate((0, 0), rotation_ccw)
        end_point = rotate((0.5 * self.width_mm, 0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(0, 1.0 * self.pitch_mm, 0.5 * self.width_mm, 0))
        start_point = rotate((0, 1.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0.5 * self.width_mm, 1.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(0, 2.0 * self.pitch_mm, 1.0 * self.width_mm, 0))
        start_point = rotate((0, 2.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width_mm, 2.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(0.5 * self.width_mm, 3.0 * self.pitch_mm, 0.5 * self.width_mm, 0))
        start_point = rotate((0.5 * self.width_mm, 3.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width_mm, 3.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical lines
        # self.add(self.NO_OFFSET, Line(0, 0, 0, 2.0 * self.pitch_mm))
        start_point = rotate((0, 0), rotation_ccw)
        end_point = rotate((0, 2.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(0.5 * self.width_mm, 0, 0, 3.0 * self.pitch_mm))
        start_point = rotate((0.5 * self.width_mm, 0), rotation_ccw)
        end_point = rotate((0.5 * self.width_mm, 3.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(1.0 * self.width_mm, 2.0 * self.pitch_mm, 0, 1.0 * self.pitch_mm))
        start_point = rotate((1.0 * self.width_mm, 2.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width_mm, 3.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               text="ADE1",
                               angle=self.rotation_ccw,
                               fill='#00ff00')
