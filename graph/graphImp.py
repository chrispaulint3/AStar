from abc import ABC
from typing import List
from graph.graphBase import Graph, Feasible
from graph.graphBase import Vertex
from graph.graphBase import GraphType


class AdjList(Graph, ABC):
    def __init__(self):
        super().__init__()
        self.adjList: dict[Vertex, List[Vertex]] = dict()

    def add_vertex(self, ver: Vertex):
        if ver in self.adjList:
            raise Exception("vertex already in adjList")
            return
        self.adjList[ver] = []

    def add_edge(self, ver1: Vertex, ver2: Vertex):
        if ver1 in self.adjList and ver2 in self.adjList:
            if not self.is_edge_exist(ver1, ver2):
                self.adjList[ver1].append(ver2)

            if not self.is_edge_exist(ver2, ver1):
                self.adjList[ver2].append(ver1)
        else:
            raise Exception("vertex not in adjacent list")

    def is_edge_exist(self, startVer: Vertex, targetVer: Vertex) -> bool:
        if startVer not in self.adjList:
            return False
        elif targetVer not in self.adjList[startVer]:
            return False
        else:
            return True

    def get_neighbours(self, root_vertex: Vertex):
        return self.adjList[root_vertex]


class graphFactory:
    @staticmethod
    def get_graph(type: GraphType) -> Graph:
        if type == type.AdjList:
            return AdjList()


class GameFeasible(Feasible):
    def __init__(self):
        super().__init__()
        self.barrier: set[Vertex] = set()
        self.goal = None

    def addBarrier(self, barrier):
        self.barrier.add(barrier)

    def addGoal(self, goal: Vertex):
        self.goal = goal

    def isFeasible(self, vertex: Vertex) -> bool:
        print("判断了")
        if vertex in self.barrier:
            return False
        else:
            return True

    def isEnd(self, vertex):
        if self.goal == vertex:
            return True
        else:
            return False


if __name__ == "__main__":
    mat = AdjList()
    ver1 = Vertex((300, 100))
    ver2 = Vertex((200, 250))
    ver3 = Vertex((400, 250))
    ver4 = Vertex((700, 700))
    mat.add_vertex(ver1)
    mat.add_vertex(ver2)
    mat.add_vertex(ver3)
    # mat.add_vertex(ver4)
    mat.add_edge(ver1, ver2)
    mat.add_edge(ver1, ver3)
    mat.add_edge(ver2, ver4)
    # path = breadthFirstSearch(mat, ver1)
    # res = []
    # for step in path:
    #     res.append()
