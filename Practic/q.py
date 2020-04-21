import pygame
pygame.init()
hero_Rect = pygame.Rect(100, 500, 480, 700)
print("位置坐标x%d-y%d；大小%d-%d" % (hero_Rect.x, hero_Rect.y, hero_Rect.width, hero_Rect.height))
# 用方法创建一个矩形对象，注意rectangle必须R大写
screen = pygame.display.set_mode((480, 700))
while True:
    pass