import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def load_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    
    return texture_id

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)
    glMatrixMode(GL_MODELVIEW)

def enable_texture_mapping():
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)

def disable_texture_mapping():
    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)

def draw_olympic_rings(texture_ids):
    positions = [
        (-2.5, 1, 0),
        (0, 1, 0),
        (2.5, 1, 0), 
        (-1.2, 0, 0), 
        (1.2, 0, 0)
    ]

    glEnable(GL_TEXTURE_2D)

    for i, pos in enumerate(positions):
        glBindTexture(GL_TEXTURE_2D, texture_ids[i])
        glPushMatrix()
        glTranslatef(*pos)

        enable_texture_mapping()
        glutSolidTorus(0.35, 1.0, 30, 30) ####
        disable_texture_mapping()

        glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def init_lighting():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 5.0, 0.0, 1.0])
    
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0]) 
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [-5.0, 3.0, 5.0, 1.0])
    
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0]) 
    glLightfv(GL_LIGHT1, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0]) 

    glEnable(GL_LIGHT2)
    glLightfv(GL_LIGHT2, GL_POSITION, [5.0, 5.0, 0.0, 1.0])
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, [-1.0, -1.0, -1.0])

    glLightfv(GL_LIGHT2, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])  
    glLightfv(GL_LIGHT2, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  

def display(texture_ids):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_olympic_rings(texture_ids)
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Олимпийские кольца с текстурами")
    glutInit() 
    resize(600, 600)
    glClearColor(0.1, 0.1, 0.1, 1)
    init_lighting()

    textures = [
        load_texture("tekstura.png")
    ]

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        display(textures)
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
