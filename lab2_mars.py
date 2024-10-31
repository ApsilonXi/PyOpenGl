import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

rotation_angles = [0, 0, 0, 0, 0]
camera_angle_x = 0
camera_angle_y = 0
camera_distance = 1
mouse_pressed = False

def update_rotation():
    global rotation_angles
    rotation_speeds = [5, -1, 1.5, -2, 10]
    for i in range(len(rotation_angles)):
        rotation_angles[i] += rotation_speeds[i]
        rotation_angles[i] %= 360  

def handle_mouse_motion(x, y):
    global camera_angle_x, camera_angle_y, last_mouse_x, last_mouse_y
    if mouse_pressed:  
        dx = x - last_mouse_x
        dy = y - last_mouse_y
        camera_angle_x += dx * 0.2  
        camera_angle_y += dy * 0.2
    last_mouse_x = x
    last_mouse_y = y

def handle_mouse_button(button, pressed):
    global mouse_pressed
    if button == 1:
        mouse_pressed = pressed

def apply_camera():
    glLoadIdentity()
    eye_x = camera_distance * math.sin(math.radians(camera_angle_x)) * math.cos(math.radians(camera_angle_y))
    eye_y = camera_distance * math.sin(math.radians(camera_angle_y))
    eye_z = camera_distance * math.cos(math.radians(camera_angle_x)) * math.cos(math.radians(camera_angle_y))

    gluLookAt(eye_x, eye_y, eye_z, 0, 0, 0, 0, 1, 0)

def draw_glaza(radius, slices, stacks):
    # Создание сферы для головы
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    glColor3f(0.0, 0.6, 0.0)  # Оранжевый цвет
    gluSphere(quadric, radius, slices, stacks)

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

    #рисуем глаза
    for x in [-0.1, 0.1]:
        glPushMatrix()
        glTranslatef(x, 0.8, 1.8)  
        draw_glaza(0.05, 20, 20)
        glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    apply_camera() 
    draw_marsianin()
    pygame.display.flip()

def main():
    global last_mouse_x, last_mouse_y

    pygame.init()
    screen = pygame.display.set_mode((1000, 1000), DOUBLEBUF | OPENGL)
    glClearColor(0.1, 0.1, 0.1, 1)

    clock = pygame.time.Clock()
    running = True
    last_mouse_x, last_mouse_y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(True)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEMOTION:
                handle_mouse_motion(*event.pos)
            if event.type == MOUSEBUTTONDOWN:
                handle_mouse_button(event.button, True)
            if event.type == MOUSEBUTTONUP:
                handle_mouse_button(event.button, False)

        update_rotation() 
        display()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()