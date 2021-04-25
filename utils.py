import math
from sympy import Polygon, pi, Point2D, Segment2D, Line2D


def rotate(coords, degrees):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in degrees.
    """
    angle = math.radians(degrees)
    origin = (0, 0)
    ox, oy = origin
    px, py = coords
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def round_coords(coords):
    return round(coords[0], 2), round(coords[1], 2)


def calc_rect_path(top_left, bottom_right, tool_diam):
    """ Creates the milling path for the outline of the specified
        rectangle.  The tool center is inside of the rectangle by
        half the width. """
    result = []
    adj = tool_diam / 2
    # Top left
    result.append((top_left[0] + adj, top_left[1] - adj))
    # Top right
    result.append((bottom_right[0] - adj, top_left[1] - adj))
    # Bottom right
    result.append((bottom_right[0] - adj, bottom_right[1] + adj))
    # Bottom left
    result.append((top_left[0] + adj, bottom_right[1] + adj))
    # Top left
    result.append((top_left[0] + adj, top_left[1] - adj))
    return result


def mill_calc_h(top_left, bottom_right, tool_diam):
    """ Takes a rectangle (defined by corners) and a tool diameter and generates
        the points on the milling path to clear the area.  We scan from top
        left to bottom right in all cases.
    """
    dy = bottom_right[1] - top_left[1]
    dx = bottom_right[0] - top_left[0]
    # Adjusted for tool
    adx = dx - tool_diam
    # Number of passes
    passes = math.ceil(math.fabs(dy) / tool_diam)
    # Pass offset
    pass_offset = dy / passes
    # Generate passes
    origin_x = top_left[0] + tool_diam / 2
    # Start tool a bit below the top of the edge (remember, we are
    # milling from the top down
    y = top_left[1] - (tool_diam / 2)
    result = []
    for p in range(0, passes):
        # Even passes go left to right
        if p % 2 == 0:
            result.append((origin_x, y))
            result.append((origin_x + adx, y))
        # Odd passes to right to left
        elif p % 2 == 1:
            result.append((origin_x + adx, y))
            result.append((origin_x, y))
        # Move up
        y = y + pass_offset
    return result


def mill_calc_v(top_left, bottom_right, tool_diam):
    """ Takes a rectangle (defined by corners) and a tool diameter and generates
        the points on the milling path to clear the area.  We scan from top
        left to bottom right in all cases.
    """
    dy = bottom_right[1] - top_left[1]
    dx = bottom_right[0] - top_left[0]
    # Number of passes is based on the width (dx) of the area
    passes = math.ceil(math.fabs(dx) / tool_diam)
    # Pass offset
    pass_offset = dx / passes
    # Generate passes
    top_y = top_left[1] - (tool_diam / 2)
    bottom_y = bottom_right[1] + (tool_diam / 2)
    x = top_left[0] + (tool_diam / 2)
    result = []
    for p in range(0, passes):
        # Even passes go top to bottom
        if p % 2 == 0:
            result.append((x, top_y))
            result.append((x, bottom_y))
        # Odd passes to right to left
        elif p % 2 == 1:
            result.append((x, bottom_y))
            result.append((x, top_y))
        # Move right
        x = x + pass_offset
    return result


def ccw_angle(a: Point2D, b: Point2D, c: Point2D):
    """ This function looks at three points and returns the CCW angle formed between them
    considering point b is the vertex.  The result will be from 0 to 359 (i.e. no negative
    angles will be returned.
    """
    # Normalize everything back to the origin
    v1 = a.x - b.x, a.y - b.y
    v2 = c.x - b.x, c.y - b.y
    # Both angles are relative to the x-axis
    angle = math.atan2(v2[1], v2[0]) - math.atan2(v1[1], v1[0])
    # Adjust for negative angles
    if angle < 0:
        return 2.0 * math.pi + angle
    else:
        return angle


class Graph:

    def __init__(self):
        self.nodes = []

    def add_polygon(self, poly: Polygon):
        # Add the segments that make up the sides
        for side in poly.sides:
            self.add_segment(side)

    def add_segment(self, seg: Segment2D):
        # Find or create nodes for the end-points of the segment
        self.add_point(seg.points[0])
        self.add_point(seg.points[1])
        # Look for any crossings of existing edges in the graph
        crossing_points = self.find_crossing_points(seg)
        # Make sure each crossing point has a node in the graph
        for crossing_point in crossing_points:
            self.add_point(crossing_point)
        # Cross-connect the end-points of the new line to form a new edge,
        # leveraging all possible coincident nodes.
        # First, find the coincident nodes:
        incident_nodes = self.find_incident_nodes(seg)
        # Sort the incident nodes according to their distance from the starting point
        incident_nodes.sort(key=lambda n: n.point.distance(seg.points[0]))
        # Sanity check
        if incident_nodes[0].point != seg.points[0] or incident_nodes[-1].point != seg.points[1]:
            raise Exception("Unexpected result after sort")
        # Stitch together the neighbors from one end to the other
        last_node: Node = None
        for node in incident_nodes:
            if last_node is not None:
                last_node.add_neighbor_if_necessary(node)
                node.add_neighbor_if_necessary(last_node)
            last_node = node

    def find_incident_nodes(self, seg: Segment2D):
        """
        :param seg:
        :return: A list of all of the existing nodes that touch the specified segment
        """
        return [n for n in self.nodes if seg.contains(n.point)]

    def add_point(self, new_point: Point2D):
        """
        Adds a point to the graph and returns the node.  If the point coincides with an
        existing node then that node is returned.  If the point coincides with an existing
        edge then then edge is split and the new node is returned.  Otherwise a new (independent)
        node is returned.
        :param new_point:
        :return:
        """
        # Look for the node coincident case
        if new_point in [n.point for n in self.nodes]:
            return [n for n in self.nodes if n.point == new_point][0]
        else:
            # Look for the edge coincident case. Consider each node:
            for node in self.nodes:
                # Consider each edge from this node
                for neighbor_node in node.neighbors:
                    # Make a segment that represents the edge
                    seg = Segment2D(node.point, neighbor_node.point)
                    # Check to see if the new point lies on the line
                    if seg.contains(new_point):
                        #print("Splitting edge", node.point, neighbor_node.point, "at", new_point)
                        # If so then we add a new node and re-link the neighbor
                        # relationships
                        new_node = Node(new_point)
                        self.nodes.append(new_node)
                        # Break the old relationship
                        node.neighbors.remove(neighbor_node)
                        neighbor_node.neighbors.remove(node)
                        # Create new ones
                        node.neighbors.append(new_node)
                        new_node.neighbors.append(node)
                        neighbor_node.neighbors.append(new_node)
                        new_node.neighbors.append(neighbor_node)
                        return new_node
            # If we reach this point then no split was possible, make
            # a new node and return it
            new_node = Node(new_point)
            #print("No split possible, adding node with point", new_node.point)
            self.nodes.append(new_node)
            return new_node

    def find_crossing_points(self, new_seg: Segment2D):
        intersection_points = []
        # Look for the edge coincident case.
        # Consider each node
        for node in self.nodes:
            # Consider each edge
            for neighbor_node in node.neighbors:
                # Make a segment that represents the edge
                existing_seg = Segment2D(node.point, neighbor_node.point)
                # Take a look at intersections that aren't already represented by nodes in the graph.  Note that it
                # is possible that some of the intersections may be lines (in the case where the new line is
                # overlapping an existing edge).  But we don't care about those cases because they are already covered
                # by existing nodes in the graph.
                for intersection in existing_seg.intersection(new_seg):
                    if isinstance(intersection, Point2D):
                        # No duplicates allowed
                        if intersection not in intersection_points:
                            # Search through all of the nodes to see if this is an established point.
                            if intersection not in [n.point for n in self.nodes]:
                                intersection_points.append(intersection)
        return intersection_points

    def get_node_count(self) -> int:
        return len(self.nodes)

    def get_node_at_point(self, point: Point2D) -> 'Node':
        if point in [n.point for n in self.nodes]:
            return [n for n in self.nodes if n.point == point][0]
        else:
            raise Exception("Point not found in graph")

    def get_node_at_bottom_left(self) -> 'Node':
        bottom_left = Point2D(0, 0)
        smallest_distance = 0
        smallest_node = None
        for node in self.nodes:
            distance = bottom_left.distance(node.point)
            if smallest_node is None or distance < smallest_distance:
                smallest_node = node
                smallest_distance = distance
        return smallest_node

    def get_exterior_nodes(self):
        result = []
        # Start off with a dummy last point to get things going
        last_point = Point2D(0, -1)
        last_node = None
        starting_node = self.get_node_at_bottom_left()
        working_node = starting_node
        # We will keep on walking until we return to the original node.
        # A special pass is provided for the beginning of the walk.
        while working_node != starting_node or len(result) == 0:
            result.append(working_node)
            # We want to keep turning as left as possible, so
            # consider each neighbor to find the largest CCW angle
            largest_angle = 0
            largest_angle_node = None
            for neighbor_node in working_node.neighbors:
                # We'll never double-back, so ignore this case
                if neighbor_node is last_node:
                    continue
                angle = math.degrees(ccw_angle(last_point, working_node.point, neighbor_node.point))
                if largest_angle_node is None or angle > largest_angle:
                    largest_angle = angle
                    largest_angle_node = neighbor_node
            # Check to see if we ended up in a situation where there were no useful
            # neighbors to traverse
            if largest_angle_node is None:
                raise Exception("Graph is not enclosed")
            last_point = working_node.point
            last_node = working_node
            working_node = largest_angle_node
        return result

    def get_exterior_segments(self):
        nodes = self.get_exterior_nodes()
        result = []
        for i in range(0, len(nodes)):
            next_i = (i + 1) % len(nodes)
            result.append(Segment2D(nodes[i].point, nodes[next_i].point))
        return result


class Node:

    def __init__(self, point: Point2D):
        self.point = point
        self.neighbors = []

    def add_neighbor_if_necessary(self, new_node):
        # Sanity check
        if new_node is self:
            raise Exception("It is not possible to make a node a neighbor of itself")
        if new_node not in self.neighbors:
            self.neighbors.append(new_node)


