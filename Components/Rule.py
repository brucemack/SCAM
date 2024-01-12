# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class Rule(Compound):

    def __init__(self, pitch_mm, length_units, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        start_point = 0, 0
        end_point = length_units * pitch_mm, 0
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal rendering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)

