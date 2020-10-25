# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ
#
# This is the SA162 (aka NE602).  Completely standard DIP8
# package, except the ground is on pin 3.  We also leave more
# room on the corner pins to make soldering easier.
#
import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class SA612(Compound):
    # A common component used to create the layout for a DIP package
    pitch_mm = 2.54
    width_mm = 25

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines from bottom up
        start_point = rotate((0, -1.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, -1.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 1.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 1.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 2.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 2.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 3.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 3.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 5.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 5.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical lines from left to right

        # Notice some special treatment on pin 3 here (unusual ground)
        start_point = rotate((0, -1.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 1.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 2.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 5.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((self.width_mm / 2.0, -1.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm / 2.0, 5.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((self.width_mm, -1.0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 5.0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="SA612",
                               fill='#00ff00')
