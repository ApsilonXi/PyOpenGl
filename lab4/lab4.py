from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy as np

angle_x = 0
angle_y = 0
mouse_down = False
last_x, last_y = 0, 0
texture_id_body = None
texture_id_eyes = None

# Анимационные параметры
walk_angle = 0
walk_direction = 1  # 1 - вперед, -1 - назад

def load_texture(body_image, eyes_image):
    global texture_id_body, texture_id_eyes
    
    image_body = Image.open(body_image)
    img_data_body = image_body.convert("RGBA").tobytes()

    texture_id_body = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id_body)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_body.width, image_body.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data_body)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    image_eyes = Image.open(eyes_image)
    img_data_eyes = image_eyes.convert("RGBA").tobytes()

    texture_id_eyes = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id_eyes)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_eyes.width, image_eyes.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data_eyes)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glEnable(GL_DEPTH_TEST) 
    glEnable(GL_TEXTURE_2D) 
    load_texture("lab3/texture.png", "lab3/texture2.png")  

def draw_cylinder(radius, height, slices=32):
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluCylinder(quadric, radius, radius, height, slices, 1)

def draw_sphere(radius, slices=32, stacks=32):
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, slices, stacks)

def draw_antenna():
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    draw_cylinder(0.03, 0.5)
    glPopMatrix()
    glTranslatef(0.0, 0.05, 0.0)  
    draw_sphere(0.05)

def draw_eyes():
    glBindTexture(GL_TEXTURE_2D, texture_id_eyes)
    glPushMatrix()
    glTranslatef(-0.1, 0.7, 0.35)  
    draw_sphere(0.07)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1, 0.7, 0.35) 
    draw_sphere(0.07)
    glPopMatrix() 
    glBindTexture(GL_TEXTURE_2D, texture_id_body)

def draw_marsianin():
    glBindTexture(GL_TEXTURE_2D, texture_id_body)

    # Тело
    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.2)  
    glRotatef(90, 1.0, 0.0, 0.0)
    draw_cylinder(0.2, 1.0)
    glPopMatrix()

    # Голова
    glPushMatrix()
    glTranslatef(0.0, 0.7, 0.2)  
    draw_sphere(0.2)
    glPopMatrix()

    # Усики
    glPushMatrix()
    glTranslatef(-0.1, 1.0, 0.2)  # Левая
    draw_antenna()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1, 1.0, 0.2)  # Правая
    draw_antenna()
    glPopMatrix()

    # Левая нога
    glPushMatrix()
    glTranslatef(-0.2, -0.5, 0.2) 
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(np.sin(np.radians(walk_angle)) * 30, 1.0, 0.0, 0.0)  # Анимация ноги
    draw_cylinder(0.1, 0.5)
    glPopMatrix()

    # Правая нога
    glPushMatrix()
    glTranslatef(0.2, -0.5, 0.2)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(-np.sin(np.radians(walk_angle)) * 30, 1.0, 0.0, 0.0)  # Анимация ноги
    draw_cylinder(0.1, 0.5)
    glPopMatrix()

    # Левая рука
    glPushMatrix()
    glTranslatef(-0.3, 0.2, 0.2)  
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(-np.sin(np.radians(walk_angle)) * 30, 1.0, 0.0, 0.0)  # Анимация руки
    draw_cylinder(0.07, 0.6)
    glPopMatrix()

    # Правая рука
    glPushMatrix()
    glTranslatef(0.3, 0.2, 0.2)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(np.sin(np.radians(walk_angle)) * 30, 1.0, 0.0, 0.0)  # Анимация руки
    draw_cylinder(0.07, 0.6)
    glPopMatrix()

    # Глаза
    draw_eyes()

def update_walk(value):
    global walk_angle, walk_direction
    walk_angle += walk_direction * 2  # Скорость ходьбы
    if walk_angle > 30 or walk_angle < -30:
        walk_direction *= -1  # смена направления движения ног
    glutPostRedisplay()
    glutTimerFunc(16, update_walk, 0)  # вызываем обновление (~60 FPS)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5.0)  
    glRotatef(angle_x, 1.0, 0.0, 0.0)
    glRotatef(angle_y, 0.0, 1.0, 0.0)

    draw_marsianin()

    glutSwapBuffers()

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
        angle_x += (y - last_y) * 0.5
        angle_y += (x - last_x) * 0.5
        last_x, last_y = x, y
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Marsianin with Texture and Animation")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)

    # Запуск анимации
    glutTimerFunc(16, update_walk, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
