
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_rot = 0.0
y_rot = 0.0
z_rot = 0.0
zoom = 1.0

def draw_sphere(radius, slices, stacks):
    quad = gluNewQuadric()
    gluQuadricTexture(quad, True)
    gluSphere(quad, radius, slices, stacks)

def draw_head_base():
    glColor3f(0.6445, 0.164, 0.164)
    draw_sphere(1, 50, 50)

def draw_head_eyes():
    glTranslatef(-0.2, 0.15, 0.92)
    glColor3f(1, 1, 1)
    draw_sphere(0.1, 50, 50)
    glTranslatef(0.4, 0, 0)
    draw_sphere(0.1, 50, 50)
    glTranslatef(-0.4, 0, 0.06)
    glColor3f(0, 0, 0)
    draw_sphere(0.05, 50, 50)
    glTranslatef(0.4, 0, 0)
    draw_sphere(0.05, 50, 50)

def draw_head_nose():
    glTranslatef(-0.2, -0.2, 0)
    draw_sphere(0.15, 50, 50)

def draw_head_smile():
    glColor3f(0, 0, 0)
    glTranslatef(0, 0, -0.145)
    glutSolidTorus(0.1, 0.3, 20, 20)

def draw_head_ears():
    glTranslatef(-0.5, 0.8, -0.7)
    glutSolidTorus(0.1, 0.3, 20, 20)
    glTranslatef(0, -0.1, 0)
    glColor3f(0.6445, 0.164, 0.164)
    glutSolidTorus(0.1, 0.2, 20, 20)
    glTranslatef(1, 0.1, 0)
    glColor3f(0, 0, 0)
    glutSolidTorus(0.1, 0.3, 20, 20)
    glTranslatef(0, -0.1, 0)
    glColor3f(0.6445, 0.164, 0.164)
    glutSolidTorus(0.1, 0.2, 20, 20)

def draw_head():
    # основа
    draw_head_base()
    # глаза
    draw_head_eyes()
    # нос
    draw_head_nose()
    # улыбка
    draw_head_smile()
    # уши
    draw_head_ears()

def draw_body_base():
    glTranslatef(-0.5, -1.8, -0.135)
    glColor3f(0.6445, 0.164, 0.164)
    draw_sphere(1, 50, 50)

def draw_body_up_paws():
    glTranslatef(-1, 0.4, 0)
    glColor3f(0, 0, 0)
    draw_sphere(0.3, 50, 50)
    glTranslatef(2, 0, 0)
    draw_sphere(0.3, 50, 50)
    glTranslatef(-2.2, -0.15, 0)
    draw_sphere(0.27, 50, 50)
    glTranslatef(2.4, 0, 0)
    draw_sphere(0.27, 50, 50)
    glTranslatef(-2.45, -0.3, 0)
    draw_sphere(0.05, 50, 50)
    glTranslatef(2.5, 0, 0)
    draw_sphere(0.05, 50, 50)
    glTranslatef(-2.5, 0.05, -0.15)
    draw_sphere(0.05, 50, 50)
    glTranslatef(2.5, 0, 0)
    draw_sphere(0.05, 50, 50)
    glTranslatef(-2.5, 0, 0.3)
    draw_sphere(0.05, 50, 50)
    glTranslatef(2.5, 0, 0)
    draw_sphere(0.05, 50, 50)

def draw_body_down_paws():
    glTranslatef(-1.75, -1, -0.15)
    draw_sphere(0.3, 50, 50)
    glTranslatef(1, 0, 0)
    draw_sphere(0.3, 50, 50)
    glTranslatef(-1, 0, 0.3)
    draw_sphere(0.3, 50, 50)
    glTranslatef(1, 0, 0)
    draw_sphere(0.3, 50, 50)
    glTranslatef(-1.15, 0, 0.3)
    draw_sphere(0.05, 50, 50)
    glTranslatef(0.15, 0, 0.05)
    draw_sphere(0.05, 50, 50)
    glTranslatef(0.15, 0, -0.05)
    draw_sphere(0.05, 50, 50)
    glTranslate(1, 0, 0)
    draw_sphere(0.05, 50, 50)
    glTranslate(-0.15, 0, 0.05)
    draw_sphere(0.05, 50, 50)
    glTranslate(-0.15, 0, -0.05)
    draw_sphere(0.05, 50, 50)

def draw_body():
    # основа
    draw_body_base()
    # верхние лапы
    draw_body_up_paws()
    # нижние лапы
    draw_body_down_paws()

def draw():
    draw_head()
    draw_body()
    glFlush()

def display():
    #корректное отображение цветов и вращения объектов
    global x_rot, y_rot, z_rot, zoom
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslate(0.0, 0.0, -5.0 * zoom)
    glRotate(x_rot, 1.0, 0.0, 0.0)
    glRotate(y_rot, 0.0, 1.0, 0.0)
    glRotate(z_rot, 0.0, 0.0, 1.0)
    draw()
    glutSwapBuffers()

def resize(width, height):
    #реализация изменения размеров окна
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75.0, width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def key_callback(key, x, y):
    #вращение фигур нажатием опредеоёных кнопок
    global x_rot, y_rot, z_rot, zoom
    if key == b'i':
        x_rot -= 5
    if key == b'k':
        x_rot += 5
    if key == b'j':
        y_rot -= 5
    if key == b'l':
        y_rot += 5
    if key == b'u':
        z_rot += 5
    if key == b'o':
        z_rot -= 5
    if key == b'w':
        zoom /= 1.1
    if key == b's':
        zoom *= 1.1

def init():
    #создаём окно
    global x_rot, y_rot, z_rot
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(250, 50)
    glutCreateWindow(b"Vinny-Puh")
    #передаём функции
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(resize)
    glutKeyboardFunc(key_callback)
    #задаём задний фон
    glClearColor(0.5, 0.5, 0.5, 1.0)
    #работаем со светом и тенью
    glEnable(GL_DEPTH_TEST)
    #бесконечный цикл для отображения окна
    glutMainLoop()

init()
