import turtle                           # Proporciona las herramientas graficas para dibujar en la pantalla
import time                             # Para controlar el tiempo,por ejemplo, pausas en el juego.
import random                           # Para generar numeros aleatorios,como las posiciones de la comida
import pygame                           # La diversion nunca termina.

# Inicializar pygame y el mixer
pygame.mixer.init()


# Sonidos
# Carga la cancion de fondo

pygame.mixer.music.load("assets/music/background/neon.mp3")     # Ruta de la cancion.
pygame.mixer.music.set_volume(0.2)      # Ajusta el volumen al 20%
pygame.mixer.music.play(-1)             # Reproducir en bucle (parametro -1 para bucle infinito)

# Cargar el sonido para cuando la serpiente coma
sonido_comida = pygame.mixer.Sound("assets/sounds/comida1.wav")     # Ruta del archivo de sonido.
sonido_comida.set_volume(0.5)                                       # Ajusta el volumen del sonido de la comida

# Cargar el sonido para cuando la serpiente toque el power-up-speed
sonido_power_up_speed = pygame.mixer.Sound("assets/sounds/power-up-speed.wav")
sonido_power_up_speed.set_volume(0.3)

#constantes
posponer = 0.1                          # Tiempo de espera entre cada actualización (controla la velocidad del juego).


# Marcador

score = 0                               # Puntuacion inicial del jugador.
high_Score = 0                          # Puntuacion mas alta alcanzada.

#Configuracion de la ventana

window = turtle.Screen()                # Crea la ventana del juego
window.title("NeoSnake2")               # Asigna el titulo de la ventana
window.bgcolor("black")                 # Establecer el color de fondo a negro
window.setup(width=600, height=600)     # Define el tamaño de la ventana a 600x600 pixeles
window.tracer(0)                        # Desactiva la actualización automática de la pantalla



# Texto del marcador
texto = turtle.Turtle()                 # Crea el objeto 'texto' para mostrar el marcador.
texto.speed(0)                          # No se necesita velocidad de animacion.
texto.color("white")                    # Texto de color blanco.
texto.penup()                           # Evita que el texto dibuje lineas.
texto.hideturtle()                      # Oculta el cursor de la tortuga.
texto.goto(0, 260)                # Coloca el texot en la parte superior de la pantalla.
texto.write("Score: 0   High Score: 0", align="center",font=("Courier", 24,"normal")) # Muestra el marcador inicial


#Cabeza de la serpiente

cabeza = turtle.Turtle()                # Crea el objeto 'cabeza'.
cabeza.speed(0)                         # Establece la velocidad de animacion en el valor mas rapido.
cabeza.shape("square")                  # Asignando la forma de cuadrado a la cabeza.
cabeza.color("white")                   # Color blanco para la cabeza de la serpiente.
cabeza.penup()                          # Evita que la cabeza dibuje lineas mientras se mueve.
cabeza.goto(0,0)                  # Posiciona la cabeza en el centro de la pantalla.
cabeza.direction = "stop"               # La cabeza comienza detenida (Sin direccion).

### Configuracion del juego
velocidad_inicial = 0.1
velocidad = velocidad_inicial
power_up_activo = False
posponer = velocidad
###

# Comida
comida = turtle.Turtle()                # Crear el objeto 'comida'
comida.speed(0)                         # Velocidad de animacion rapida.
comida.shape("circle")                  # Asignando la forma de un circulo a la comida.
comida.color("red")                     # Asignando el color rojo a la comida.
comida.penup()                          # Evita que la comida dibuje mientras se mueve.

# Segmentos del cuerpo de la serpiente (inicialmente vacíos)
segmentos = []  # Lista para almacenar los segmentos del cuerpo de la serpiente.

# Funcion que devuelve una lista de posiciones ocupadas por la serpiente
def obtener_posiciones_cuerpo():
    return [(segmento.xcor(), segmento.ycor()) for segmento in segmentos]

