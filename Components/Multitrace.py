# SCAM G-Code Generator
# (c) 2021 Bruce MacKinnon KC1FSZ
import math
from Element import Element
from sympy import Polygon, pi, Point2D, Segment2D, Line2D
import utils


def make_square(origin_x_mm: float, origin_y_mm: float, p: Point2D, size) -> Polygon:
    half_size = size / 2.0
    return Polygon(p.translate(-half_size, -half_size),
                   p.translate(-half_size, +half_size),
                   p.translate(+half_size, +half_size),
                   p.translate(+half_size, -half_size)).translate(origin_x_mm, origin_y_mm)


def make_trace(origin_x_mm: float, origin_y_mm: float,
               sp: Point2D, ep: Point2D, width) -> Polygon:
    # Figure out the rotation angle between the two points (assuming the start point is fixed)
    rot = math.atan2(ep.y - sp.y, ep.x - sp.x)
    half_width = width / 2.0
    p0 = sp.translate(-0, -half_width).rotate(rot, sp)
    p1 = sp.translate(-0, +half_width).rotate(rot, sp)
    p2 = ep.translate(+half_width, +half_width).rotate(rot, ep)
    p3 = ep.translate(+half_width, -half_width).rotate(rot, ep)
    return Polygon(p0, p1, p2, p3).translate(origin_x_mm, origin_y_mm)


class Multitrace(Element):
    """ A point-to-point trace element """
    def __init__(self, points, end_size_mm = 6, trace_size = 3):
        if len(points) <= 1:
            raise ValueError("Too few points")
        self.end_pad_size = end_size_mm
        self.trace_size = trace_size
        # Convert the x/y tuples into Point2D objects
        self.points = [Point2D(point[0], point[1]) for point in points]

    def _generate_segments(self, origin_x_mm, origin_y_mm):
        """ Takes the points and turns them into a series of segments that define the
        outline.
        """
        polygons = []
        last_point_index = len(self.points) - 1

        # Make a starting pad
        polygons.append(make_square(origin_x_mm, origin_y_mm, self.points[0], self.end_pad_size))
        # Make an ending pad
        polygons.append(make_square(origin_x_mm, origin_y_mm, self.points[last_point_index], self.end_pad_size))
        # Make a connecting trace between the other points
        for i in range(0, len(self.points) - 1):
            polygons.append(make_trace(origin_x_mm, origin_y_mm, self.points[i], self.points[i + 1], self.trace_size))

        # Create a graph and add the polygons
        graph = utils.Graph()
        for p in polygons:
            graph.add_polygon(p)

        return graph.get_exterior_segments()

    def render(self, canvas, origin_x_mm, origin_y_mm, color, params):

        for seg in self._generate_segments(origin_x_mm, origin_y_mm):
            self._render_segment(canvas, seg, params, color)

    def _render_segment(self, canvas, seg: Segment2D, params, color):

        start_point_translated = seg.points[0].x, seg.points[0].y
        end_point_translated = seg.points[1].x, seg.points[1].y

        start_point_scaled = self.u2px_2d(start_point_translated, params)
        end_point_scaled = self.u2px_2d(end_point_translated, params)

        canvas.create_line(start_point_scaled[0],
                           params.height - start_point_scaled[1],
                           end_point_scaled[0],
                           params.height - end_point_scaled[1],
                           fill=color)

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, params):

        # All of the segments have the origin translation built in
        segments = self._generate_segments(origin_x_mm, origin_y_mm)
        start_point = segments[0].points[0]

        # Determine the z depth for each pass
        z_inc = depth_mm / params.passes
        z = 0

        # Position the tool at the start of the first segment (rapid)
        gcode_stream.out("G00 X" + gcode_stream.dec4(start_point.x) + " Y" + gcode_stream.dec4(start_point.y))

        for p in range(params.passes):

            # Put the tool into the piece
            # Increase the depth
            z = z + z_inc
            gcode_stream.comment("Pass " + str(p) + " at depth " + str(z))
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_z))
            gcode_stream.out("G01 Z" + gcode_stream.dec4(z))

            # Set the XY feed rate
            gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_xy))

            # Move to the end of each segment
            for seg in segments:
                end_point = seg.points[1].x, seg.points[1].y
                # Mill to the end point
                gcode_stream.out("G01 X" + gcode_stream.dec4(end_point[0]) + " Y" + gcode_stream.dec4(end_point[1]))

        # Pull the tool out of the piece after the last pass
        gcode_stream.out("G01 F" + gcode_stream.dec4(params.feedrate_z_out))
        gcode_stream.out("G00 Z" + gcode_stream.dec4(params.travel_z))
