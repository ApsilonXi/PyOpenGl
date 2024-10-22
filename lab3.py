import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def resize(width, height):
    glViewport(0,0,width,height)
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    glOrtho(-5,5, -5,5, 2,12)
    gluLookAt( 0,0,5, 0,0,0, 0,1,0 )
    glMatrixMode( GL_MODELVIEW )

def display():
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

    glPushMatrix()
    glTranslated(0.5,4,0)
    glColor3d(0,0,1)
    glutSolidCube(1); # куб

    glTranslated(0,-2,0)
    glColor3d(0,1,1)
    glutSolidTorus(0.2,0.5); # тор

    glTranslated(0,-2,0)
    glColor3d(1,0,0)
    glutSolidCylinder(0.5,1); # цилиндр

    glTranslated(0,-2,0)
    glColor3d(0,1,0)
    glutSolidCone(1,1); # конус

    glTranslated(2,8,0)
    glColor3d(1,0,1)
    glutSolidIcosahedron(1); # икосаэдр

    glTranslated(0,-2,0)
    glColor3d(1,1,1)
    glutSolidOctahedron(1); # октаэдр

    glTranslated(0,-2,0)
    glColor3d(0,1,1)
    glutSolidTeapot(0.7) # чайник

    glTranslated(0,-2,0)
    glColor3d(0,1,0)
    glutSolidTetrahedron(1) # тетраэдр

    glTranslated(0,-2,0)
    glColor3d(1,1,0)
    glutSolidDodecahedron(1) # додо

    glTranslated(-6,8,0)
    glColor3d(0,0,1)
    glutWireCube(1) # каркасная модель куба

    glTranslated(0,-2,0)
    glColor3d(0,1,1)
    glutWireTorus(0.2,0.5) # каркасная модель тора

    glTranslated(0,-2,0)
    glColor3d(1,0,0)
    glutWireCylinder(0.5,1) # каркасная модель цилиндра

    glTranslated(0,-2,0)
    glColor3d(0,1,0)
    glutWireCone(1,1) # каркасная модель конуса

    glTranslated(2,8,0)
    glColor3d(1,0,1)
    glutWireIcosahedron(1) # каркасные модели икосаэдр

    glTranslated(0,-2,0)
    glColor3d(1,1,1)
    glutWireOctahedron(1) # октаэдр

    glTranslated(0,-2,0)
    glColor3d(0,1,1)
    glutWireTeapot(0.7) # каркасная модель чайника

    glTranslated(0,-2,0)
    glColor3d(0,1,0)
    glutWireTetrahedron(1) # тетраэдр

    glTranslated(0,-2,0)
    glColor3d(1,1,0)
    glutWireDodecahedron(1)

    glPopMatrix()
    glutSwapBuffers()

def main():
    pygame.init()
    display_pygame = (800, 600)
    pygame.display.set_mode(display_pygame, DOUBLEBUF | OPENGL)

    glutInit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        display()
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
