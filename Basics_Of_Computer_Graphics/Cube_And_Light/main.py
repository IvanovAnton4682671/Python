
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_rot = 0.0
y_rot = 0.0
z_rot = 0.0
zoom = 1.0

def draw_cube(red, green, blue, scale):
    glColor3f(red, green, blue)
    glutSolidCube(scale)

def draw_platform(red, green, blue, scale_x, scale_y, scale_z):
    glColor3f(red, green, blue)
    glPushMatrix()
    glScalef(scale_x, scale_y, scale_z)
    glutSolidCube(1)
    glPopMatrix()

def draw():
    # создаём платформу тёмно-серого цвета
    draw_platform(0.1664, 0.1664, 0.1664, 10, 10, 1)
    glTranslatef(0, 0, 1)
    # создаём белый куб
    draw_cube(1, 1, 1, 1)

def light_green():
    # работаем со светом
    glEnable(GL_LIGHTING)  # включаем освещение
    glEnable(GL_LIGHT0)  # включаем источник света №0
    # для света первые 3 числа - координаты (x, y, z),
    # четвёртое - является ли свет направленным (0.0) или точечным (1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, [-5.0, 0.0, 2.0, 0.5])  # направленный источник света сверху
    # для света первые 3 числа - цвет (red, green, blue),
    # четвёртое - является ли свет прозрачным (0.0) или видимым (1.0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.0, 1.0, 0.0, 0.5])  # задаём зелёный цвет света
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # зеркальные свойства материала
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 50.0)  # степень зеркального отражения
    # добавление собственного цвета материала объектов в отражение
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)

# гораздо красивее с синим цветом
def light_yellow():
    # работаем со светом
    glEnable(GL_LIGHTING)  # включаем освещение
    glEnable(GL_LIGHT1)  # включаем источник света №1
    # для света первые 3 числа - координаты (x, y, z),
    # четвёртое - является ли свет направленным (0.0) или точечным (1.0)
    glLightfv(GL_LIGHT1, GL_POSITION, [5.0, 0.0, 2.0, 0.5])  # направленный источник света сверху
    # для света первые 3 числа - цвет (red, green, blue),
    # четвёртое - является ли свет прозрачным (0.0) или видимым (1.0)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 1.0, 0.0, 0.5])  # задаём жёлтый цвет света
    #glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.0, 0.0, 1.0, 0.5])  # задаём синий цвет света
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # зеркальные свойства материала
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 50.0)  # степень зеркального отражения
    # добавление собственного цвета материала объектов в отражение
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)

def display():
    # корректное отображение цветов и вращения объектов
    global x_rot, y_rot, z_rot, zoom
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslate(0.0, 0.0, -5.0 * zoom)
    glRotate(x_rot, 1.0, 0.0, 0.0)
    glRotate(y_rot, 0.0, 1.0, 0.0)
    glRotate(z_rot, 0.0, 0.0, 1.0)
    draw()
    glutSwapBuffers()
    glFlush()

def resize(width, height):
    # реализация изменения размеров окна
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75.0, width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def key_callback(key, x, y):
    # вращение фигур нажатием определёных кнопок
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
    # создаём окно
    global x_rot, y_rot, z_rot
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(250, 50)
    glutCreateWindow(b"Cube and Light")
    # передаём функции
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(resize)
    glutKeyboardFunc(key_callback)
    # задаём задний фон
    glClearColor(0.5, 0.5, 0.5, 1.0)
    # работаем со светом и тенью
    glEnable(GL_DEPTH_TEST)
    light_green()
    light_yellow()
    # бесконечный цикл для отображения окна
    glutMainLoop()

init()
