# SCAM G-Code Generator
# (c) 2024 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class LM380(Compound):

    # A common component used to create the layout for a DIP package
    pitch_mm = 2.54
    width_mm = 20

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal
        start_point = rotate((0, 7 * self.pitch_mm), rotation_ccw)
        end_point = rotate((20, 7 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((20, 8 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 8 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 9 * self.pitch_mm), rotation_ccw)
        end_point = rotate((20, 9 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((25, 8 * self.pitch_mm), rotation_ccw)
        end_point = rotate((40, 8 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((45, 9 * self.pitch_mm), rotation_ccw)
        end_point = rotate((25, 9 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((40, 5 * self.pitch_mm), rotation_ccw)
        end_point = rotate((45, 5 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((25, 3 * self.pitch_mm), rotation_ccw)
        end_point = rotate((45, 3 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((45, 1 * self.pitch_mm), rotation_ccw)
        end_point = rotate((25, 1 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((35, 0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((40, 0 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        # Vertical
        start_point = rotate((25, 3 * self.pitch_mm), rotation_ccw)
        end_point = rotate((25, 1 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((35, 0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((35, 1 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((40, 0 * self.pitch_mm), rotation_ccw)
        end_point = rotate((40, 3 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((45, 3 * self.pitch_mm), rotation_ccw)
        end_point = rotate((45, 1 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((25, 8 * self.pitch_mm), rotation_ccw)
        end_point = rotate((25, 9 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((40, 9 * self.pitch_mm), rotation_ccw)
        end_point = rotate((40, 5 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((45, 5 * self.pitch_mm), rotation_ccw)
        end_point = rotate((45, 9 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((20, 9 * self.pitch_mm), rotation_ccw)
        end_point = rotate((20, 7 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))

        start_point = rotate((0, 7 * self.pitch_mm), rotation_ccw)
        end_point = rotate((0, 9 * self.pitch_mm), rotation_ccw)
        self.add(self.NO_OFFSET, Line(start_point, end_point))


    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="LM380",
                               fill='#00ff00')
