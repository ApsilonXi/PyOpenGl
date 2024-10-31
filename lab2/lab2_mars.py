from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

angle_x = 0
angle_y = 0
mouse_down = False
last_x, last_y = 0, 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glEnable(GL_DEPTH_TEST) 

def draw_cylinder(radius, height, slices=32):
    quadric = gluNewQuadric()
    gluCylinder(quadric, radius, radius, height, slices, 1)

def draw_sphere(radius, slices=32, stacks=32):
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, slices, stacks)

def draw_antenna():
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    draw_cylinder(0.03, 0.5)
    glPopMatrix()
    glTranslatef(0.0, 0.05, 0.0)  
    draw_sphere(0.05)

def draw_eyes():
    glColor3f(0.0, 1.0, 0.0)  # Зелёные глаза
    glPushMatrix()
    glTranslatef(-0.1, 0.7, 0.35)  
    draw_sphere(0.07)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1, 0.7, 0.35) 
    draw_sphere(0.07)
    glPopMatrix()

def draw_marsianin():
    glColor3f(1.0, 0.5, 0.0)  # Оранжевый цвет

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
    draw_cylinder(0.1, 0.5)
    glPopMatrix()

    # Правая нога
    glPushMatrix()
    glTranslatef(0.2, -0.5, 0.2)
    glRotatef(90, 1.0, 0.0, 0.0)
    draw_cylinder(0.1, 0.5)
    glPopMatrix()

    # Левая рука
    glPushMatrix()
    glTranslatef(-0.3, 0.2, 0.2)  
    glRotatef(90, 1.0, 0.0, 0.0)
    draw_cylinder(0.07, 0.6)
    glPopMatrix()

    # Правая рука
    glPushMatrix()
    glTranslatef(0.3, 0.2, 0.2)
    glRotatef(90, 1.0, 0.0, 0.0)
    draw_cylinder(0.07, 0.6)
    glPopMatrix()

    # Глаза
    draw_eyes()

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
    glutCreateWindow(b"3D Marsianin Model")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()

if __name__ == "__main__":
    main()
