from turtle import *
from math import *

speed(0)
bgcolor("black")

# Patrón de círculos
for i in range(16):
    for j in range(18):
        color('#FFA216')
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Espiral del disco floral
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
goldens = 137.508
phi = goldens * (pi / 180)

for i in range(140):
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    setheading(i * goldens)
    penup()
    goto(x, y + 40)
    pendown()
    stamp()

def point(x, y):
    penup() 
    goto(x, y) 
    pendown()
    color ('black')  # Cambia el color aquí
    fillcolor('#000000')  # Relleno de color verde claro
    begin_fill()
    circle(4)
    end_fill()

def draw_T(x, y):
    position_t = [(x, y + 30),
                 (x + 6, y + 30),
                 (x + 12, y + 30),
                 (x + 18,y + 30),
                 (x + 24, y + 30),
                 (x + 12,y + 30),
                 (x + 12, y + 24),
                 (x + 12,y + 18),
                 (x + 12, y + 12),
                 (x + 12,y + 6),
                 (x + 12,y)]
    for pos in position_t:
        point(*pos)

def draw_U(x, y):
    position_u = [(x , y + 30),
                  (x, y + 24),
                  (x, y + 18),
                  (x, y + 12),
                  (x, y + 6),
                  (x + 3, y + 3),
                  (x + 6, y),
                  (x + 12, y - 1),
                  (x + 18, y),
                  (x + 21, y + 3),
                  (x + 24, y + 6),
                  (x + 24, y + 12),
                  (x + 24, y + 18),
                  (x + 24, y + 24),
                  (x + 24, y + 30),
                  (x + 12, y + 36),
                  (x + 16, y + 40)]
    for pos in position_u:
        point(*pos)

# Mueve el texto "TÚ" hacia arriba
draw_T(-27, 20)  # Subimos el texto 70 unidades hacia arriba
draw_U(7, 20)    # Subimos el texto 70 unidades hacia arriba

# Función para agregar un pie de página
def write_footer(text, x, y):
    penup()
    goto(x, y)
    pendown()
    color('white')  # Cambia el color aquí si prefieres otro
    write(text, align="center", font=("Arial", 16, "bold"))
    penup()

# Escribimos el pie de página después de dibujar el girasol
write_footer("Para Mi Novia Hermosa [Daniela♥] Te AMO a ti y A Mateus", 0, -250)  # Ajusta las coordenadas si es necesario

hideturtle()
done()

