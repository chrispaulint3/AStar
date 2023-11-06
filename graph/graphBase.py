from abc import ABC
from abc import abstractmethod
from enum import Enum


class VertexType(Enum):
    normal = 1
    barrier = 2
    goal = 3


class GraphType(Enum):
    AdjList = 1
    AdjMat = 2


class Vertex:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class GameVertex(Vertex):
    def __init__(self, val, vertexType=VertexType.normal):
        super(GameVertex, self).__init__(val)
        self.type = vertexType


class Graph:
    def __init__(self):
        pass

    @abstractmethod
    def add_vertex(self, ver: Vertex):
        pass

    @abstractmethod
    def delete_vertex(self):
        pass

    @abstractmethod
    def add_edge(self, ver1: Vertex, ver2: Vertex):
        pass

    @abstractmethod
    def delete_edge(self):
        pass

    @abstractmethod
    def get_neighbours(self, root_vertex: Vertex):
        pass

    @abstractmethod
    def is_edge_exist(self, startVer: Vertex, targetVer: Vertex) -> bool:
        pass
