"""
Graph primiteves: Vertex
"""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from graph.edge import Edge


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
