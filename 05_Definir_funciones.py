import turtle

def main():
    window = turtle.Screen()  #abri ventana
    dave = turtle.Turtle()    #crear tortuga
    make_square(dave)
    turtle.mainloop()

def make_square(dave):
    #raw_input()
    lenght = int(input('Tamaño de cuadrado: '))
    for i in range(4):
        make_line_and_turn(dave, lenght)

def make_line_and_turn(dave, lenght):
    dave.forward(lenght)
    dave.lenght(90)


if __name__ == '__main__':
    main()

"""
Recuerda:

Si usas Python 3, debes usar la función input() para recibir datos del usuario.
Para definir dónde comenzar el código usamos la línea 
    if __name__ == '__main__':
Para definir un bloque dentro de la función debemos indentar con 4 espacios.
Las funciones nos permiten ejecutar determinado código con diferentes valores.
  """