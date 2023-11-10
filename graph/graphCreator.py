from abc import ABC
from abc import abstractmethod
from typing import List
from graph.graphBase import Vertex
from graph.graphBase import Graph
from graph.graphBase import VertexType
from graph.graphBase import GameVertex
from graph.graphImp import graphFactory
from graph.graphImp import GraphType
from algorithm.graphSearch import breadthFirstSearchGenerator


def createGraphVertex(width: int = 800, height: int = 600, padding: int = 20):
    # map the position to Vertex
    vertexMat: List[List[GameVertex]] = []

    # create the map Node
    for i in range(padding, height, padding):
        vertexRow: List[GameVertex] = []
        for j in range(padding, width, padding):
            currentVertex = GameVertex((j, i))
            vertexRow.append(currentVertex)
        vertexMat.append(vertexRow)
    return vertexMat


def createGraphEdge(graphType: GraphType, vertexMat: List[List[GameVertex]]) -> Graph:
    graph = graphFactory.get_graph(graphType)
    for row in vertexMat:
        for vert in row:
            graph.add_vertex(vert)
    vertexMatHeight: int = len(vertexMat)
    vertexMatWidth: int = len(vertexMat[0])
    for i in range(vertexMatHeight):
        for j in range(vertexMatWidth):
            currentVertex = vertexMat[i][j]
            if i - 1 >= 0:
                neighbourVertex = vertexMat[i - 1][j]
                graph.add_edge(currentVertex, neighbourVertex)
            if i + 1 < vertexMatHeight:
                neighbourVertex = vertexMat[i + 1][j]
                graph.add_edge(currentVertex, neighbourVertex)
            if j - 1 >= 0:
                neighbourVertex = vertexMat[i][j - 1]
                graph.add_edge(currentVertex, neighbourVertex)
            if j + 1 < vertexMatWidth:
                neighbourVertex = vertexMat[i][j + 1]
                graph.add_edge(currentVertex, neighbourVertex)

    return graph


class GraphCreator(ABC):
    def __init__(self):
        self.mat: List[List[Vertex]] = None
        self.graph: Graph = None
        self.rootPos: List[int] = None

    @abstractmethod
    def createGraph(self, graphType: GraphType):
        pass

    @abstractmethod
    def setRoot(self, rootPos):
        pass

    @abstractmethod
    def getRoot(self):
        pass

    @abstractmethod
    def getVertexByInd(self, y, x):
        pass


class GridGraphCreator(GraphCreator):
    def __init__(self):
        super().__init__()

    def createGraph(self, graphType: GraphType):
        self.mat = createGraphVertex()
        self.graph = createGraphEdge(graphType, self.mat)

    def setRoot(self, rootPos):
        self.rootPos = rootPos

    def getRoot(self):
        if self.rootPos is None:
            return
        return self.getVertexByInd(self.rootPos[1], self.rootPos[0])

    def getVertexByInd(self, y, x):
        return self.mat[y][x]
