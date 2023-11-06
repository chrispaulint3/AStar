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
from graph.graphBase import VertexType

import pygame


class Visual(GameBase, ABC):
    def __init__(self, graphCreator: GraphCreator):
        super(Visual, self).__init__()
        self.graphCreator = graphCreator
        self.gameSurface = GameSurface(RESOLUTION, self.graphCreator)
        self.userInterface = UserInterface()

        self.gen = breadthFirstSearchGenerator(self.graphCreator.graph, self.graphCreator.getRoot())

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        currentNode = next(self.gen)
                        pygame.draw.circle(self.gameSurface.surface, RED, currentNode.val, 8)
                        for neighbour in self.graphCreator.graph.get_neighbours(currentNode):
                            pygame.draw.line(self.gameSurface.surface, BLACK, currentNode.val, neighbour.val)
                    except StopIteration:
                        pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # process mouse input
                    mousePos = pygame.mouse.get_pos()
                    x, y = findMouseNode(mousePos, 20)
                    print(x,y)
                    self.userInterface.updateBarrier((x, y))

    def update(self):
        self.graphCreator.updateVertexState(self.userInterface.barrier,VertexType.barrier)
        self.gameSurface.update(self.userInterface.barrier)
        pass

    def render(self):
        self._screen.blit(self.gameSurface.surface, (0, 0))
        pygame.display.update()
        self._clock.tick(FPS)

    def run(self):
        while self._running:
            self.processInput()
            self.update()
            self.render()


if __name__ == "__main__":
    graphCreator = GridGraphCreator([15, 15])
    graphCreator.createGraph(GraphType.AdjList)
    game = Visual(graphCreator)
    game.run()
    pygame.quit()
