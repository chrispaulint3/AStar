import pygame
from visualization.visualBase import GameBase
from graph.graphImp import AdjList
from visualization.conf import *
from graph.graphBase import Vertex
from algorithm.graphSearch import breadthFirstSearchGenerator


class Visual(GameBase):
    def __init__(self):
        super().__init__()
        self.mat = AdjList()
        self.rootVertex = self.initGraph()
        self.gen = breadthFirstSearchGenerator(self.mat, self.rootVertex)
        self.surface = pygame.Surface(RESOLUTION)
        self.surface.fill(WHITE)

    def initGraph(self):
        ver1 = Vertex((300, 100))
        ver2 = Vertex((200, 250))
        ver3 = Vertex((400, 250))
        ver4 = Vertex((200, 400))
        self.mat.add_vertex(ver1)
        self.mat.add_vertex(ver2)
        self.mat.add_vertex(ver3)
        self.mat.add_vertex(ver4)
        self.mat.add_edge(ver1, ver2)
        self.mat.add_edge(ver1, ver3)
        self.mat.add_edge(ver2, ver4)
        return ver1

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        print("按下")
                        currentNode = next(self.gen)
                        pygame.draw.circle(self.surface, RED, currentNode.val, 20)
                        for neighbour in self.mat.get_neighbours(currentNode):
                            pygame.draw.line(self.surface, BLACK, currentNode.val, neighbour.val)
                    except StopIteration:
                        pass



    def update(self):
        pass

    def render(self):
        self._screen.blit(self.surface, (0, 0))
        pygame.display.update()
        self._clock.tick(FPS)

    def run(self):
        while self._running:
            self.processInput()
            self.update()
            self.render()


if __name__ == "__main__":
    game = Visual()
    game.run()
    pygame.quit()
