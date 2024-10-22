import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5, 5, -5, 5, 2, 12)
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    #Куб 
    glPushMatrix()
    glTranslatef(0.5, 4, 0)
    glColor3f(0, 0, 1)
    glutSolidCube(1)
    glPopMatrix()

    #куб
    glPushMatrix()
    glTranslatef(0.5, 2, 0)
    glColor3f(0, 1, 0)
    glutSolidCube(1)
    glPopMatrix()

    # тор
    glPushMatrix()
    glTranslatef(0.5, 0, 0)
    glColor3f(0.5, 1, 0)
    glutSolidTorus(0.2, 0.5, 20, 20)
    glPopMatrix()

    #Цилиндр 
    glPushMatrix()
    glTranslatef(0.5, -2, 0)
    glColor3f(1, 0, 0)
    glutSolidCylinder(0.5, 1, 20, 20)
    glPopMatrix()

    # конус
    glPushMatrix()
    glTranslatef(0.5, -4, 0)
    glColor3f(0.8, 0, 0) 
    glutSolidCone(1, 1, 20, 20)
    glPopMatrix()

    # икосаэдр
    glPushMatrix()
    glTranslatef(3, 2, 0)
    glColor3f(0.1, 1, 0.4) 
    glutSolidIcosahedron()
    glPopMatrix()

    # октаэдр
    glPushMatrix()
    glTranslatef(3, 0, 0)
    glColor3f(1, 1, 1)  
    glutSolidOctahedron()
    glPopMatrix()

    # чайник
    glPushMatrix()
    glTranslatef(3, -2, 0)
    glColor3f(0.3, 0, 0.5)
    glutSolidTeapot(0.7)
    glPopMatrix()

    glPopMatrix()

    
    glPushMatrix()

    # каркасный куб
    glPushMatrix()
    glTranslatef(-2, 4, 0)
    glColor3f(0, 0, 1)  
    glutWireCube(1)
    glPopMatrix()

    # каркасный куб
    glPushMatrix()
    glTranslatef(-2, 2, 0)
    glColor3f(0, 1, 0)  
    glutWireCube(1)
    glPopMatrix()

    # каркасный тор
    glPushMatrix()
    glTranslatef(-2, 0, 0)
    glColor3f(1, 0, 0.3)  
    glutWireTorus(0.2, 0.5, 20, 20)
    glPopMatrix()

    # каркасный цилиндр
    glPushMatrix()
    glTranslatef(-2, -2, 0)
    glColor3f(1, 0, 0)  # 
    glutWireCylinder(0.5, 1, 20, 20)
    glPopMatrix()

    # каркасный конус
    glPushMatrix()
    glTranslatef(-2, -4, 0)
    glColor3f(0, 1, 0)  
    glutWireCone(1, 1, 20, 20)
    glPopMatrix()

    # каркасный икосаэдр
    glPushMatrix()
    glTranslatef(-4, 2, 0)
    glColor3f(0, 1, 0)
    glutWireIcosahedron()
    glPopMatrix()

    # каркасный октаэдр
    glPushMatrix()
    glTranslatef(-4, 0, 0)
    glColor3f(1, 1, 1)
    glutWireOctahedron()
    glPopMatrix()

    # каркасный чайник
    glPushMatrix()
    glTranslatef(-4, -2, 0)
    glColor3f(1, 0, 0) 
    glutWireTeapot(0.7)
    glPopMatrix()

    glPopMatrix()

    pygame.display.flip()

def init_lighting():
    pos = [3, 3, 3, 1]
    dir = [-1, -1, -1]

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, dir)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    glutInit() 
    resize(800, 600)
    glClearColor(0.5, 0.7, 1.0, 1.0)
    init_lighting()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        display()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()



