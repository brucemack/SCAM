from Element import Element;


class Rectangle(Element):

    def __init__(self, point_0, point_1):
        self.points = []
        self.points.append(point_0)
        self.points.append(point_1)

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):
        # Make the required adjustments
        points_scaled = []
        for point in self.points:
            point_translated = origin_x_mm + point[0], origin_y_mm + point[1]
            points_scaled.append(self.u2px_2d(point_translated, params))

        canvas.create_rectangle(points_scaled[0][0],
            params.height - points_scaled[0][1],
            points_scaled[1][0],
            params.height - points_scaled[1][1], fill="red")

        """
        canvas.create_line(points_scaled[0][0],
                           params.height - points_scaled[0][1],
                           points_scaled[1][0],
                           params.height - points_scaled[1][1],
                           fill=color)
        canvas.create_line(points_scaled[1][0],
                           params.height - points_scaled[1][1],
                           points_scaled[2][0],
                           params.height - points_scaled[2][1],
                           fill=color)
        canvas.create_line(points_scaled[2][0],
                           params.height - points_scaled[2][1],
                           points_scaled[3][0],
                           params.height - points_scaled[3][1],
                           fill=color)
        canvas.create_line(points_scaled[3][0],
                           params.height - points_scaled[3][1],
                           points_scaled[0][0],
                           params.height - points_scaled[0][1],
                           fill=color)
        """

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, params):
        # Determine the z depth for each pass
        z_inc = depth_mm / params.passes
        z = 0
        # Position the tool at the start (Rapid)
        gcode_stream.out("G00 X" + gcode_stream.dec4(self.points[0][0]) + " Y" +
                         gcode_stream.dec4(self.points[0][1]))
        for p in range(params.passes):
            # Increase the depth
            z = z + z_inc
            gcode_stream.comment("Pass " + str(p) + " at depth " + str(z))
            # Put the tool into the piece
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_z))
            gcode_stream.out("G01 Z" + gcode_stream.dec4(z))
            # Mill to each point
            """
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_xy))
            gcode_stream.out("G01 X" + gcode_stream.dec4(self.points[1][0]) + " Y" +
                             gcode_stream.dec4(self.points[1][1]))
            gcode_stream.out("G01 X" + gcode_stream.dec4(self.points[2][0]) + " Y" +
                             gcode_stream.dec4(self.points[2][1]))
            gcode_stream.out("G01 X" + gcode_stream.dec4(self.points[3][0]) + " Y" +
                             gcode_stream.dec4(self.points[3][1]))
            gcode_stream.out("G01 X" + gcode_stream.dec4(self.points[0][0]) + " Y" +
                             gcode_stream.dec4(self.points[0][1]))
            """
            # Pull the tool out of the piece
            gcode_stream.out("G00 Z" + gcode_stream.dec4(params.travel_z))
