"""
Graph primiteves
"""


class Edge:
    """
    Graph Edge
    """
    edge_id: str = None
    value: any = None
    start = None
    end = None

    def __init__(
            self,
            e_id: str,
            value: any,
            start,
            end):
        """
        Init edge
        """
        self.edge_id = e_id
        self.value = value
        self.start = start
        self.end = end

    def is_valid(self):
        """
        Edge shall have valid end and start
        """
        return self.start is not None and self.end is not None


class Vertex:
    """
    Graph vertex  base
    """

    vertex_id: str = None
    value: any = None
    edges: list[Edge] = None

    def __init__(self,
                 v_id: str,
                 value: any):
        """
        Init transac
        """
        self.vertex_id = v_id
        self.value = value
        self.vertex_id = v_id

    def add_edge(self,
                 edge: Edge):
        """
        Append edge to vertex
        """
        edge.start = self
        self.edges.append(edge)
