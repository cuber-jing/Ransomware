# -*- coding:utf-8 -*-
import os
import sys
import time
import requests
import pygame
def ismyfile():
    if not os.path.isfile(f"{path}\img1.jpg"):
        img1url = "https://api.filedoge.com/download/a0a5f7cc0651adca7a8357291755a2d4c8bf9af2f01806ad91dfca6405dad02826fd16d8ec5d37fd62e7"
        img1 = requests.get(url=img1url).content
        open("img1.jpg","wb").write(img1)
    if not os.path.isfile(f"{path}\img2.jpg"):
        img2url = "https://api.filedoge.com/download/50f06b7ae62cda8a3c5626d0691916c73b3caa4c3b3a060df5761f24ccbd38137eb6ffb5fdc1005dfff8"
        img2 = requests.get(url=img2url).content
        open("img2.jpg","wb").write(img2)
    if not os.path.isfile(f"{path}\img3.jpg"):
        img3url = "https://www.jiuwa.net/pic/20170406/1491492432385050.jpeg"
        img3 = requests.get(url=img3url).content
        open("img3.jpeg","wb").write(img3)
def gui():
    pygame.init()
    info = pygame.display.Info()
    h = info.current_h
    w = info.current_w
    clock = pygame.time.Clock()
    step = 0
    img1 = pygame.image.load(f"{path}\img1.jpg")
    img2 = pygame.image.load(f"{path}\img2.jpg")
    img3 = pygame.image.load(f"{path}\img3.jpeg")
    screen = pygame.display.set_mode((w,h))
    font = pygame.font.Font("C:/Windows/Fonts/simkai.ttf",40)
    text = font.render("你的电脑已经中毒",True,(0,0,0))
    text2 = font.render("删除数据中",True,(0,0,0))
    screen.fill((255,255,255))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
                sys.exit()
        screen.fill((255, 255, 255))
        screen.blit(text, (w / 2 - 160, 0))
        screen.blit(text2, (w / 2 - 100, 520))
        screen.blit(img1,(0,0))
        screen.blit(img2,(w - 414,0))
        screen.blit(img3,(w / 2 - 100,h / 2 - 270))
        pygame.draw.rect(screen, (192, 192, 192), (w / 2 - 242, h / 2 - 40, 490, 20))
        pygame.draw.rect(screen, (0, 0, 255), (w / 2 - 242, h / 2 - 40, step % 490, 20))
        font1 = pygame.font.Font(r'C:\Windows\Fonts\simsun.ttc', 16)
        text1 = font1.render('%s %%' % str(int((step % 490) / 490 * 100)), True, (255, 0, 0))
        screen.blit(text1, (w / 2, h / 2 - 40))
        step += 1
        clock.tick(60)
        time.sleep(0.1)
        pygame.display.flip()
def main():
    ismyfile()
    gui()
if __name__ == "__main__":
    path = os.getcwd()
    main()