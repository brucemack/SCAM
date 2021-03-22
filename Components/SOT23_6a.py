# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ
#
# This is the SOT23-6 package with pin 2 grounded
#
import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class SOT23_6a(Compound):

    pitch_mm = 0.95
    width = 20
    adj_mm = 0.1

    def __init__(self, rotation_ccw=0, gnd2=True):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines from bottom up
        if gnd2:
            start_point = rotate((self.width * 0.25, 0.0 * self.pitch_mm), rotation_ccw)
            end_point = rotate((self.width, 0.0 * self.pitch_mm), rotation_ccw)
            self.add(self.NO_OFFSET, Line(start_point, end_point))
        else:
            start_point = rotate((0.0, 0.0 * self.pitch_mm), rotation_ccw)
            end_point = rotate((self.width, 0.0 * self.pitch_mm), rotation_ccw)
            self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.25 * self.width, 6.0 * self.pitch_mm - self.adj_mm), rotation_ccw)
        end_point = rotate((0.75 * self.width, 6.0 * self.pitch_mm - self.adj_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.25 * self.width, 7.0 * self.pitch_mm + self.adj_mm), rotation_ccw)
        end_point = rotate((0.75 * self.width, 7.0 * self.pitch_mm + self.adj_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        if gnd2:
            start_point = rotate((0.25 * self.width, 13.0 * self.pitch_mm), rotation_ccw)
            end_point = rotate((self.width, 13.0 * self.pitch_mm), rotation_ccw)
            self.add(self.NO_OFFSET, Line(start_point, end_point))
        else:
            start_point = rotate((0.0, 13.0 * self.pitch_mm), rotation_ccw)
            end_point = rotate((self.width, 13.0 * self.pitch_mm), rotation_ccw)
            self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical
        if not gnd2:
            start_point = rotate((0.0, 0.0 * self.pitch_mm), rotation_ccw)
            end_point = rotate((0.0, 13.0 * self.pitch_mm), rotation_ccw)
            self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.25 * self.width, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0.25 * self.width, 6.0 * self.pitch_mm - self.adj_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.25 * self.width, 7.0 * self.pitch_mm + self.adj_mm), rotation_ccw)
        end_point = rotate((0.25 * self.width, 13.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.5 * self.width, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0.5 * self.width, 13.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.75 * self.width, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0.75 * self.width, 6.0 * self.pitch_mm - self.adj_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0.75 * self.width, 7.0 * self.pitch_mm + self.adj_mm), rotation_ccw)
        end_point = rotate((0.75 * self.width, 13.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((1.0 * self.width, 0.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((1.0 * self.width, 13.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))


    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="SOT23-6",
                               fill='#00ff00')
