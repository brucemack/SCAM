# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class DBM(Compound):
    # A common component used to create the layout for a double-balanced
    # diode ring mixer.

    pitch_mm = 8

    def __init__(self, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw
        # Horizontal
        start_point = 1.0 * self.pitch_mm, 0
        end_point = 4.0 * self.pitch_mm, 0
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 1.0 * self.pitch_mm, 1.0 * self.pitch_mm
        end_point = 5.0 * self.pitch_mm, 1.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 0.0 * self.pitch_mm, 2.0 * self.pitch_mm
        end_point = 5.0 * self.pitch_mm, 2.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 0.0 * self.pitch_mm, 3.0 * self.pitch_mm
        end_point = 4.0 * self.pitch_mm, 3.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 1.0 * self.pitch_mm, 4.0 * self.pitch_mm
        end_point = 2.0 * self.pitch_mm, 4.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        # Vertical
        start_point = 0.0 * self.pitch_mm, 2.0 * self.pitch_mm
        end_point = 0.0 * self.pitch_mm, 3.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 1.0 * self.pitch_mm, 0.0 * self.pitch_mm
        end_point = 1.0 * self.pitch_mm, 1.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 1.0 * self.pitch_mm, 2.0 * self.pitch_mm
        end_point = 1.0 * self.pitch_mm, 4.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 2.0 * self.pitch_mm, 1.0 * self.pitch_mm
        end_point = 2.0 * self.pitch_mm, 2.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 2.0 * self.pitch_mm, 3.0 * self.pitch_mm
        end_point = 2.0 * self.pitch_mm, 4.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 3.0 * self.pitch_mm, 1.0 * self.pitch_mm
        end_point = 3.0 * self.pitch_mm, 2.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 4.0 * self.pitch_mm, 0.0 * self.pitch_mm
        end_point = 4.0 * self.pitch_mm, 3.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

        start_point = 5.0 * self.pitch_mm, 1.0 * self.pitch_mm
        end_point = 5.0 * self.pitch_mm, 2.0 * self.pitch_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal rendering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, params),
                               params.height - self.u2px(origin_y_mm, params),
                               anchor=tk.SW,
                               angle=self.rotation_ccw,
                               text="DBM",
                               fill='#00ff00')

