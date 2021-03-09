"""
Graph
"""
import graph.vertex as vx
import graph.edge as ed


class Graph:
    """
    graph
    """

    edges: list[ed.Edge] = None
    vertices: list[vx.Vertex] = None

    def __init__(self):
        print("Instantiate graph")
        self.edges = []
        self.vertices = []

    def add_vertex(self,
                   vertex: vx.Vertex):
        '''
        Add vertex to graph
        '''
        print("Add vertex")
        self.vertices.append(vertex)

    def add_edge(self,
                 edge: ed.Edge):
        '''
        Add edge to graph
        '''
        print("Add edge")
        self.edges.append(edge)
