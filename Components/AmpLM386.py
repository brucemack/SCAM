# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ


import tkinter as tk
from Compound import Compound
from Line import Line


class AmpLM386(Compound):
    # A common component used to create the layout for an LM386 audio amplifier.

    pitch_mm = 2.54
    width_mm = 20

    def __init__(self, ground_pin= False):
        super().__init__()

        # Horizontal
        self.add(self.NO_OFFSET, Line(0.5 * self.width_mm, 0.0 * self.pitch_mm, 0.75 * self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0.5 * self.width_mm, 3.0 * self.pitch_mm, 0.5 * self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0,                   4.0 * self.pitch_mm, 1.25 * self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0,                   5.0 * self.pitch_mm, 1.0 * self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0,                   6.0 * self.pitch_mm, 1.0 * self.width_mm, 0))
        self.add(self.NO_OFFSET, Line(0,                  10.0 * self.pitch_mm, 1.0 * self.width_mm, 0))

        # Vertical
        self.add(self.NO_OFFSET, Line(0, 4.0 * self.pitch_mm, 0, 6.0 * self.pitch_mm))
        self.add(self.NO_OFFSET, Line(self.width_mm / 2 , 3.0 * self.pitch_mm, 0, 7.0 * self.pitch_mm))
        self.add(self.NO_OFFSET, Line(0.5 * self.width_mm, 0 * self.pitch_mm, 0, 3.0 * self.pitch_mm))
        self.add(self.NO_OFFSET, Line(self.width_mm, 0.0 * self.pitch_mm, 0, 10.0 * self.pitch_mm))
        self.add(self.NO_OFFSET, Line(1.25 * self.width_mm, 0.0 * self.pitch_mm, 0, 4.0 * self.pitch_mm))

    def render(self, canvas, origin_x_mm, origin_y_mm, height, color, scaling):
        # Normal rendering process
        super().render(canvas, origin_x_mm, origin_y_mm, height, color, scaling)
        # Text overlay
        t = canvas.create_text(self.u2px(origin_x_mm + 0.5, scaling),
                               height - self.u2px(origin_y_mm, scaling),
                               anchor=tk.SW,
                               text="LM386",
                               fill='#00ff00')
