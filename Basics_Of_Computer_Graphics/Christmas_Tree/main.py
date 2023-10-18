
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_rot = 0.0
y_rot = 0.0
z_rot = 0.0
zoom = 1.0

def star():
    glTranslate(0.0, 0.75, 0.0)

    #создаём перевёрнутый пятиугольник как тело звезды
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.125, 0.0, 0.0)
    glVertex3f(0.125, 0.0, 0.0)
    glVertex3f(0.25, -0.15, 0.0)
    glVertex3f(0.0, -0.25, 0.0)
    glVertex3f(-0.25, -0.15, 0.0)
    glEnd()

    #создаём 5 треугольников как концы звезды
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.125, 0.0, 0.0)
    glVertex3f(0.125, 0.0, 0.0)
    glVertex3f(0.0, 0.25, 0.0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(0.125, 0.0, 0.0)
    glVertex3f(0.25, -0.15, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(0.25, -0.15, 0.0)
    glVertex3f(0.0, -0.25, 0.0)
    glVertex3f(0.4, -0.4, 0.0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.4, -0.4, 0.0)
    glVertex3f(-0.25, -0.15, 0.0)
    glVertex3f(0.0, -0.25, 0.0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.125, 0.0, 0.0)
    glVertex3f(-0.25, -0.15, 0.0)
    glVertex3f(-0.5, 0.0, 0.0)
    glEnd()
    glTranslate(0.0, -0.75, 0.0)

def triangles(x, y, z):
    #рисуем пирамиду (уровень ёлки, треугльниками)

    #задаём тень материалам
    #material_diffuse = [0.0, 1.0, 0.0, 1.0]
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-x, 0.0, z)
    glVertex3f(x, 0.0, x)
    glVertex3f(0.0, y, 0.0)
    glEnd()

    #material_diffuse = [0.0, 1.0, 0.0, 1.0]
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(x, 0.0, z)
    glVertex3f(x, 0.0, -z)
    glVertex3f(0.0, y, 0.0)
    glEnd()

    #material_diffuse = [0.0, 1.0, 0.0, 1.0]
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(x, 0.0, -z)
    glVertex3f(-x, 0.0, -z)
    glVertex3f(0.0, y, 0.0)
    glEnd()

    #material_diffuse = [0.0, 1.0, 0.0, 1.0]
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-x, 0.0, -z)
    glVertex3f(-x, 0.0, z)
    glVertex3f(0.0, y, 0.0)
    glEnd()

def trunk(width, height, depth, red, green, blue):
    #рисуем ствол (несколько прямоугольников)

    # задаём тень материалам
    #material_diffuse = [0.75, 0.75, 0.0, 1.0]
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)

    glColor3f(red, green, blue)
    glBegin(GL_QUADS)

    # Front face
    glVertex3f(0, 0, 0)
    glVertex3f(width, 0, 0)
    glVertex3f(width, height, 0)
    glVertex3f(0, height, 0)

    # Back face
    glVertex3f(0, 0, depth)
    glVertex3f(width, 0, depth)
    glVertex3f(width, height, depth)
    glVertex3f(0, height, depth)

    # Top face
    glVertex3f(0, height, 0)
    glVertex3f(width, height, 0)
    glVertex3f(width, height, depth)
    glVertex3f(0, height, depth)

    # Bottom face
    glVertex3f(0, 0, 0)
    glVertex3f(width, 0, 0)
    glVertex3f(width, 0, depth)
    glVertex3f(0, 0, depth)

    # Right face
    glVertex3f(width, 0, 0)
    glVertex3f(width, 0, depth)
    glVertex3f(width, height, depth)
    glVertex3f(width, height, 0)

    # Left face
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, depth)
    glVertex3f(0, height, depth)
    glVertex3f(0, height, 0)

    glEnd()

def toys(x_trans, y_trans, z_trans, red, green, blue):
    glTranslate(x_trans, y_trans, z_trans)
    trunk(0.10, 0.10, 0.10, red, green, blue)
    glTranslate(-x_trans, -y_trans, -z_trans)


def draw():
    #рисуем звезду
    star()
    # Рисуем ёлку (после каждого объекта задаём смещение вниз, а для ствола - и по другим осям)
    triangles(0.5, 0.5, 0.5)

    #игрушки на первом уровне
    toys(-0.375, -0.1, -0.375, 1.0, 1.0, 1.0)
    toys(0.375, -0.1, 0.375, 0.0, 0.0, 1.0)
    toys(-0.375, -0.1, 0.375, 1.0, 0.0, 0.0)
    toys(0.375, -0.1, -0.375, 1.0, 1.0, 0.0)

    # игрушки на втором уровне
    toys(-0.375, -0.6, -0.375, 0.0, 0.0, 1.0)
    toys(0.375, -0.6, 0.375, 1.0, 1.0, 1.0)
    toys(-0.375, -0.6, 0.375, 1.0, 1.0, 0.0)
    toys(0.375, -0.6, -0.375, 1.0, 0.0, 0.0)

    yOffset = -0.5
    glTranslate(0.0, yOffset, 0.0)

    triangles(0.75, 0.75, 0.75)
    yOffset_toys1 = yOffset - 0.50
    # игрушки на третьем уровне
    toys(-0.375, yOffset_toys1, -0.375, 1.0, 0.0, 0.0)
    toys(0.375, yOffset_toys1, 0.375, 0.0, 0.0, 1.0)
    toys(-0.375, yOffset_toys1, 0.375, 1.0, 1.0, 1.0)
    toys(0.375, yOffset_toys1, -0.375, 1.0, 1.0, 0.0)

    yOffset = -0.75
    glTranslate(0.0, yOffset, 0.0)

    triangles(1.0, 1.0, 1.0)

    xOffset = -0.15
    yOffset = -0.8
    zOffset = -0.15
    glTranslate(xOffset, yOffset, zOffset)
    trunk(0.3, 0.8, 0.3, 0.75, 0.75, 0.0)

def display():
    #корректное отображение цветов и вращения объектов
    global x_rot, y_rot, z_rot, zoom
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslate(0.0, 0.0, -5.0 * zoom)
    glRotate(x_rot, 1.0, 0.0, 0.0)
    glRotate(y_rot, 0.0, 1.0, 0.0)
    glRotate(z_rot, 0.0, 0.0, 1.0)
    #glutSolidTeapot(0.5)
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
    glutCreateWindow(b"Happy New Year!")

    #передаём функции
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(resize)
    glutKeyboardFunc(key_callback)

    #задаём задний фон
    glClearColor(0.5, 0.5, 0.5, 1.0)

    #работаем со светом и тенью
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT0)
    #light_ambient = [0.5, 0.5, 0.5, 1.0]
    #light_diffuse = [0.7, 0.7, 0.7, 1.0]
    #light_position = [1.0, 1.0, 1.0, 0.0]
    #glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    #glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    #бесконечный цикл для отображения окна
    glutMainLoop()

init()
