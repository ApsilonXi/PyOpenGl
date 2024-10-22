import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Определяем вершины и рёбра человека
def draw_sphere(radius, slices, stacks):
    # Создание сферы для головы
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    glColor3f(1.0, 0.6, 0.0)  # Оранжевый цвет
    gluSphere(quadric, radius, slices, stacks)

def draw_cylinder(radius, height, slices):
    # Создание цилиндра для тела и ног
    glBegin(GL_QUAD_STRIP)
    for i in range(0, slices + 1):
        theta = 2 * np.pi * i / slices
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        glVertex3f(x, y, 0)  # Нижняя вершина
        glVertex3f(x, y, height)  # Верхняя вершина
    glEnd()

def draw_marsianin():
    # Рисуем голову
    glPushMatrix()
    glTranslatef(0, 0.8, 1.8)  # Поднимаем голову
    draw_sphere(0.4, 20, 20)
    glPopMatrix()

    # Рисуем тело
    glPushMatrix()
    glTranslatef(0, 0.5, 1)  # Устанавливаем тело ниже головы
    draw_cylinder(0.15, 0.8, 20)
    glPopMatrix()

    # Рисуем ноги
    for x in [-0.1, 0.1]:  # Две ноги
        glPushMatrix()
        glTranslatef(x, 0.6, 0)  # Расставляем ноги
        draw_cylinder(0.05, 2.4, 10)
        glPopMatrix()

    # Рисуем руки
    for x in [-0.2, 0.2]:  
        glPushMatrix()
        glTranslatef(x, 0.4, 1) 
        draw_cylinder(0.05, 0.5, 10)
        glPopMatrix()

def main():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    rot = [0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 1, 0, 0) 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_marsianin()
        pygame.display.flip()
        pygame.time.wait(10)

main()