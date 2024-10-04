import sys
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_z2():
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3d(1,1,1)
    glBegin(GL_QUADS)
    glVertex3d(-1,-1,0)
    glVertex3d(-1, 1,0)
    glVertex3d( 1, 1,0)
    glVertex3d( 1,-1,0)
    glEnd() 

if __name__ == "__main__":
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, (3,3,3,0.5))
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (-1,-1,-1))
        glMaterialfv(GL_FRONT, GL_SPECULAR, (1,1,1,1))
        glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
        glLighti(GL_LIGHT0, GL_SPOT_EXPONENT, 0)
        draw_z2()

        pygame.display.flip()
        pygame.time.wait(10)

