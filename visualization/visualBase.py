import enum
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
from pygame import Rect
from pygame.font import Font
from graph.graphBase import Vertex
from algorithm.graphSearch import getPath


class GameState(enum.Enum):
    READY = 1
    START = 2
    FIND = 3


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
        self.startVertex = None
        self.goal: tuple[int, int] = goal
        self.goalCache = None
        self.pathTarget = None
        self.comeFrom: dict[Vertex, Vertex] = None
        self.currentVertex = None

    def updateBarrier(self, barrier: tuple[int, int]):
        self.barrier = barrier

    def updateGoal(self, goal: tuple[int, int]):
        self.goalCache = self.goal
        self.goal = goal

    def updateStart(self, start: tuple[int, int]):
        self.startVertex = start

    def updatePathTarget(self, pathTarget: dict[Vertex, Vertex]):
        self.pathTarget = pathTarget

    def updateComeFrom(self, comeFrom: dict[Vertex, Vertex]):
        self.comeFrom = comeFrom

    def updateCurrentVertex(self, currentVertex: Vertex):
        self.currentVertex = currentVertex


class GameSurface:
    def __init__(self, surfaceSize: tuple[int, int], graph: GraphCreator, nodeRadius: float = 8):
        self.surface = Surface(surfaceSize)
        self.graph = graph
        self.nodeRadius = nodeRadius
        self.barrier_cache = []
        self.goal = None
        self.initSurface()

    def initSurface(self):
        self.surface.fill(WHITE)
        for row in self.graph.mat:
            for vert in row:
                draw.circle(self.surface, RED, vert.val, self.nodeRadius, width=1)

    def update(self, userInterface: UserInterface = None):
        if userInterface.currentVertex is not None:
            draw.circle(self.surface, RED, userInterface.currentVertex.val, 8)
        if userInterface.barrier is not None:
            x, y = self.graph.mat[userInterface.barrier[1]][userInterface.barrier[0]].val
            draw.circle(self.surface, BLACK, (x, y), 8)
        if userInterface.goal is not None:
            # clear the previous goal point
            if userInterface.goalCache is not None:
                x, y = self.graph.mat[userInterface.goalCache[1]][userInterface.goalCache[0]].val
                left = x - self.nodeRadius
                top = y - self.nodeRadius
                rect = Rect(left, top, 2 * self.nodeRadius, 2 * self.nodeRadius)
                self.surface.fill(WHITE, rect)
                draw.circle(self.surface, RED, (x, y), 8, width=1)
            # draw the new goal
            x, y = self.graph.mat[userInterface.goal[1]][userInterface.goal[0]].val
            draw.circle(self.surface, GREEN, (x, y), 8)

        if userInterface.pathTarget is not None:
            targetNode = self.graph.mat[userInterface.pathTarget[1]][userInterface.pathTarget[0]]
            if targetNode == self.graph.getRoot():
                return
            path2Target: List[Vertex] = getPath(userInterface.comeFrom, targetNode)
            print(path2Target)
            pathLen = len(path2Target)
            for ind in range(pathLen - 1):
                draw.line(self.surface, BLACK, path2Target[ind].val, path2Target[ind + 1].val, width=5)


class NormalSurface:
    def __init__(self, surfaceSize: tuple[int, int]):
        self.surface = Surface(surfaceSize)
        self.font = Font('./MotionPicture_PersonalUseOnly.ttf', 30)
        self.message = ["keyboard usage", "g: set goal", "s: set start point", "c: reset",
                        "mouse right button: add barrier"
            , "mouse left button: show path"]
        self.gameMessage = []
        self.initSurface()

    def initSurface(self):
        self.surface.fill(WHITE)
        for ind, msg in enumerate(self.message):
            text = self.font.render(msg, True, BLACK)
            self.surface.blit(text, (0, ind * 30))

    def updateGameMessage(self):
        pass
