from abc import ABC
from typing import List
from visualBase import GameBase
from visualization.conf import *
from graph.graphCreator import createGraphVertex
from graph.graphBase import GraphType
from graph.graphBase import Graph
from graph.graphCreator import createGraphEdge
from algorithm.graphSearch import breadthFirstSearchGenerator
from visualization.utils import findMouseNode
from graph.graphCreator import GridGraphCreator
from graph.graphCreator import GraphCreator
from visualization.visualBase import GameSurface
from visualization.visualBase import UserInterface
from visualization.visualBase import NormalSurface
from graph.graphImp import GameFeasible
from graph.graphBase import Feasible
from graph.graphBase import VertexType
from algorithm.graphSearch import getPath
from algorithm.graphSearch import SearchAlgorithm
from visualization.visualBase import GameState
import pygame


class Visual(GameBase, ABC):
    def __init__(self, graphCreator: GraphCreator, searchAlgo: SearchAlgorithm):
        super(Visual, self).__init__()
        self.graphManager = graphCreator
        self.algo = searchAlgo
        self.algo.iniGenerator(self.graphManager.getVertexByInd(15, 15))

        self.gameSurface = GameSurface((800, 600), self.graphManager)
        self.helpSurface = NormalSurface((800, 200))
        self.userInterface = UserInterface()

        self.currentNode = None
        self.comeFrom = None

        self.gameState = GameState

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        currentNode, comeFrom = self.algo.next()
                        self.userInterface.updateComeFrom(comeFrom)
                        self.userInterface.updateCurrentVertex(currentNode)
                    except StopIteration as e:
                        if self.comeFrom is not None:
                            pass
                        else:
                            currentNode, comeFrom = e.value
                            self.currentNode = currentNode
                            self.comeFrom = comeFrom
                elif event.key == pygame.K_g:
                    mousePos = pygame.mouse.get_pos()
                    x, y = findMouseNode(mousePos, 20)
                    self.userInterface.updateGoal((x, y))
                elif event.key == pygame.K_s:
                    mousePos = pygame.mouse.get_pos()
                    x, y = findMouseNode(mousePos, 20)
                    self.userInterface.updateStart((x, y))
                    self.gameState = GameState.START
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    # process mouse input
                    mousePos = pygame.mouse.get_pos()
                    x, y = findMouseNode(mousePos, 20)
                    vertex = self.graphManager.getVertexByInd(y, x)
                    self.userInterface.updateBarrier((x, y))
                    self.algo.feasible.addBarrier(vertex)

                elif event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    x, y = findMouseNode(mousePos, 20)
                    self.userInterface.updatePathTarget((x, y))

    def update(self):
        self.gameSurface.update(self.userInterface)
        self.helpSurface.updateGameMessage(self.userInterface)

    def render(self):
        self._screen.blit(self.gameSurface.surface, (0, 0))
        self._screen.blit(self.helpSurface.surface, (0, 600))
        pygame.display.update()
        self._clock.tick(FPS)

    def run(self):
        while self._running:
            self.processInput()
            self.update()
            self.render()


def main():
    feasible = GameFeasible()
    graph = GridGraphCreator()
    graph.createGraph(GraphType.AdjList)
    algorithm = SearchAlgorithm(graph.graph, feasible)
    game = Visual(graph, algorithm)
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
