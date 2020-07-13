from Element import Element;


class Line(Element):

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def render(self, canvas, origin_x_mm, origin_y_mm, height, color, scaling):
        canvas.create_line(self.u2px(origin_x_mm + self.x, scaling),
                           height - self.u2px(origin_y_mm + self.y, scaling),
                           self.u2px(origin_x_mm + self.x + self.dx, scaling),
                           height - self.u2px(origin_y_mm + self.y + self.dy, scaling), fill=color)

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, params):
        z_inc = depth_mm / params.passes
        z = z_inc
        for p in range(params.passes):
            gcode_stream.comment("Pass " + str(p) + " at depth " + str(z))
            # Position the tool (Rapid)
            gcode_stream.out("G00 X" + gcode_stream.dec4(origin_x_mm + self.x) + " Y" +
                             gcode_stream.dec4(origin_y_mm + self.y))
            # Put the tool into the piece
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_z))
            gcode_stream.out("G01 Z" + gcode_stream.dec4(z))
            # Mill
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_xy))
            gcode_stream.out("G01 X" + gcode_stream.dec4(origin_x_mm + self.x + self.dx) + " Y" +
                             gcode_stream.dec4(origin_y_mm + self.y + self.dy))
            # Pull the tool out of the piece
            gcode_stream.out("G00 Z" + gcode_stream.dec4(params.travel_z))
            z = z + z_inc
