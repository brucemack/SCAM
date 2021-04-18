# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ
from Element import Element


class Multitrace(Element):

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        [i[1].render(canvas, origin_x_mm + i[0][0], origin_y_mm + i[0][1], color, params) for i in self.list]

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, params):
        [i[1].mill(gcode_stream, origin_x_mm + i[0][0], origin_y_mm + i[0][1], depth_mm, params) for i in self.list]

