from typing import List
from graph.graphBase import Vertex
from graph.graphBase import Graph


def findMouseNode(mouse_pos: tuple[int, int], padding: int) -> tuple[int, int]:
    nodeIndexX = mouse_pos[0] // padding
    nodeIndexY = mouse_pos[1] // padding
    return nodeIndexX, nodeIndexY
