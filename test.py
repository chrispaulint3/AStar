import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Graph in Pygame")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 定义图的数据结构
# 假设我们的图有三个节点，每个节点有一个位置和它连接的其他节点
nodes = {
    "A": {"pos": (100, 100), "edges": ["B", "C"]},
    "B": {"pos": (400, 400), "edges": ["A", "C"]},
    "C": {"pos": (700, 100), "edges": ["A", "B"]},
}


def draw_graph():
    # 绘制边
    for node, attributes in nodes.items():
        for edge in attributes["edges"]:
            pygame.draw.line(screen, BLACK, attributes["pos"], nodes[edge]["pos"], 2)

    # 绘制节点
    for node, attributes in nodes.items():
        pygame.draw.circle(screen, RED, attributes["pos"], 20)
        label = pygame.font.SysFont("Arial", 20).render(node, True, WHITE)
        screen.blit(label, (attributes["pos"][0] - 10, attributes["pos"][1] - 10))


# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_graph()

    pygame.display.flip()

pygame.quit()
sys.exit()