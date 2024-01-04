# SCAM G-Code Generator
# (c) 2023 Bruce MacKinnon KC1FSZ
#
# This is the SOT23-6 package with pin 2 grounded
#
import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *

class LMV321_a(Compound):

    def __init__(self, rotation_ccw=0, gnd2=True):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines from bottom up
        start_point = rotate(( 0.0,  0.0), rotation_ccw)
        end_point =   rotate((35.0,  0.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate(( 0.0,  7.0), rotation_ccw)
        end_point =   rotate((35.0,  7.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate(( 0.0,  8.0), rotation_ccw)
        end_point =   rotate((35.0,  8.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate(( 0.0, 15.0), rotation_ccw)
        end_point =   rotate((35.0, 15.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical from left to right
        start_point = rotate(( 0.0,  0.0), rotation_ccw)
        end_point =   rotate(( 0.0,  7.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate(( 0.0,  8.0), rotation_ccw)
        end_point =   rotate(( 0.0, 15.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate(( 5.0,  0.0), rotation_ccw)
        end_point =   rotate(( 5.0,  7.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate(( 5.0,  8.0), rotation_ccw)
        end_point =   rotate(( 5.0, 15.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((10.0,  0.0), rotation_ccw)
        end_point =   rotate((10.0,  7.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((10.0,  8.0), rotation_ccw)
        end_point =   rotate((10.0, 15.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((20.0,  0.0), rotation_ccw)
        end_point =   rotate((20.0, 7.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((20.0,  8.0), rotation_ccw)
        end_point =   rotate((20.0, 15.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((30.0,  0.0), rotation_ccw)
        end_point =   rotate((30.0, 7.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((30.0,  8.0), rotation_ccw)
        end_point =   rotate((30.0, 15.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((35.0,  0.0), rotation_ccw)
        end_point =   rotate((35.0, 7.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((35.0,  8.0), rotation_ccw)
        end_point =   rotate((35.0, 15.0), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="LMV321_a",
                               fill='#00ff00')
