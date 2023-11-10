from queue import Queue
from graph.graphBase import GameVertex
from graph.graphBase import Vertex
from graph.graphBase import Graph
from graph.graphBase import Feasible
from typing import List


class SearchAlgorithm:
    def __init__(self, graph: Graph, feasible: Feasible):
        self.graph = graph
        self.vertex = None
        self.feasible = feasible
        self.gen = None

    def breadFirstGenerator(self):
        frontier = Queue()
        reached = set()
        comeFrom = dict()
        frontier.put(self.vertex)
        reached.add(self.vertex)
        comeFrom[self.vertex] = None
        while not frontier.empty():
            currentVertex = frontier.get()
            if self.feasible.isEnd(currentVertex):
                return currentVertex, comeFrom
            for neighbour in self.graph.get_neighbours(currentVertex):
                if neighbour not in reached and self.feasible.isFeasible(currentVertex):
                    frontier.put(neighbour)
                    reached.add(neighbour)
                    comeFrom[neighbour] = currentVertex
            yield currentVertex, comeFrom

    def iniGenerator(self, vertex):
        self.setRoot(vertex)
        self.gen = self.breadFirstGenerator()

    def next(self):
        return next(self.gen)

    def setRoot(self, vertex):
        self.vertex = vertex

    def setGraph(self, graph):
        self.graph = graph

    def setFeasible(self, feasible):
        self.feasible = feasible


def breadthFirstSearchGenerator(graph: Graph, vertex: Vertex, feasible: Feasible) -> tuple[GameVertex, dict]:
    frontier = Queue()
    reached = set()
    comeFrom = dict()
    frontier.put(vertex)
    reached.add(vertex)
    comeFrom[vertex] = None
    while not frontier.empty():
        currentVertex = frontier.get()
        if feasible.isEnd(currentVertex):
            return currentVertex, comeFrom
        for neighbour in graph.get_neighbours(currentVertex):
            if neighbour not in reached and feasible.isFeasible(currentVertex):
                frontier.put(neighbour)
                reached.add(neighbour)
                comeFrom[neighbour] = currentVertex
        yield currentVertex, comeFrom


def breadthFirstSearch(graph: Graph, vertex: Vertex) -> dict[Vertex, Vertex]:
    frontier = Queue()
    reached = set()
    comeFrom = dict()
    frontier.put(vertex)
    while not frontier.empty():
        currentNode = frontier.get()
        reached.add(currentNode)
        for neighbour in graph.get_neighbours(currentNode):
            if neighbour not in reached:
                frontier.put(neighbour)
                comeFrom[neighbour] = currentNode
    return comeFrom


def getPath(comeFrom: dict, targetVertex: Vertex) -> List[Vertex]:
    childVertex: Vertex = targetVertex
    res: List[Vertex] = list()
    res.append(childVertex)
    while comeFrom.get(childVertex) is not None:
        res.append(comeFrom[childVertex])
        childVertex = comeFrom[childVertex]
    res.reverse()
    return res
