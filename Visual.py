import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from GUI import *
from Quaternion import *


def visual():
    video_flags = OPENGL | DOUBLEBUF
    pygame.init()
    screen = pygame.display.set_mode((800, 610), video_flags)
    pygame.display.set_caption("AnMeh")
    resizewin(800, 610)
    init()
    frames = 0
    ticks = pygame.time.get_ticks()
    while 1:
        gui = GUI()
        gui.begin()
        event = pygame.event.poll()
        [yaw, pitch, roll] = read_data()
        draw(1, yaw, pitch, roll)
        pygame.display.flip()
        frames += 1
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            break
    print("fps: %d" % ((frames * 1000) / (pygame.time.get_ticks() - ticks)))


def resizewin(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0 * width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init():
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def read_data():
    with open("Data.json", "r") as rf:
        data = json.load(rf)
    return data


def draw(w, nx, ny, nz):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0.0, -7.0)
    drawText((-2.6, 1.8, 2), "AnMeh", 18)
    drawText((-2.6, -2.2, 2), "Press Escape to exit.", 16)
    drawText((-2.6, -2, 2), "quaternion = " + quat_to_string(Euler_to_Quaternion(nx, ny, nz)), 14)
    yaw = nx
    pitch = ny
    roll = nz
    drawText((-2.6, -1.8, 2), "Yaw: %f, Pitch: %f, Roll: %f" % (yaw, pitch, roll), 16)
    glRotatef(-roll, 0.00, 0.00, 1.00)
    glRotatef(pitch, 1.00, 0.00, 0.00)
    glRotatef(yaw, 0.00, 1.00, 0.00)
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1, -1.0)
    glVertex3f(-1.0, 1, -1.0)
    glVertex3f(-1.0, 1, 1.0)
    glVertex3f(1.0, 1, 1.0)

    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(1.0, -1, 1.0)
    glVertex3f(-1.0, -1, 1.0)
    glVertex3f(-1.0, -1, -1.0)
    glVertex3f(1.0, -1, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 1, 1.0)
    glVertex3f(-1.0, 1, 1.0)
    glVertex3f(-1.0, -1, 1.0)
    glVertex3f(1.0, -1, 1.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1, -1.0)
    glVertex3f(-1.0, -1, -1.0)
    glVertex3f(-1.0, 1, -1.0)
    glVertex3f(1.0, 1, -1.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 1, 1.0)
    glVertex3f(-1.0, 1, -1.0)
    glVertex3f(-1.0, -1, -1.0)
    glVertex3f(-1.0, -1, 1.0)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 1, -1.0)
    glVertex3f(1.0, 1, 1.0)
    glVertex3f(1.0, -1, 1.0)
    glVertex3f(1.0, -1, -1.0)
    glEnd()


def drawText(position, textString, size):
    font = pygame.font.SysFont("Courier", size, True)
    textSurface = font.render(textString, True, (255, 255, 255, 255), (0, 0, 0, 255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos3d(*position)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
