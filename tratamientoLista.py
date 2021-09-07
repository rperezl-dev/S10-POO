from os import system as pantalla_win
from operaciones_numeros.intermedio import Intermedio


class Lista(Intermedio):
    def __init__(self, lista=['h', '0', 'l', '@', ' ', ':', ')', ' ', '0', '1'], num=5):
        self.lista = lista
        self.num = num
    
    def presentar_lista(self):
        print('Recorrer lista')
        if len(self.lista) != 0:
            for i in range(len(self.lista)):
                if i+1 == len(self.lista):
                    print(self.lista[i] + '.')
                else: print(self.lista[i] + ',', end=' ')
        else: print(' -No hay elemento que recorrer.')
    
    def buscar_lista(self, valor='0'):
        print('Buscar valor')
        if len(self.lista) != 0:
            ubicacion_valor = []
            for i, j in enumerate(self.lista):
                if j == valor:
                    ubicacion_valor.append(i+1)
            print('El valor', valor, 'se encontró en la posición', ubicacion_valor)
            if not ubicacion_valor:
                print('El valor', valor, 'no se encontró en la lista.')
        else:
            print('No hay valor que buscar porque\nla lista está vacía.')

    def lista_factorial(self):
        lista_factoriales = []
        print('Lista con', end=' ')
        Intermedio.factorial(self, self.num)
        for i in reversed(range(1, self.num+1)):
            lista_factoriales.append(i)
        return lista_factoriales
    
    def primo(self):
        lista_primos = []
        no_primo = False
        print('Número primo')
        for numero in range(self.num+1):
            if numero >= 2:
                for i in range(2, numero):
                    if numero % i == 0:
                        no_primo = True
                        break
                if not no_primo:
                    lista_primos.append(numero)
            else: pass
            no_primo = False
        return lista_primos
    
    def lista_notas(self, lista_notas_dict={'Juan':[10, 8, 9], 'Pedro':[9, 5, 6]}):
        print('Lista con notas de alumnos')
        for i in lista_notas_dict:
            print('Para el alumno', i, 'sus notas son las siguientes:\n ->| ', end='')
            for j in lista_notas_dict[i]:
                print(j, end=' | ')
            print('')
    
    def insertar_lista(self, posicion=2, valor=3):
        print('Insertar valor en lista según posición')
        print('Lista antigua:', self.lista)
        self.lista.insert(posicion-1, valor)
        print('Lista nueva:', self.lista)
    
    def eliminar_lista(self, valor='0'):
        print('Eliminar ocurrencias de una lista')
        repeticiones_elemento = self.lista.count(valor)
        print('Lista antigua:', self.lista)
        if repeticiones_elemento:
            for i in range(repeticiones_elemento):
                self.lista.remove(valor)
            print('Lista nueva:', self.lista)
        else:
            print('No encontramos ese elemento')
    
    def retornar_valor_lista(self, posicion=0):
        print('Retorna cualquier valor de la lista eliminandolo')
        try:
            return self.lista[posicion-1]
        except IndexError:
            print('No existen los suficientes elementos para\npoder eliminar esa posición de la lista')
            print('Ingresa otra posición')
    
    def copiar_tupla_lista(self, tupla=('conversion', 'tupla', 'a', 'lista')):
        print('Copiar tupla a lista\nTupla prefabricada')
        print('Tupla:', tupla)
        print('Lista:', list(tupla))
    
    def vuelto_lista(self, lista_clientes_diccionario={15.0:['Carlos', 'Esther'], 10.0:['Pablo', 'Alex', 'Dick']}):
        print('Dar el vuelto a varios clientes')
        for i in lista_clientes_diccionario:
            print('Un valor de $' + str(i) + ' será entregado a los clientes:\n- ', end='')
            for j in lista_clientes_diccionario[i]:
                print(j + ' - ', end='')
            print('')


