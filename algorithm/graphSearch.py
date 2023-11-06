from queue import Queue
from graph.graphBase import Vertex
from graph.graphBase import Graph


def breadthFirstSearchGenerator(graph: Graph, vertex: Vertex) -> Vertex:
    frontier = Queue()
    reached = set()
    frontier.put(vertex)
    reached.add(vertex)
    while not frontier.empty():
        currentNode = frontier.get()
        for neighbour in graph.get_neighbours(currentNode):
            if neighbour not in reached:
                frontier.put(neighbour)
                reached.add(neighbour)
        yield currentNode


def breadthFirstSearch(graph: Graph, vertex: Vertex) -> dict[Vertex,Vertex]:
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


