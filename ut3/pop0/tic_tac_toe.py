# Juego Tic-Tac-Toe en Python.

''' Haremos el tablero usando un diccionario 
    en el que las claves serán la ubicación 
    (por ejemplo: arriba a la izquierda, a la 
    mitad a la derecha, etc.) y sus valores 
    iniciales serán espacios vacíos y después 
    de cada movimiento  cambiaremos el valor
    de acuerdo a la elección del jugador. '''
    
''' Crearemos un tablero en blanco y mediante 
    el Numeric keypad (Teclado numérico) iremos
    modificando la ubicación de cada valor mediante
    el valor introducido por el usuario.
    Ejemplo tablero:
                    7|8|9
                    4|5|6
                    1|2|3
'''

board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }
