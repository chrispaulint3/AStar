import pygame
#
# # 初始化pygame
# pygame.init()
#
# # 设置屏幕大小
# screen = pygame.display.set_mode((640, 480))
#
# # 设置基本参数
# done = False
# text = ''
# font = pygame.font.Font(None, 50)
# input_active = False
# color_inactive = pygame.Color('lightskyblue3')
# color_active = pygame.Color('dodgerblue2')
# input_box_color = color_inactive
# input_box = pygame.Rect(100, 100, 140, 50)
#
# # 游戏主循环
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # 如果用户点击了输入框
#             if input_box.collidepoint(event.pos):
#                 # 切换活动状态
#                 input_active = not input_active
#             else:
#                 input_active = False
#             # 根据活动状态更改输入框的颜色
#             input_box_color = color_active if input_active else color_inactive
#         if event.type == pygame.KEYDOWN:
#             if input_active:
#                 if event.key == pygame.K_RETURN:
#                     print(text)
#                     text = ''  # Enter后清空文本
#                 elif event.key == pygame.K_BACKSPACE:
#                     text = text[:-1]  # 删除最后一个字符
#                 else:
#                     text += event.unicode  # 添加输入的字符
#
#     # 填充背景
#     screen.fill((30, 30, 30))
#
#     # 渲染文字
#     txt_surface = font.render(text, True, (255, 255, 255))
#     # 调整输入框的宽度
#     input_box.w = max(100, txt_surface.get_width() + 10)
#
#     # 绘制输入框和文字
#     screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
#     pygame.draw.rect(screen, input_box_color, input_box, 2)
#
#     # 刷新屏幕
#     pygame.display.flip()
#
# # 结束pygame
# pygame.quit()


