from abc import abstractmethod, ABC
from abc import ABC
from typing import List
from pygame import init
from pygame.display import set_mode
from pygame.display import set_caption
from pygame.time import Clock
from visualization.conf import *
from graph.graphCreator import createGraphVertex
from graph.graphCreator import GraphCreator
from graph.graphBase import GraphType
from pygame import Surface
from pygame import draw
from visualization.conf import WHITE


class GameBase:
    def __init__(self):
        init()
        set_caption(GAME_CAPTION)
        self._screen = set_mode(RESOLUTION)
        self._running = True
        self._clock = Clock()
        self._fps = FPS

    def set_running_flag(self, flag: bool):
        self._running = flag

    @abstractmethod
    def processInput(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def run(self):
        pass


class UserInterface:
    def __init__(self, goal: tuple[int, int] = None):
        self.barrier: tuple[int, int] = None
        self.goal: tuple[int, int] = goal

    def updateBarrier(self, barrier: tuple[int, int]):
        self.barrier = barrier

    def updateGoal(self, goal: tuple[int, int]):
        self.goal = goal


class GameSurface:
    def __init__(self, surfaceSize: tuple[float, float], graph: GraphCreator):
        self.surface = Surface(surfaceSize)
        self.graph = graph
        self.initSurface()

    def initSurface(self):
        self.surface.fill(WHITE)
        for row in self.graph.mat:
            for vert in row:
                draw.circle(self.surface, RED, vert.val, 8, width=1)

    def update(self, userInterface: UserInterface = None):
        # if userInterface.barrier is not None
        #     x, y = self.graph.mat[command[1]][command[0]].val
        #     draw.circle(self.surface, BLACK, (x, y), 8)
        pass
