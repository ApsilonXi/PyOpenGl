from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy as np

# Переменные для анимации
teapot_angle = 0
pouring = False

# Переменные для вращения сцены
angle_x = 0
angle_y = 0
mouse_down = False
last_x, last_y = 0, 0

# Текстуры
texture_id_teapot = None
texture_id_cup = None
texture_id_saucer = None
texture_id_tea = None

# Освещение
light_pos = [1.0, 1.0, 1.0, 1.0]

def load_texture(image_file):
    image = Image.open(image_file)
    img_data = image.convert("RGBA").tobytes()
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return texture_id

def init():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    
    global texture_id_teapot, texture_id_cup, texture_id_saucer, texture_id_tea
    texture_id_teapot = load_texture("lab5/teapot.png")
    texture_id_cup = load_texture("lab5/cup.png")
    texture_id_saucer = load_texture("lab5/saucer.png")
    texture_id_tea = load_texture("lab5/tea.png")

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glEnable(GL_COLOR_MATERIAL)

def draw_cylinder(radius, height, slices=32):
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluCylinder(quadric, radius, radius, height, slices, 1)

def draw_sphere(radius, slices=32, stacks=32):
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, slices, stacks)

def draw_teapot():
    glBindTexture(GL_TEXTURE_2D, texture_id_teapot)
    glPushMatrix()
    glTranslatef(-0.5, 0.5, 0.0)  # Позиционируем чайник
    glRotatef(teapot_angle, 0, 0, 1)  # Наклон чайника
    glRotatef(270, 0, 1, 0)  # Поворачиваем чайник на 270 градусов
    glutSolidTeapot(0.4)
    glPopMatrix()

def draw_cup():
    glBindTexture(GL_TEXTURE_2D, texture_id_cup)
    glPushMatrix()
    glTranslatef(0.5, 0.0, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    draw_cylinder(0.3, 0.5)  # Чашка
    glPopMatrix()

    # Чай внутри чашки
    glBindTexture(GL_TEXTURE_2D, texture_id_tea)
    glPushMatrix()
    glTranslatef(0.5, 0.25, 0.0)
    draw_sphere(0.27)  # Чай
    glPopMatrix()

def draw_saucer():
    glBindTexture(GL_TEXTURE_2D, texture_id_saucer)
    glPushMatrix()
    glTranslatef(0.5, -0.05, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    draw_cylinder(0.4, 0.05)  # Блюдце
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5.0)  # Удаляем камеру от сцены

    # Применяем вращение сцены
    glRotatef(angle_x, 1.0, 0.0, 0.0)
    glRotatef(angle_y, 0.0, 1.0, 0.0)

    # Рисуем чайник, чашку и блюдце
    draw_teapot()
    draw_cup()
    draw_saucer()

    glutSwapBuffers()  # Меняем буферы для двойной буферизации

def reshape(width, height):
    if height == 0:
        height = 1
    aspect = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def mouse(button, state, x, y):
    global mouse_down, last_x, last_y
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            mouse_down = True
            last_x, last_y = x, y
        else:
            mouse_down = False

def motion(x, y):
    global angle_x, angle_y, last_x, last_y
    if mouse_down:
        angle_x += (y - last_y) * 0.5  # Управление по оси X
        angle_y += (x - last_x) * 0.5  # Управление по оси Y
        last_x, last_y = x, y
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Teapot Pouring Animation with Mouse Rotation")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    
    # Настройка мыши
    glutMouseFunc(mouse)
    glutMotionFunc(motion)

    glutMainLoop()

if __name__ == "__main__":
    main()
