import turtle                           # Proporciona las herramientas graficas para dibujar en la pantalla
import time                             # Para controlar el tiempo,por ejemplo, pausas en el juego.
import random                           # Para generar numeros aleatorios,como las posiciones de la comida

#constantes
posponer = 0.1                          # Tiempo de espera entre cada actualización (controla la velocidad del juego).

#Configuracion de la ventana

window = turtle.Screen()                # Crea la ventana del juego
window.title("NeoSnake2")               # Asigna el titulo de la ventana
window.bgcolor("black")                 # Establecer el color de fondo a negro
window.setup(width=600, height=600)     # Define el tamaño de la ventana a 600x600 pixeles
window.tracer(0)                        # Desactiva la actualización automática de la pantalla



#Cabeza de la serpiente

cabeza = turtle.Turtle()                # Crea el objeto 'cabeza'.
cabeza.speed(0)                         # Establece la velocidad de animacion en el valor mas rapido.
cabeza.shape("square")                  # Asignando la forma de cuadrado a la cabeza.
cabeza.color("white")                   # Color blanco para la cabeza de la serpiente.
cabeza.penup()                          # Evita que la cabeza dibuje lineas mientras se mueve.
cabeza.goto(0,0)                  # Posiciona la cabeza en el centro de la pantalla.
cabeza.direction = "stop"               # La cabeza comienza detenida (Sin direccion).

# Comida
comida = turtle.Turtle()                # Crear el objeto 'comida'
comida.speed(0)                         # Velocidad de animacion rapida.
comida.shape("circle")                  # Asignando la forma de un circulo a la comida.
comida.color("red")                     # Asignando el color rojo a la comida.
comida.penup()                          # Evita que la comida dibuje mientras se mueve.


# Generar una posición inicial aleatoria para la comida

x = random.randint(-280,280)         # Genera una posicion aleatoria en el eje X.
y = random.randint(-280,280)         # Genera una posicion aleatoria en el eje Y.
comida.goto(x,y)                        # Coloca la comida en una posicion aleatoria.


# Funciones para cambiar la direccion de la serpiente

def arriba():
    if cabeza.direction != "down":      # No se puede ir hacia abajo si la serpiente esta yendo hacia arriba.
        cabeza.direction = "up"         # Cambia la direccion hacia arriba.

def abajo():
    if cabeza.direction != "up":        # No se peude ir hacia arriba si la serpiente esta yendo hacia abajo.
        cabeza.direction = "down"       # Cambia la direcion hacia abajo.

def izquierda():
    if cabeza.direction != "right":     # No se puede ir hacia la derecha si la serpiente esta yendo hacia la izquierda.
        cabeza.direction = "left"       # Cambia la direccion hacia la izquierda.

def derecha():
    if cabeza.direction != "left":      # No se puede ir hacia la izquierda si la serpiente esta yendo hacia la derecha.
        cabeza.direction = "right"      # Cambia la direccion hacia la derecha.

# Funcion para mover la serpiente segun su direccion actual.

def mov():
    if cabeza.direction == "up":        # Si la direccion es hacia arriba.
        y = cabeza.ycor()               # Obtiene la coordenada 'Y' actual de la cabeza.
        cabeza.sety(y + 20)             # Mueve la cabeza 20 pixeles hacia arriba.

    if cabeza.direction == "down":      # Si la direcicon es hacia arriba.
        y = cabeza.ycor()               # Obtiene la coordenada 'Y' actual de la cabeza.
        cabeza.sety(y - 20)             # Mueve la cabeza 20 pixeles hacia abajo.

    if cabeza.direction == "left":      # Si la direccion es hacia la izquierda.
        x = cabeza.xcor()               # Obtiene la coordenada 'X' actual de la cabeza.
        cabeza.setx(x - 20)             # Mueve la cabeza 20 pixeles hacia la izquierda.

    if cabeza.direction == "right":     # Si la direccion es hacia la derecha.
        x = cabeza.xcor()               # Obtiene la coordenada 'x' actual de la cabeza.
        cabeza.setx(x + 20)             # Mueve la cabeza 20 pixeles hacia la derecha


# Configurar los controles del teclado

window.listen()                            # Activa la escucha de eventos del teclado.
window.onkeypress(arriba, "Up")       # Asigna la tecla 'Up' para mover la serpiente hacia arriba
window.onkeypress(abajo, "Down")      # Asigna la tecla 'Down' para mover la serpiente hacia abajo
window.onkeypress(izquierda, "Left")  # Asigna la tecla 'Left' para mover la serpiente hacia la izquierda
window.onkeypress(derecha, "Right")   # Asigna la tecla 'Right' para mover la serpiente hacia la derecha.



# Bucle principal del jeugo que se ejecuta de manera continua
while True:
    window.update()                         # Actualiza la pantalla en cada iteracion.

    # Llama a la funcion mov() para mover la cabeza de la serpiente segun la direccion actual
    mov()

    # Pausa el juego por el tiempo especificado en 'posponer' (Para controlar la velocidad)
    time.sleep(posponer)

    # Detectar si la cabeza de la serpiente ha colisionado con los bordes de la ventana
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        # si ocurre una colision, se pausa el juego por 1 segundo.
        time.sleep(1)
        # Reinicia la posicion de la cabeza al centro de la pantalla (coordenadas 0,0)
        cabeza.goto(0,0)
        # Detiene el movimiento de la serpiente
        cabeza.direction = "stop"





# Mantener la ventana abierta
#window.mainloop()  # Este metodo mantiene la ventana abierta