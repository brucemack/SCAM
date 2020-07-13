# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ
from Element import Element


class Compound(Element):
    # This element type is used to organize a set of child elements under a local
    # coordinate system.

    NO_OFFSET = (0, 0)

    def __init__(self):
        self.list = []

    def add(self, offset, el):
        self.list.append((offset, el))

    def render(self, canvas, origin_x_mm, origin_y_mm, height, color, scaling):
        [i[1].render(canvas, origin_x_mm + i[0][0], origin_y_mm + i[0][1], height, color, scaling) for i in self.list]

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, params):
        [i[1].mill(gcode_stream, origin_x_mm + i[0][0], origin_y_mm + i[0][1], depth_mm, params) for i in self.list]
