import sys
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

# Функция для рисования ёлки
def draw_tree():
    width = 1.0  
    height = 0.5      

    '''glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  # Зелёный цвет
    glVertex3f(0.0, height, 0.0)  # Верхушка
    glVertex3f(-width / 2, 0.0, 0.0)  # Левый угол
    glVertex3f(width / 2, 0.0, 0.0)   # Правый угол
    glEnd()'''

    '''glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  
    glVertex3f(0.0, height * 2, 0.0)  
    glVertex3f(-width / 2, height, 0.0) 
    glVertex3f(width / 2, height, 0.0)   
    glEnd()


    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  
    glVertex3f(0.0, height * 3, 0.0) 
    glVertex3f(-width / 2, height * 2, 0.0) 
    glVertex3f(width / 2, height * 2, 0.0)   
    glEnd()'''

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  # Зелёный цвет
    glVertex3f(0.0, height, 0.0)  # Верхушка
    glVertex3f(-width / 2, 0.0, 0.0)  # Левый угол
    glVertex3f(width / 2, 0.0, 0.0)   # Правый угол
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  # Зелёный цвет
    glVertex3f(0.0, height * 2, 0.0)  # Верхушка
    glVertex3f(-width / 2 * 0.8, height, 0.0)  # Левый угол
    glVertex3f(width / 2 * 0.8, height, 0.0)   # Правый угол
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  # Зелёный цвет
    glVertex3f(0.0, height * 3, 0.0)  # Верхушка
    glVertex3f(-width / 2 * 0.6, height * 2, 0.0)  # Левый угол
    glVertex3f(width / 2 * 0.6, height * 2, 0.0)   # Правый угол
    glEnd()

def draw_trunk():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.25, 0.1)  # Коричневый цвет
    glVertex3f(-0.1, 0.0, 0.0)  # Левый нижний угол
    glVertex3f(0.1, 0.0, 0.0)   # Правый нижний угол
    glVertex3f(0.1, -0.4, 0.0)  # Правый верхний угол
    glVertex3f(-0.1, -0.4, 0.0) # Левый верхний угол
    glEnd()

if __name__ == "__main__":
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Рисуем ёлку и пень
        draw_tree()
        draw_trunk()

        pygame.display.flip()
        pygame.time.wait(10)