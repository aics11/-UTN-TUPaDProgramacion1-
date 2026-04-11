#05-tp listas
import random

#Ejercicio N°1
lista_notas = [8, 7, 10, 6, 9, 5, 8, 4, 10, 7]
promedio = sum(lista_notas) / len(lista_notas)

print(f"Lista de notas: {lista_notas}")
print(f"Promedio de notas: {promedio}")

nota_alta = max(lista_notas)
nota_baja = min(lista_notas)

print(f"La nota mas alta fue: {nota_alta} y la nota mas baja fue: {nota_baja}")


#Ejercicio N°2

productos = []
for i in range(5):
    productos.append(input("Ingrese el producto: ").lower())
print(sorted(productos)) #ordena la lista

eliminar_opcion = input("Desea eliminar algun producto? Presione n o N para finalizar o s/S para eliminar: ").lower()
if eliminar_opcion == "s":
    while eliminar_opcion == "s":
        borrar = input("ingrese el producto que desea eliminar: ").lower()
        if borrar in productos:
            productos.remove(borrar)
            print(f"nueva lista de productos: {productos}")
        else:
            print("El producto no esta en la lista. ")
        eliminar_opcion = input("Desea eliminar algun producto? Presione n o N para finalizar o s/S para eliminar: ").lower()
elif eliminar_opcion == "n":
    print(f"Los productos seleccionados fueron: {productos}")
else:
    print("Selecciono una opcion incorrecta")


#Ejercicio  N°3
lista_numeros = []
lista_pares = []
lista_impares = []
for i in range(15):
    numero_aleatorio = random.randint(1,100)
    lista_numeros.append(numero_aleatorio)
    if numero_aleatorio % 2 == 0:
        lista_pares.append(numero_aleatorio)
    else:
        lista_impares.append(numero_aleatorio)
print(f"De la siguiente lista aleatora: {lista_numeros}," 
      f" se separo entre la cantidad de numeros pares: {lista_pares}" 
      f" y la cantidad numeros impares: {lista_impares}")

#Ejercicio N°4

datos = [10,20,10,30,40,20,50,10]
lista_sin_duplicados = []

for numero in datos:
    if numero not in lista_sin_duplicados:
        lista_sin_duplicados.append(numero)
print(f"El resultado de la lista filtrada sin duplicados es: {lista_sin_duplicados}")


#Ejercicio N°5

