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


# Mantener la ventana abierta
window.mainloop()  # Este metodo mantiene la ventana abierta