def aparecer_comida():
    posiciones_cuerpo = obtener_posiciones_cuerpo()
    while True:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        # Verifica que la nueva posicion no este en el cuerpo
        if (x,y) not in posiciones_cuerpo:
            comida.goto(x,y)
            break

aparecer_comida()

# Generar una posición inicial aleatoria para la comida
#x = random.randint(-280,280)         # Genera una posicion aleatoria en el eje X.
#y = random.randint(-280,280)         # Genera una posicion aleatoria en el eje Y.
#comida.goto(x,y)                        # Coloca la comida en una posicion aleatoria.

# Power-up de velocidad
window.addshape("assets/img/speed.gif")
power_up_speed = turtle.Turtle()
power_up_speed.shape("assets/img/speed.gif")
power_up_speed.penup()
power_up_speed.hideturtle()

# Mostrar el power-up de velocidad en una posición aleatoria
def aparecer_power_up_speed():
    posiciones_cuerpo = obtener_posiciones_cuerpo()
    while True:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        # Verificar que la nueva posición no esté en el cuerpo
        if (x, y) not in posiciones_cuerpo:
            power_up_speed.goto(x, y)
            power_up_speed.showturtle()
            break

# Función para activar el efecto del power-up
def activar_power_up():
    global velocidad, power_up_activo, posponer
    duracion_power_up = random.randint(3, 7)  # Duración aleatoria entre 3 y 7 segundos
    velocidad = velocidad_inicial / 2         # Aumenta la velocidad temporalmente
    posponer = velocidad
    power_up_activo = True
    # Programar el desactivado después de la duración aleatoria del power-up
    window.ontimer(desactivar_power_up, duracion_power_up * 1000)

# Función para desactivar el efecto del power-up
def desactivar_power_up():
    global velocidad, power_up_activo, posponer
    velocidad = velocidad_inicial
    posponer = velocidad
    power_up_activo = False
    power_up_speed.hideturtle()


# Variable para almacenar la ultima direccion completada

ultima_direccion = "stop"

# Funciones para cambiar la direccion de la serpiente

def arriba():
    if cabeza.direction != "down" and ultima_direccion != "down":      # No se puede ir hacia abajo si la serpiente esta yendo hacia arriba.
        cabeza.direction = "up"                                        # Cambia la direccion hacia arriba.

def abajo():
    if cabeza.direction != "up" and ultima_direccion != "up":          # No se peude ir hacia arriba si la serpiente esta yendo hacia abajo.
        cabeza.direction = "down"                                      # Cambia la direcion hacia abajo.

def izquierda():
    if cabeza.direction != "right" and ultima_direccion != "right":    # No se puede ir hacia la derecha si la serpiente esta yendo hacia la izquierda.
        cabeza.direction = "left"                                      # Cambia la direccion hacia la izquierda.

def derecha():
    if cabeza.direction != "left" and ultima_direccion != "left":      # No se puede ir hacia la izquierda si la serpiente esta yendo hacia la derecha.
        cabeza.direction = "right"                                     # Cambia la direccion hacia la derecha.

# Funcion para mover la serpiente segun su direccion actual.

def mov():
    global ultima_direccion             # Hacer referencia a la variable global

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

    # Actualizar 'ultima_direccion' despues de completar el movimiento
    ultima_direccion = cabeza.direction






# Configurar los controles del teclado

window.listen()                            # Activa la escucha de eventos del teclado.
window.onkeypress(arriba, "Up")       # Asigna la tecla 'Up' para mover la serpiente hacia arriba
window.onkeypress(abajo, "Down")      # Asigna la tecla 'Down' para mover la serpiente hacia abajo
window.onkeypress(izquierda, "Left")  # Asigna la tecla 'Left' para mover la serpiente hacia la izquierda
window.onkeypress(derecha, "Right")   # Asigna la tecla 'Right' para mover la serpiente hacia la derecha.



