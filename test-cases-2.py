import math
import unittest
from sympy import Polygon, pi, Point2D, Segment2D, Line2D
import utils


class TestGraph(unittest.TestCase):

    def test_0(self):
        """ Testing the clockwise angle between three points """
        p0 = Point2D(0, 0)
        p1 = Point2D(0, 1)
        p2 = Point2D(1, 1)
        self.assertAlmostEqual(90, math.degrees(utils.ccw_angle(p0, p1, p2)), 2)

        p0 = Point2D(0, 0)
        p1 = Point2D(0, 1)
        p2 = Point2D(1, 2)
        self.assertAlmostEqual(135.0, math.degrees(utils.ccw_angle(p0, p1, p2)), 2)

        p0 = Point2D(0, 0)
        p1 = Point2D(0, 1)
        p2 = Point2D(1, 0)
        self.assertAlmostEqual(45, math.degrees(utils.ccw_angle(p0, p1, p2)), 2)

        p0 = Point2D(0, 0)
        p1 = Point2D(0, 1)
        p2 = Point2D(0, 2)
        self.assertAlmostEqual(180.0, math.degrees(utils.ccw_angle(p0, p1, p2)), 2)

        p0 = Point2D(0, 0)
        p1 = Point2D(0, 1)
        p2 = Point2D(-1, 1)
        self.assertAlmostEqual(270.0, math.degrees(utils.ccw_angle(p0, p1, p2)), 2)

        p0 = Point2D(0, 0)
        p1 = Point2D(0, 1)
        p2 = Point2D(1, 1)
        self.assertAlmostEqual(90.0, math.degrees(utils.ccw_angle(p0, p1, p2)), 2)


    def test_1(self):

        graph = utils.Graph()

        print("Adding new line #1")
        graph.add_segment(Segment2D(Point2D(0, 0), Point2D(3, 3)))
        # Make sure the neighbor relationships are right
        node_0 = graph.get_node_at_point(Point2D(0, 0))
        self.assertEqual(1, len(node_0.neighbors))

        print("Adding new line #2")
        graph.add_segment(Segment2D(Point2D(0, 0), Point2D(3, 4)))
        # Make sure the neighbor relationships are right
        node_0 = graph.get_node_at_point(Point2D(0, 0))
        self.assertEqual(2, len(node_0.neighbors))

        print("Adding new line #3 (intersection)")
        graph.add_segment(Segment2D(Point2D(0, 2), Point2D(2, 0)))
        # Make sure the neighbor relationships are right.  The intersection
        # point has neighbors in all 4 directions now
        node_0 = graph.get_node_at_point(Point2D(1, 1))
        self.assertEqual(4, len(node_0.neighbors))

        # Show nodes
        print("Node Points:", [n.point for n in graph.nodes])

        print("Adding new line #4 (extension of existing edge)")
        graph.add_segment(Segment2D(Point2D(0, 0), Point2D(4, 4)))
        # In this situation we should only be adding one node
        self.assertEqual(8, graph.get_node_count())
        # Make sure the neighbor relationships are right
        node_0 = graph.get_node_at_point(Point2D(3, 3))
        node_1 = graph.get_node_at_point(Point2D(4, 4))
        self.assertEqual(2, len(node_0.neighbors))
        self.assertEqual(1, len(node_1.neighbors))

    def test_2(self):

        print("test_2")
        graph = utils.Graph()

        # Make two overlapping polygons
        p0 = Polygon((0, 0), (0, 2), (2, 2), (2, 0))
        graph.add_polygon(p0)
        p1 = Polygon((1, 1), (1, 3), (3, 3), (3, 1))
        graph.add_polygon(p1)
        # Show nodes
        print("Node points:", [n.point for n in graph.nodes])
        ext_nodes = graph.get_exterior_nodes()
        print("Exterior points:", [n.point for n in ext_nodes])
        self.assertEqual(8, len(ext_nodes))
        print("Exterior segments:", graph.get_exterior_segments())


if __name__ == '__main__':
    unittest.main()