def menu():
    pantalla_win('cls')
    opc = 0
    while opc != 11:
        _lista = []
        _num = 0
        print('+Menú Tratamiento de Lista+')
        print('  1) Recorrer y presentar los datos de una lista')
        print('  2) Buscar un valor en una lista')
        print('  3) Retornar una lista con los factoriales')
        print('  4) Retornar una lista de números primos')
        print('  5) Recorrer una lista de diccionario con notas de alumnos')
        print('  6) Insertar un dato en una Lista dada lo Posición')
        print('  7) Eliminar todas las ocurrencias en una Lista')
        print('  8) Retornar cualquier valor de una lista eliminándolo')
        print('  9) Copiar cada elemento de una tupla en una lista')
        print(' 10) Dar el vuelto a varios clientes')
        print(' 11) Salir')
        print('************************************************************')
        print('')
        while True:
            try:
                opc = int(input('Ingrese una opción: '))
                if opc in range(1, 12): break
                else: print('Ingrese una opción disponible.')
            except ValueError:
                print('Ingrese una opción válida.')
        print('')
        # INGRESO DE VALORES
        if opc in range(1, 5) or opc in range(6, 9):  # OPCION 1 2 6 7 8 NECESITAN LISTA
            if opc not in range(3, 5):
                elemento = ''
                valor = ''
                print('Ingreso de elementos en una lista')
                print('Ingrese "exit()" sin comillas para salir')
                while elemento.replace(' ', '') != 'exit()':
                    elemento = input('-Ingrese un elemento: ')
                    if elemento.replace(' ', '') != 'exit()':
                        _lista.append(elemento)
                if (opc == 2 or opc == 6 or opc == 7):  # OPCION 2 7 ADICIONAL UN VALOR
                    valor = input('-Ingrese un valor: ')
            if opc == 3 or opc == 4 or opc == 6 or opc == 8:  # OPCION 3 4 SOLO NECESITAN VALORES, 6 VALOR POSICIÓN.
                _num = 0
                while True:
                    try:
                        _num = int(input('-Ingrese un número: '))
                        if _num > 0: break
                        else: print('Ingrese un número entero mayor a 0.')
                    except ValueError:
                        print('Ingrese un valor correcto.')
        elif opc == 5 or opc == 10:  # OPCION 5 10
            nombre = ''
            numero = ''
            diccionario = {}
            print('Ingreso de elementos en un diccionario')
            print('Ingrese "exit()" sin comillas para salir')
            if opc == 5:  # OPCION 5 LLAVE(NOMBRE) Y VALOR([NUMERO, NUMERO...])
                while True:  # VALIDACION PARA LLAVE    nombre.replace(' ', '') != 'exit()'
                    nombre = input('Ingrese un nombre: ')
                    if nombre != 'exit()':
                        diccionario[nombre] = []
                        while True:  # VALIDACION PARA VALOR    numero.replace(' ', '') != 'exit()'
                            try:
                                numero = input('Ingrese la calificación: ').replace(' ', '')
                                if numero.replace(' ', '') != 'exit()':
                                    numero_aux = float(numero)
                                    if numero_aux > 0 and numero_aux <= 10:
                                        diccionario[nombre].append(numero_aux)
                                    else:
                                        print('Ingrese notas entre un rango de 1-10.')
                                else:
                                    if numero.replace(' ', '') == 'exit()' and not diccionario[nombre]:  # Certifica que ingrese por lo menos un elemento.
                                        print('Ingresa al menos un valor.')
                                    else: break
                            except ValueError:
                                print('Ingrese un valor correcto.')
                    else:
                        if nombre.replace(' ', '') == 'exit()' and not diccionario:  # Certifica que ingrese por lo menos un elemento.
                            print('Ingresa al menos un elemento.')
                        else: break
            else:  # OPCION 10 LLAVE(NUMERO) Y VALOR([NOMBRE, NOMBRE])
                while True:  # VALIDACION PARA LLAVE
                    numero = input('Ingrese un valor: $')
                    if numero != 'exit()':
                        try:
                            numero = round(float(numero), 2)
                            diccionario[numero] = []
                            while True:  # VALIDACION PARA VALOR
                                    nombre = input('Ingrese los nombre de clientes: ').replace(' ', '')
                                    if nombre.replace(' ', '') != 'exit()':
                                            diccionario[numero].append(nombre)
                                    else:
                                        if nombre.replace(' ', '') == 'exit()' and not diccionario[numero]:  # Certifica que ingrese por lo menos un elemento.
                                            print('Ingresa al menos un valor.')
                                        else: break   
                        except ValueError:
                            print('Ingrese un valor correcto.')
                    else:
                        if numero.replace(' ', '') == 'exit()' and not diccionario:  # Certifica que ingrese por lo menos un elemento.
                            print('Ingresa al menos un elemento.')
                        else: break
        elif opc == 9: pass
        else:
            print('¡Gracias por visitarnos!')
            input('Pulsa Enter <-- para salir... ')
            pantalla_win('cls')
            break
        manipular_lista = Lista(_lista, _num)
        if opc != 11:
            print('')
            if opc == 1:
                manipular_lista.presentar_lista()
            elif opc == 2:
                manipular_lista.buscar_lista(valor)
            elif opc == 3:
                factorial = manipular_lista.lista_factorial()
                print('Lista Factorial:', factorial)
            elif opc == 4:
                primo = manipular_lista.primo()
                print(primo)
            elif opc == 5:
                manipular_lista.lista_notas(diccionario)
            elif opc == 6:
                manipular_lista.insertar_lista(_num, valor)
            elif opc == 7:
                manipular_lista.eliminar_lista(valor)
            elif opc == 8:
                valor_lista = manipular_lista.retornar_valor_lista(_num)
                print('Elemento de la lista:', valor_lista)
            elif opc == 9:
                manipular_lista.copiar_tupla_lista()
            else:
                manipular_lista.vuelto_lista(diccionario)
            input('\nPulsa Enter <-- para limpiar la pantalla... ')
            pantalla_win('cls')