# Bucle principal del juego que se ejecuta de manera continua
while True:
    window.update()                         # Actualiza la pantalla en cada iteracion.

    # Manejo de colisiones con el power-up de velocidad
    if power_up_speed.isvisible() and cabeza.distance(power_up_speed) < 20 and not power_up_activo:
        sonido_power_up_speed.play()
        activar_power_up()
        power_up_speed.hideturtle()  # Ocultar el power-up hasta que reaparezca

    # Aparecer el power-up de velocidad aleatoriamente
    if not power_up_activo and random.randint(0, 50) == 0:
        aparecer_power_up_speed()



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

        # Ocultar todos los segmentos del cuerpo de la serpiente
        for segmento in segmentos:
            segmento.hideturtle() # Oculta el segmento de la pantalla

        # Vaciar la lista de segmentos, eleiminando el cuerpo de la serpiente
        segmentos.clear()

        # Reinicia el marcador a 0
        score = 0
        # Borrar el textoa ctual del marcador
        texto.clear()
        # Actualiza y muestra el marcador y el puntaje maximo
        texto.write("Score: {}    High Score: {}".format(score, high_Score),
                    align="center", font=("Courier", 24, "normal"))



    # Detectar si la cabeza de la serpiente esta lo suficientemente cerca de la comida (menos de 20 pixeles)
    if cabeza.distance(comida) < 20:
        sonido_comida.play()                    # Reproducir el sonido de la comida.
        # Generar nuevas coordenadas aleatorias para la comida dentro de los limites de la ventana
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        # Mover la comida a la nueva posicion aleatoria
        comida.goto(x,y)

        # Crear un nuevo segmento para el cuerpo de la serpiente
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)                 # Velocidad de animacion del nuevo segmento.
        nuevo_segmento.shape("square")          # Forma cuadrada para el segmento
        nuevo_segmento.color("grey")            # Color del segmento (Gris en este caso)
        nuevo_segmento.penup()                  # Deshabilitar la pluma para evitar que dibuje.
        # Añadir el nuevo segmento al final de la lista de segmentos.
        segmentos.append(nuevo_segmento)

        # Incrementa el marcador en 10 puntos
        score += 10

        # Si el puntaje actual es mayor al puntaje maximo registrado.
        if score > high_Score:
            high_Score = score # actualiza el puntaje maximo

        # Borra el texto actual y actualiza el marcador y el puntaje maximo
        texto.clear()
        texto.write("Score: {}    High Score: {}".format(score, high_Score),
                    align="center", font=("Courier", 24, "normal"))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos) # Obtener el numero total de segmentos en la serpiente
    # Desde el ultimo segmento hacia el primero, cada uno toma la posicon del segmento anterior
    for index in range (totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()         # Obtener la coordenada X del segmento anterior.
        y = segmentos[index - 1].ycor()         # Obtener la coordenada Y del segmento anterior.
        segmentos[index].goto(x,y)              # Mover el segmento actual a esa posicon

    # Si la serpiente tiene al menos un segmento
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    # Llama a la funcion mov() para mover la cabeza de la serpiente segun la direccion actual
    mov()

    # Detectar colisiones entre la cabeza y el cuerpo de la serpiente
    for segmento in segmentos:
        # Si la cabeza esta lo suficientemente cerca de cualquier segmento del cuerpo (menos de 20 pixeles)
        if segmento.distance(cabeza) < 20:
            # Pausar el juepo por 1 segundo antes de reiniciar
            time.sleep(1)
            # Reiniciar la posicion de la cabeza al centro de la pantalla
            cabeza.goto(0,0)
            # Detener el movimiento de la serpiente
            cabeza.direction = "stop"

            # Ocultar todos los segmentos del cuerpo de la serpiente
            for segmento in segmentos:
                segmento.hideturtle()  # Ocultar cada segmento de la pantalla

            # Vaciar la lista de segmentos para reiniciar el cuerpo de la serpiente.
            segmentos.clear()


            # Reiniciar el marcador a 0
            score = 0
            # Borrar el texto actual del marcador y actualizarlo
            texto.clear()
            texto.write("Score: {}    High Score: {}".format(score, high_Score),
                        align="center", font=("Courier", 24, "normal"))