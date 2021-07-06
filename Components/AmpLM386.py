# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ


import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class AmpLM386(Compound):
    # A common component used to create the layout for an LM386 audio amplifier.

    pitch_mm = 2.54
    width_mm = 25

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines
        start_point = rotate((0.5 * self.width_mm, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.25 * self.width_mm, 0.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.5 * self.width_mm, 3.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width_mm, 3.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.0 * self.width_mm, 4.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.25 * self.width_mm, 4.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(0,                   5.0 * self.pitch_mm, 1.0 * self.width_mm, 0))
        start_point = rotate((0.0 * self.width_mm, 5.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width_mm, 5.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(0,                   6.0 * self.pitch_mm, 1.0 * self.width_mm, 0))
        start_point = rotate((0.0 * self.width_mm, 6.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width_mm, 6.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # self.add(self.NO_OFFSET, Line(0,                  10.0 * self.pitch_mm, 1.0 * self.width_mm, 0))
        start_point = rotate((0.0 * self.width_mm, 10.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width_mm, 10.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical
        start_point = rotate((0, 4.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 5.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 6.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 10.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((self.width_mm / 2, 3.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm / 2, 10.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((self.width_mm / 2, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm / 2, 3.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((self.width_mm, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 10.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((1.25 * self.width_mm, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.25 * self.width_mm, 4.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal rendering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="LM386",
                               fill='#00ff00')
