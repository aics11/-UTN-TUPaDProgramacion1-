
#Ejercicio 1
edad = int(input("escriba su edad: "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad") 


#Ejercicio 2
nota = int(input("Escriba su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio 3

par = int(input("Escriba un numero: "))

if par % 2 == 0:
    print("El numero es par")
else:
    print("Por favor, ingrese un numero par")


#Ejercicio 4

edad = int(input("Escriba su edad: "))

if edad < 12:
    print("Usted es un niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es Adolecente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto joven")
else:
    print("Usted es un Adulto")


#Ejercicio 5
contraseña = input("Escriba una contraseña entre 8 y 14 caracteres: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha Ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

consumo = int(input("Escriba su consumo en Kwh: "))
if consumo < 150:
    print("Consumo bajo")
elif consumo  >= 150 and consumo <= 300:
    print("Consumo Medio")
elif consumo > 500:
    print("Consumo alto")
    print("Considere medidas de ahorro energetico")
else:
    print("Consumo alto")



#Ejercicio 7

palabra = input("Escribe una palabra o frase: ")
vocal = palabra[-1]
print(vocal)
if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
    print(palabra + "!")
else:
    print(palabra)


#Ejercicio 8

nombre = input("ingrese su nombre: ")
opcion = int(input("opcion 1: nombre en mayusculas, opcion 2: minisculas, opcion 3: Primera letra mayuscula"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("La opcion elegida no existe" )


#Ejercicio 9

magnitud = int(input("Escriba la magnitud del terremoto: "))
if magnitud < 3:
    print("Magnitud muy leve (imperceptible)")
elif magnitud >= 3 and  magnitud <4:
    print("Magnitud leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Magnitud Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud <6:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 6 and magnitud < 7:
    print( "Muy Fuerte (puede causar daños significativos)")
else:
    print("Magnitud > 7, Extremo (puede causar graves daños a gran escala)")


#Ejercicio 10

hemisferio = input("Escribir 'S' si pertenece al hemisferio sur o 'N' hemisferio norte: ")
mes = int(input("Escriba el mes en numero: "))
dia = int(input("Escriba el dia en numero: "))

if hemisferio == "N" or hemisferio == "n":
    match mes:
        case 12: 
            if dia > 20:
                print("Estamos en Invierno")
            else:
                print("Estamos en Otoño")
        case 1:
            print("Estamos en Invierno")
        case 2:
            print("Estamos en Invierno")
        case 3:
            if dia < 21:
                print("Estamos en inverno")
            else:
                "Estamos en Primavera"
        case 4:
            print("Estamos en Primavera")
        case 5:
            print("Estamos en Primavera")
        case 6:
            if dia <21:
                print("Estamos en Primavera")
            else:
                print("Estamos en Verano")
        case 7:
            print("Estamos en Verano")
        case 8:
            print("Estamos en Verano")
        case 9: 
            if dia < 21:
                print("Estamos en Verano")
            else:
                print("Estamos en Otoño")
        case _:
            print("Estamos en otoño")
elif hemisferio == "S" or hemisferio == "s":
    match mes:
        case 12: 
            if dia > 20:
                print("Estamos en Verano")
            else:
                print("Estamos en Primavera")
        case 1:
            print("Estamos en Verano")
        case 2:
            print("Estamos en Verano")
        case 3:
            if dia < 21:
                print("Estamos en Verano")
            else:
                "Estamos en Otoño"
        case 4:
            print("Estamos en Otoño")
        case 5:
            print("Estamos en Otoño")
        case 6:
            if dia <21:
                print("Estamos en Otoño")
            else:
                print("Estamos en Invierno")
        case 7:
            print("Estamos en Invierno")
        case 8:
            print("Estamos en Invierno")
        case 9: 
            if dia < 21:
                print("Estamos en Invierno")
            else:
                print("Estamos en Primavera")
        case _:
            print("Estamos en Primavera")
else:
    print("Por favor elija hemisfero N o S")