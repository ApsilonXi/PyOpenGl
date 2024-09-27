import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Функция для рисования сферы
def draw_sphere(radius, slices, stacks):
    for i in range(stacks):
        lat0 = math.pi * (-0.5 + float(i) / stacks)  # углы широты
        z0 = radius * math.sin(lat0)  # координата Z
        r0 = radius * math.cos(lat0)  # радиус на широте
        lat1 = math.pi * (-0.5 + float(i + 1) / stacks)  # следующий угол широты
        z1 = radius * math.sin(lat1)
        r1 = radius * math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * float(j) / slices  # углы долготы
            x = math.cos(lng)  # координаты X
            y = math.sin(lng)

            glNormal3f(x * r0, y * r0, z0)  # нормали
            glVertex3f(x * r0, y * r0, z0)  # верхняя точка
            glNormal3f(x * r1, y * r1, z1)
            glVertex3f(x * r1, y * r1, z1)  # нижняя точка
        glEnd()

# Функция для рисования куба
def draw_cube(size):
    vertices = [
        [size, size, size],
        [size, size, -size],
        [size, -size, -size],
        [size, -size, size],
        [-size, size, size],
        [-size, size, -size],
        [-size, -size, -size],
        [-size, -size, size],
    ]
    
    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_martian(position):
    # Рисуем тело (сфера)
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    glColor3f(0.6, 0.2, 0.8)  # Фиолетовый цвет
    draw_sphere(1, 20, 20)  # Рисуем тело
    glPopMatrix()

    # Рисуем голову (сфера)
    glPushMatrix()
    glTranslatef(position[0], position[1] + 1.5, position[2])
    glColor3f(0.6, 0.2, 0.8)  # Фиолетовый цвет
    draw_sphere(0.8, 20, 20)  # Рисуем голову
    glPopMatrix()
    
    # Рисуем руки (цилиндры)
    arm_length = 1.0
    glColor3f(0.6, 0.2, 0.8)  # Фиолетовый цвет для рук
    
    # Левая рука
    glPushMatrix()
    glTranslatef(position[0] - 1, position[1] + 1, position[2])  # Положение левой руки
    glRotatef(90, 0, 1, 0)  # Поворачиваем руку
    gluCylinder(gluNewQuadric(), 0.2, 0.2, arm_length, 20, 20)  # Рисуем руку
    glPopMatrix()

    # Правая рука
    glPushMatrix()
    glTranslatef(position[0] + 1, position[1] + 1, position[2])  # Положение правой руки
    glRotatef(90, 0, 1, 0)  # Поворачиваем руку
    gluCylinder(gluNewQuadric(), 0.2, 0.2, arm_length, 20, 20)  # Рисуем руку
    glPopMatrix()

    # Рисуем ноги (цилиндры)
    leg_length = 1.0
    
    # Левая нога
    glPushMatrix()
    glTranslatef(position[0] - 0.5, position[1] - 1, position[2])  # Положение левой ноги
    glRotatef(90, 0, 1, 0)  # Поворачиваем ногу
    gluCylinder(gluNewQuadric(), 0.2, 0.2, leg_length, 20, 20)  # Рисуем ногу
    glPopMatrix()

    # Правая нога
    glPushMatrix()
    glTranslatef(position[0] + 0.5, position[1] - 1, position[2])  # Положение правой ноги
    glRotatef(90, 0, 1, 0)  # Поворачиваем ногу
    gluCylinder(gluNewQuadric(), 0.2, 0.2, leg_length, 20, 20)  # Рисуем ногу
    glPopMatrix()

# Функция для установки освещения
def set_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    light_position = [0, 1, 1, 0]  # Исходящая позиция света
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    ambient_light = [0.2, 0.2, 0.2, 1]  #Ambient light
    diffuse_light = [1.0, 1.0, 1.0, 1]  #Diffuse light
    specular_light = [1.0, 1.0, 1.0, 1]  #Specular light

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    glEnable(GL_DEPTH_TEST)  # Включение теста глубины
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Установка перспективы
    glTranslatef(0.0, 0.0, -10)  # Перемещение камеры назад

    set_lighting()  # Устанавливаем освещение

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Рисуем марсианина, куб и сферу
        glPushMatrix()
        glTranslatef(2, -1, 0)  # Позиция куба
        draw_cube(1)  # Рисовать куб
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(0, 1, 0)  # Позиция сферы
        draw_sphere(1, 10, 10)  # Рисовать сферу
        glPopMatrix()

        draw_martian((0, 0, -5))  # Положение марсианина
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()