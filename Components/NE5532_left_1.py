# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class NE5532_left_1(Compound):

    # A common component used to create the layout for a DIP package
    pitch_mm = 2.54
    width_mm = 20

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal
        start_point = rotate((0, 1 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 1 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((self.width_mm, 2 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 2 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 5 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 5 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical
        start_point = rotate((self.width_mm, 5 * self.pitch_mm), rotation_ccw)
        end_point = rotate((self.width_mm, 1 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 1 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 5 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="NE5532L1",
                               fill='#00ff00')
