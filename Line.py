from Element import Element;


class Line(Element):

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):

        start_point_translated = origin_x_mm + self.start_point[0], origin_y_mm + self.start_point[1]
        end_point_translated = origin_x_mm + self.end_point[0], origin_y_mm + self.end_point[1]
        start_point_scaled = self.u2px_2d(start_point_translated, params)
        end_point_scaled = self.u2px_2d(end_point_translated, params)

        canvas.create_line(start_point_scaled[0],
                           params.height - start_point_scaled[1],
                           end_point_scaled[0],
                           params.height - end_point_scaled[1],
                           fill=color)

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, params):
        # Determine the z depth for each pass
        z_inc = depth_mm / params.passes
        z = 0
        for p in range(params.passes):
            # Increase the depth
            z = z + z_inc
            gcode_stream.comment("Pass " + str(p) + " at depth " + str(z))
            start_point = origin_x_mm + self.start_point[0], origin_y_mm + self.start_point[1]
            end_point = origin_x_mm + self.end_point[0], origin_y_mm + self.end_point[1]
            # Dean KK4DAS has suggested that milling in the -Y direction (towards the
            # bottom of the work piece looking down on it) may have problems
            # on the CNC 3018 so we adjust the direction of work accordingly
            if start_point[1] > end_point[1]:
                hold = start_point
                start_point = end_point
                end_point = hold
            # Position the tool at the start (Rapid)
            gcode_stream.out("G00 X" + gcode_stream.dec4(start_point[0]) + " Y" +
                             gcode_stream.dec4(start_point[1]))
            # Put the tool into the piece
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_z))
            gcode_stream.out("G01 Z" + gcode_stream.dec4(z))
            # Mill to the end point
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_xy))
            gcode_stream.out("G01 X" + gcode_stream.dec4(end_point[0]) + " Y" +
                             gcode_stream.dec4(end_point[1]))
            # Pull the tool out of the piece
            gcode_stream.out("G00 Z" + gcode_stream.dec4(params.travel_z))
