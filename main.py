import turtle #Proporciona las herramientas graficas para dibujar en la pantalla
import time #Para controlar el tiempo,por ejemplo, pausas en el juego.
import random # Para generar numeros aleatorios,como las posiciones de la comida

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



while True:
    window.update()                     # Actualiza la pantalla en cada iteracion.



# Mantener la ventana abierta
#window.mainloop()  # Este metodo mantiene la ventana abierta