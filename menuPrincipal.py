from os import system as pantalla_win
from calculadoras import CalculadorasMenu
from operacionesConNumeros import OperacionesConNumeros
from tratamientoLista import menu as Lista
from menuOperacionesCadenas import menu as OperacionesConCadenas

class MenuPrincipal:
    def __init__(self):
        pass
    
    def seleccion(self):
        opc = 0
        while opc != 5:
            pantalla_win('cls')
            print('+BIENVENID@ AL MENÚ PRINCIPAL+')
            print(' 1) Calculadora')
            print(' 2) Operación Numeros')
            print(' 3) Tratamiento de Listas')
            print(' 4) Operaciones de Cadenas')
            print(' 5) Salir')
            print('')
            while True:
                try:
                    opc = int(input('Selecciona una opción: '))
                    if opc > 0 and opc < 6: break
                    else: print('Ingrese una opción correcta.')
                except ValueError:
                    print('Ingrese un valor válido.')
            if opc == 1: CalculadorasMenu().menu()
            elif opc == 2: OperacionesConNumeros().menu()
            elif opc == 3: Lista()
            elif opc == 4: OperacionesConCadenas()
        else:
            print('¡Gracias por visitarnos!')
            input('Pulsa Enter <-- para salir... ')
            pantalla_win('cls')


if __name__ == '__main__':
    menu = MenuPrincipal()
    menu.seleccion()
    