#Ejercicio 1

saludo = "Hola Mundo!"
print(saludo)


#Ejercicio 2

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


#Ejercicio 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su Provincia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años, vivo en {residencia}")



#Ejercicio 4
radio_circulo = int(input("Escribe el radio de un circulo: "))
print(f"El area del circulo es : {3.1416*(radio_circulo**2)} y el perimetro es: {2*3.1416*radio_circulo}")


#Ejercicio 5
segundos = int(input("Escriba una cantidad de segundos: "))
minutos = segundos / 60
print(f"los segundos ingresados corresponden a : {minutos/60} horas ")


#Ejercicio 6
numero = int(input("Escribe un numero: "))
print(f"tabla es:{numero}*1 = {numero*1} ")
print(f"tabla es:{numero}*2 = {numero*2} ")
print(f"tabla es:{numero}*3 = {numero*3} ")
print(f"tabla es:{numero}*4 = {numero*4} ")
print(f"tabla es:{numero}*5 = {numero*5} ")
print(f"tabla es:{numero}*6 = {numero*6} ")
print(f"tabla es:{numero}*7 = {numero*7} ")
print(f"tabla es:{numero}*8 = {numero*8} ")
print(f"tabla es:{numero}*9 = {numero*9} ")
print(f"tabla es:{numero}*10 = {numero*10} ")


#Ejercicio 7
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))
suma = 0
multiplicacion = 0
division = 0
resta = numero1-numero2
if (numero1 != 0 and numero2 != 0):
    suma = numero1+numero2
    multiplicacion = numero1*numero2
    division = numero1/numero2
    resta = numero1 - numero2
    print(f"el resultado de los numeros es suma: {suma}, resta: {resta}, division: {division}, multiplicacion : {multiplicacion}")
else:
    print("Los numeros ingresados deben ser distinto de cero ")


#Ejercicio 8
altura = int(input("Ingrese de altura en centimetros: "))
peso = int(input("Ingrese su peso en kg: "))
altura = altura/100
print(f"el indice de masa corporal es igual a :{peso/(altura*altura)}")


#Ejercicio 9
celcius = int(input("Escriba la temperatura en grados celcius (solo numero): "))
fahrenheit = (9/5)*celcius+32
print(f"El resultado de los grados celcius : {celcius} pasado a fahrenheit es : {int(fahrenheit)}°")


#Ejercicio 10
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))
numero3 = int(input("Ingrese numero 3: "))
suma = numero1+numero2+numero3
print(f"El primedio de dichos numeros es : {suma/3}")
