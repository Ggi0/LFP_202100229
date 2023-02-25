import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

print('''
\n----------------------------------------------------\n
“Lenguajes Formales y de Programación” Sección: B-
Nombre:  Giovanni Saul Concohá Cax
Carné:   202100229

----------------------------------------------------\n''')

input("Presiona  'enter' para continuar...")




def opMenu1():
    clear()
    print('\n----------------------   Cargar archivo de entrada   ----------------------\n')
    archivos = open(input('Ingrese el nombre del archivo con la extensión: '), 'r') #dentro de los parentecis va la entrada
    linea = archivos.readline()
    print(f'\n1) {linea.rstrip()}')
    
    contador = 1
    while linea != '':
        linea = archivos.readline()
        contador += 1
        print(f'{contador}) {linea.rstrip()}')
        
    archivos.close()
    print('\nEl archivo cargo de forma correcta.')
    input("\nPresiona  'enter' para continuar...")

'''
def opMenu2():
    archivos = open('archivo.lfp', 'r')
    linea = archivos.readline()

    while linea != :
        pelicula = linea.split(';')
        print(pelicula[0])

    input("\nPresiona  'enter' para continuar...")
'''

def menu():
    clear()
    salirMenu = True

    while salirMenu :
        print('''\n
    ----------------------   Menú   ----------------------\n
    1) Cargar archivo de entrada
    2) Gestionar películas
    3) Filtrar
    4) Gráfica
    5) Salir
    ''')
        print('¿Qué acción desea realizar?')
        opMenu = input("inserta un número de la acción: >> ")
        
        if opMenu=="1":
            opMenu1()
        elif opMenu=="2":
            print('----------------------   Gestionar películas  ----------------------\n')
            print('1) Películas\n2) Actores')
        elif opMenu=="3":
            print('----------------------   Filtrar ----------------------\n')
        elif opMenu=="4":
            print('----------------------   Graficar  ----------------------\n')
        elif opMenu=="5":
            clear()
            print('\nAdíos\n')
            salirMenu = False
        else:
            print("No has pulsado ninguna opción valida...\n")
menu()




'''
nombre de una película
actores que participan en ella
año de estreno
género
'''