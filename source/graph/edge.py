"""
Graph primiteves: Edge
"""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from graph.vertex import Vertex


class Edge:
    """
    Graph Edge
    """
    edge_id: str = None
    value: any = None
    start: Vertex = None
    end: Vertex = None

    def __init__(
            self,
            e_id: str,
            value: any,
            start: Vertex,
            end: Vertex):
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
