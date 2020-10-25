# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from utils import *


class Trace(Compound):
    # A common component used to create a rectangular trace

    pitch_mm = 6

    def __init__(self, width_mm, height_mm, rotation_ccw=0):
        super().__init__()
        self.rotation_ccw = rotation_ccw

        # Horizontal
        start_point = 0, 0
        end_point = width_mm, 0
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))
        start_point = 0, height_mm
        end_point = width_mm, height_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))
        # Vertical
        start_point = 0, 0
        end_point =  0, height_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))
        start_point = width_mm, 0
        end_point = width_mm, height_mm
        self.add(self.NO_OFFSET, Line(rotate(start_point, rotation_ccw), rotate(end_point, rotation_ccw)))

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Normal rendering process
        super().render(canvas, origin_x_mm, origin_y_mm, color, params)

