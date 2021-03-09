"""Graph unit tests"""
import unittest

# module under test
import graph.edge as ed
import graph.vertex as vx
import graph.graph as gr


class TestGraph(unittest.TestCase):
    """
    Unit tests for graph.graph
    """

    def test_graph_instantiation(self):
        """--- shall create valid graph instance ---"""
        graph = gr.Graph()
        self.assertTrue(graph.vertices is not None)
        self.assertTrue(graph.edges is not None)

    def test_graph_add_vertex(self):
        """--- shall add one vertex to empty graph ---"""
        graph = gr.Graph()
        vertex = vx.Vertex("vertex_id", "vertex_value")

        graph.add_vertex(vertex)

        self.assertTrue(graph.vertices is not None)
        self.assertTrue(len(graph.vertices) == 1)


if __name__ == '__main__':
    unittest.main()
