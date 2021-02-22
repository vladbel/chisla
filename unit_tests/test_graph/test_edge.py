"""Module docstring"""
import unittest


# module under test
import graph.primitives as p

class TestEdge(unittest.TestCase):
    """
    Unit tests for graph.Edge
    """

    def test_edge_instantiation(self):
        """--- shall create valid edge instance ---"""
        vertex_start = p.Vertex("start_vertex_id", "start_vertex_value")
        vertex_end = p.Vertex("end_vertex_id", "end_vertex_value")

        edge = p.Edge("edge_id","edge_value",vertex_start, vertex_end)

        self.assertTrue(edge.start.vertex_id == "start_vertex_id")


if __name__ == '__main__':
    unittest.main()
