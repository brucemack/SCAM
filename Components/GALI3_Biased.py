# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class GALI3_Biased(Compound):

    pitch_mm_v = 2.54

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal lines
        start_point = rotate((5.5, -3 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((10.5, -3 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((-4, -1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((0, -1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, -1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((4.0, -1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((5.5, -1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((10.5, -1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((-4, 1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((0, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((4.0, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((5.5, 1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((10.5, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((15.5, 2 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((20, 2 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((15.5, 3 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((20, 3 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((15.5, 5 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((20, 5 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical
        start_point = rotate((-4, -1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((-4, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, -1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((0, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((4.0, -1 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((4.0, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((5.5, -3 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((5.5, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((10.5, -3 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((10.5, 1 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((15.5, 2 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((15.5, 5 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((20, 2 * self.pitch_mm_v), rotation_ccw)
        end_point = rotate((20, 5 * self.pitch_mm_v), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               text="GALI3",
                               angle=self.rotation_ccw,
                               fill='#00ff00')
