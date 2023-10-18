
# Используя двумерные примитивы, изобразить флаг Ганы

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#import turtle
#from tkinter import *
#from PIL import Image, ImageTk
#import io

glutInit()

def draw_star():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(300, 283)
    glVertex2f(350, 283)
    glVertex2f(400, 250)
    glVertex2f(450, 283)
    glVertex2f(500, 283)
    glVertex2f(450, 316)
    glVertex2f(475, 350)
    glVertex2f(400, 330)
    glVertex2f(325, 350)
    glVertex2f(350, 316)
    glEnd()

def initialization():
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Flag of Ghana")
    glutDisplayFunc(display)
    glClearColor(0.5, 0.5, 0.5, 1.0)
    gluOrtho2D(0, 800, 600, 000)
    glutMainLoop()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(200, 150)
    glVertex2f(600, 150)
    glVertex2f(600, 250)
    glVertex2f(200, 250)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(200, 250)
    glVertex2f(600, 250)
    glVertex2f(600, 350)
    glVertex2f(200, 350)
    glEnd()

    draw_star()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(200, 350)
    glVertex2f(600, 350)
    glVertex2f(600, 450)
    glVertex2f(200, 450)
    glEnd()

    #glRasterPos2f(0, 0)
    #glDrawPixels(image.size[0], image.size[1], GL_RGB, GL_UNSIGNED_BYTE, image_data)
    glFlush()

#window = turtle.Screen()
#window.setup(width=800, height=600)
#turtle.speed(0)
#turtle.color("black")
#turtle.fillcolor("black")
#turtle.begin_fill()
#turtle.left(36)
#for i in range(5):
    #turtle.forward(250)
    #turtle.left(144)
#turtle.end_fill()
#image = window.getcanvas().postscript(colormode='color')
#image = Image.open(io.BytesIO(image.encode('utf-8')))
#image_data = image.tobytes("raw", "RGB")
#turtle.done()

initialization()
