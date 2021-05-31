# SCAM G-Code Generator
# (c) 2021 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class Poly(Compound):

    def __init__(self, points, pitch_mm=6.0, rotation_ccw=0):

        super().__init__()

        self.pitch_mm = pitch_mm
        self.rotation_ccw = rotation_ccw

        last_point = None
        for point in points:
            if last_point is not None:
                start_point = rotate((last_point[0] * self.pitch_mm, last_point[1] * self.pitch_mm), rotation_ccw)
                end_point = rotate((point[0] * self.pitch_mm, point[1] * self.pitch_mm), rotation_ccw)
                self.add(self.NO_OFFSET, Line(start_point, end_point))
            last_point = point

        # Close the loop
        start_point = rotate((last_point[0] * self.pitch_mm, last_point[1] * self.pitch_mm), rotation_ccw)
        end_point = rotate((points[0][0] * self.pitch_mm, points[0][1] * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               text="Polygon",
                               angle=self.rotation_ccw,
                               fill='#00ff00')
