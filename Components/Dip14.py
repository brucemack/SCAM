# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line


class Dip14(Compound):
    # A common component used to create the layout for a DIP-14 package

    pitch_mm = 2.54
    width_mm = 25

    def __init__(self, ground_pin= False):
        super().__init__()
        # Horizontal
        if ground_pin:
            self.add(self.NO_OFFSET, Line(self.width_mm / 2, 0.0 * self.pitch_mm, self.width_mm / 2, 0))
        else:
            self.add(self.NO_OFFSET, Line(0, 0.0 * self.pitch_mm, self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0, 1.0 * self.pitch_mm, self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0, 2.0 * self.pitch_mm, self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0, 3.0 * self.pitch_mm, self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0, 4.0 * self.pitch_mm, self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0, 5.0 * self.pitch_mm, self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0, 6.0 * self.pitch_mm, self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0, 7.0 * self.pitch_mm, self.width_mm, 0))
        # Vertical
        if ground_pin:
            self.add(self.NO_OFFSET, Line(0, self.pitch_mm, 0, 6.0 * self.pitch_mm))
        else:
            self.add(self.NO_OFFSET, Line(0, 0, 0, 7.0 * self.pitch_mm))
        self.add(self.NO_OFFSET, Line(self.width_mm / 2., 0, 0, 7.0 * self.pitch_mm))
        self.add(self.NO_OFFSET, Line(self.width_mm, 0, 0, 7.0 * self.pitch_mm))

    def render(self, canvas, origin_x_mm, origin_y_mm, height, color, scaling):
        # Normal renedering process
        super().render(canvas, origin_x_mm, origin_y_mm, height, color, scaling)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, scaling),
                               height - self.u2px(origin_y_mm, scaling),
                               anchor=tk.SW,
                               text="DIP14",
                               fill='#00ff00')
