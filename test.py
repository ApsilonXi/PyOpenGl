import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

# Функция для загрузки текстуры
def load_texture(file_path):
    texture = glGenTextures(1)
    image = Image.open(file_path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Поворот изображения
    image_data = image.convert("RGBA").tobytes()
    
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    
    return texture

# Определение вершин куба и его текстурных координат
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0), 
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 7), (3, 6)
]

faces = [
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 5, 1, 2),
    (5, 4, 0, 1),
    (4, 7, 3, 0),
    (7, 6, 5, 4)
]

# Текстурные координаты
texture_coords = [
    (0, 0), (1, 0), (1, 1), (0, 1),
]

# Функция для отрисовки куба с текстурой
def draw_cube(texture):
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glBindTexture(GL_TEXTURE_2D, texture)
        for j in range(4):
            glTexCoord2f(texture_coords[j][0], texture_coords[j][1])  # Установка текстурных координат
            glVertex3fv(vertices[face[j]])  # Установка вершин
    glEnd()

# Инициализация Pygame и OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Загрузка текстуры
texture = load_texture('tekstura.png')  # Укажите путь к вашей текстуре

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Поворот куба
    glRotatef(1, 0, 1, 0)
    
    # Очистка и отрисовка
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube(texture)
    pygame.display.flip()
    pygame.time.wait(10)