lista_estudiantes = ["Ramiro", "Ruben", "Oscar", "Anacleta", "Milena", "Pilar", "Silvanas", "Ariel"]
opcion = ""
opcion = input("Desea Agregar o eliminar un estudiante? presione 1.- para agregar, 2.- para remover, 3.- para salir. ")
while opcion != "3":
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante que desea agregar a la lista. ")
        lista_estudiantes.append(nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante que desea eliminar de la lista. ")
        if nombre in lista_estudiantes:
            lista_estudiantes.remove(nombre)
        else:
            print("El nombre no pertenece a la lista. ")
    elif opcion == "3":
        print("Saliendo ...")
    else:
        print("Opcion incorrecta")
    opcion = input("Desea Agregar o eliminar un estudiante? presione 1.- para agregar, 2.- para remover, 3.- para salir. ")
print(f"La lista de estudiantes final es: {lista_estudiantes}")


#Ejercicio N°6

elementos = [1,5,7,9,8,2,30]
cantidad_elementos = len(elementos)
lista_inversa = []
for i in range(cantidad_elementos-1, - 1, -1):
    #print(elementos[i])
    lista_inversa.append(elementos[i])
print(lista_inversa)


#Ejercicio N°7
#Pronóstico detallado de la semana:
#Martes 7 Abr: 21°C / 9°C, inestable con lluvia.
#Miércoles 8 Abr: 21°C / 8°C, chubascos.
#Jueves 9 Abr: 18°C / 11°C, lluvia moderada/alta.
#Viernes 10 Abr: 19°C / 11°C, lluvias y lloviznas.
#Sábado 11 Abr: 17°C / 11°C, nublado y lluvias.
#Domingo 12 Abr: 24°C / 11°C, mayormente nublado.
#Lunes 13 Abr: 23°C / 12°C, probabilidad de lluvias.
#Detalle el pronosco me muestra maximas a la izquierda y minimas a la derecha seguire esa logica
temperaturas = [
    [21,9],  #Martes
    [21,8],  #Miercoles
    [18,11], #Jueves
    [19,11], #Viernes
    [17,11], #Sabado
    [24,11], #Domingo
    [23,12], #Lunes
]
maxima = 0
minima = 0

for dia in temperaturas:
    maxima += dia[0]
    minima += dia[1]

promedio_max = maxima/len(temperaturas) 
promedio_min = minima/len(temperaturas)
promedio_max = round(promedio_max, 2)
promedio_min = round(promedio_min, 2)
print(f"el promedio de la temperatura maxima de la semana es: {promedio_max}°," 
      f" y el promedio de la temperatura minima es :{promedio_min}°")


#Ejercicio N°8
estudiantes = [
    ["Ramiro",9,10,7],
    ["Julieta", 5,7,3],
    ["Claudia",9,9,9],
    ["Ariel",1,5,9],
    ["Ruben",7,8,9],
]
materias =["programacion 1", "ingles", "sistemas operativos"]

promedio_alumno = 0
promedio_materia = 0

for fila in estudiantes:
    nombre = fila[0]
    notas = fila[1:]
    promedio_alumno = sum(notas) / len(notas)
    promedio_alumno = round(promedio_alumno,2)
    print(f"Alumno: {nombre}, promedio del alumno: {promedio_alumno}")

cantidad_estudiantes = len(estudiantes)

for i in range(len(materias)):
    suma_materia = 0
    for fila in estudiantes:
        suma_materia += fila[i+1]
        promedio_materia = suma_materia / cantidad_estudiantes
    print(f"promedio de las materias: {materias[i]} es: {promedio_materia}")

#Ejercicio N°9
tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

print("Bienvenido al juego del tateti, donde eliges filas y columnas para jugar, el primer jugador en jugar comenzara con 'X'")
for i in range(9):
    fila = int(input("Ingrese la posicion deseada en la fila: "))
    columna = int(input("Ingrese la posicion de la columna deseada: "))
    print(i)
    if fila and columna < 0:
        print("Error el rango de 0 a 2, tanto en fila como columnas")
    elif fila and columna > 2:
        print("Error el rango de 0 a 2, tanto en fila como columnas")
    elif i % 2 == 0:
        tateti[fila][columna] = "X"
        for matriz in tateti:
            print(matriz)
    else:
        tateti[fila][columna] = "O"
        for matriz in tateti:
            print(matriz)
print("Juego finalizado...")  


#Ejercicio N°10
nombres = ["Plancha de pelo"],["Tostadora"],["Freidora de Aire"], ["Secadora de pelo"]
ventas = [
    [10, 20, 15, 30, 25, 10, 40], 
    [5, 15, 10, 5, 20, 30, 12],   
    [30, 40, 50, 20, 10, 10, 6],  
   [11, 11, 11, 11, 11, 11, 11]  
]
totales_productos = []
for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto: {nombres[i]} se vendio en total: {total}" )

print("-"*50)

ventas_diarias = []
for j in range(7): 
    suma_dia = 0
    for i in range(4):
        suma_dia = suma_dia + ventas[i][j]
    ventas_diarias.append(suma_dia)
mayor_venta = max(ventas_diarias)
dia_de_venta = ventas_diarias.index(mayor_venta)

print(f"El dia con mayor venta fue el dia: {dia_de_venta + 1} con {mayor_venta} ventas")

valor_maximo_del_producto = max(totales_productos)
indice_producto = totales_productos.index(valor_maximo_del_producto)
print(f"El producto mas vendido fue: {nombres[indice_producto]}({valor_maximo_del_producto}) unidades. ")


#Ejercicio 11

estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Facundo", "Gisela", "Hugo", "Iris", "Juan"]

buscar = input("Ingrese el nombre del estudiante que desea buscar: ").capitalize()

if buscar in estudiantes:
    posicion = estudiantes.index(buscar)
    print(f"el estudiante: {buscar} se encuentra en la lista. ")
    print(f"aparece en la posicion: {posicion}")
else:
    print(f"El nombre: {buscar} no esta en la lista. ")

#Ejercicio 12
numeros = []

for i in range(8):
    num = int(input("ingrese el numero entero. "))
    numeros.append(num)
    i += 1
print(f"lista original: {numeros}")

print(f"Menor a mayor {sorted(numeros)}")
print(f"Mayor a menor {sorted(numeros, reverse=True)}")

#Ejercicio 13
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"Puntaje mas alto: {max(puntajes)}")
print(f"Puntaje mas bajo: {min(puntajes)}")

ranking = sorted(puntajes, reverse=True)
print(f"ranking: {ranking}")

posicion = ranking.index(990) + 1
print(f"el puntaje 990 esta en la posicion N° {posicion} del Ranking: ") 

