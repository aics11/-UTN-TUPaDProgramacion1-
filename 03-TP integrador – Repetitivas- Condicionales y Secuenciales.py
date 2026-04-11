#tp N°3
#ejercicio N°1
nombre = input("Ingrese el nombre del cliente: ")
while not nombre.isalpha() or nombre == "":
    print("Error: Escriba solo letras para el nombre.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad_de_productos = input("Ingrese la cantidad de produstos a comprar: ")
while not cantidad_de_productos.isdigit() or int(cantidad_de_productos) <=0:
    print("Escribir solo digitos y que sea mayor que 0")
    cantidad_de_productos = input("Ingrese la cantidad de produstos a comprar: ")
suma = 0
suma_con_descuento = 0
total = 0


for i  in range(1,int(cantidad_de_productos)+1,1):
    precio_de_producto = input(f"Producto{i} - Precio: ")
    while not precio_de_producto.isdigit() or int(precio_de_producto) <= 0:
        print("ingrese solo numeros mayores a 0 : ")
        precio_de_producto = input(f"Producto{i} - Precio: ")
    precio_unitario = int(precio_de_producto)
    suma = precio_unitario + suma
    opcion_descuento = input(f"producto {i} - Tiene descuento  (S/N)? : ").lower()


    while opcion_descuento != "s" and opcion_descuento != "n":
        print("Ingrese 'S' O 'N'. ")
        opcion_descuento = input(f"producto {i} - Tiene descuento  (S/N)? : ").lower()
    
    if opcion_descuento == "s":
        suma_con_descuento += precio_unitario*0.90
    else:
        suma_con_descuento += precio_unitario

    total = suma_con_descuento + total
    
ahorro_total = suma - suma_con_descuento
promedio = suma_con_descuento / int(cantidad_de_productos)



print(f"\nCliente: {nombre}")
print(f"Total sin descuentos: ${suma}")
print(f"Total con descuentos: ${suma_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


#Ejercicio N°2

usuario = input("Ingrese el usuario: ")
clave = input("Ingrese su clave: ")
acceso = False
intentos = 1
while intentos < 3:
    if usuario == "alumno" and clave == "python123":
        print("Acceso concedido ")
        acceso = True
        break
    else:
        print(f"Error, va {intentos} de tres intentos, al llegar al limite se bloqueara la cuenta. ")
        intentos += 1
        usuario = input("Ingrese el usuario: ")
        clave = input("Ingrese su clave: ")
if intentos >= 3:
    print("Cuenta Bloqueada ")

opcion = ""
while opcion != "4":                                                                       #
    print("Elija la opcion que desea. ")
    print("1. Ver estado de inscripción")
    print("2. Cambiar clave")
    print("3. Mostrar mensaje motivacional")
    print("4. Salir")
    opcion = input("opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion)> 4:
        print("opción fuera de rango.")
        opcion = input("opcion: ") 
    if opcion == "1":
        print("Inscripto")
    elif opcion == "2":
        nueva_clave = input("Ingrese la nueva clave, mayor o igual 6 digitos. ")
        repetir = input("repita de nuevo la clave: ")
        if len(nueva_clave) >= 6 and nueva_clave == repetir:
            clave = nueva_clave
            print("La clave fue cambiada con exito.")
        else:
            print("Error: la clave no cumple requisitos o no coincide.")    
    elif opcion == "3":
        print("segui asi!!!")
    elif opcion == "4":
        print("Saliendo...")
    else:
        print("Opcion invalida")


#Ejercicio 3

nombre = input("ingrese el nombre del operador: ")


dia_de_reserva = ""
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

contarturno_lunes = 0
contarturno_martes = 0

while not nombre.isalpha() or nombre == "":
    print("Error, el nombre no puede tener digitos o estar vacio. ")
    nombre = input("ingrese el nombre del la persona a solcitar turno: ")
opcion = ""
while opcion != "5":
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion = input("Elija una opcion: ")
    if opcion == "1":
        dia_de_reserva = input("Ingrese el dia que desea rever lunes o martes: ")
        if dia_de_reserva.lower() == "lunes":
            if lunes1 == "":
                lunes1 = nombre
                print(f"Reserva realizada 1° turno del dia lunes para el señor/a {nombre}. ")
                contarturno_lunes += 1 
            elif lunes2 == "":
                lunes2 = nombre
                print(f"Reserva realizada 2° turno del dia lunes para el señor/a {nombre}. ")
                contarturno_lunes += 1 
            elif lunes3 == "":
                lunes3 = nombre
                print(f"Reserva realizada 3° turno del dia lunes para el señor/a {nombre}. ")
                contarturno_lunes += 1 
            elif lunes4 == "":
                lunes4 = nombre
                print(f"Reserva realizada 4° turno del dia lunes para el señor/a {nombre}. ")
                contarturno_lunes += 1 
        elif dia_de_reserva.lower() == "martes":
            if martes1 == "":
                martes1 = nombre
                print(f"Reserva realizada 1° turno del dia martes para el señor/a {nombre} . ")
                contarturno_martes += 1
            elif martes2 == "":
                martes2 = nombre
                print(f"Reserva realizada 2° turno del dia martes para el señor/a {nombre}. ")
                contarturno_martes += 1
            elif martes3 == "":
                martes3 = nombre
                print(f"Reserva realizada 3° turno del dia martes para el señor/a {nombre}. ")
                contarturno_martes += 1
            else:
                print("Todos los turnos ocupados, intente la semana que viene")
        else:
            print("Error, no eligio un dia valido. ")
    if opcion == "2":
        dia_de_reserva = input("Ingrese el dia que desea rever lunes o martes: ")
        if dia_de_reserva.lower() == "lunes":
            if lunes1 == nombre:
                print(f"Reserva a nombre del Sr/a{nombre} cancelada con exito. ")
                lunes1 = ""
            elif lunes2 == nombre:
                print(f"Reserva a nombre del Sr/a{nombre} cancelada con exito. ")
                lunes2 = ""
            elif lunes3 == nombre:
                print(f"Reserva a nombre del Sr/a{nombre} cancelada con exito. ")
                lunes3 = ""
            elif lunes4 == nombre:
                print(f"Reserva a nombre del Sr/a{nombre} cancelada con exito. ")
                lunes4 = ""
            else:
                print("Error nombre no existe en las reservas del lunes. ")
        elif dia_de_reserva.lower() == "martes":
            if martes1 == nombre:
                print(f"Reserva a nombre del Sr/a{nombre} cancelada con exito. ")
                martes1 = ""
            elif martes2 == nombre:
                print(f"Reserva a nombre del Sr/a{nombre} cancelada con exito. ")
                martes2 = ""
            elif martes3 == nombre:
                print(f"Reserva a nombre del Sr/a{nombre} cancelada con exito. ")
                martes3 = ""
            else:
                print("Error, nombre no existe en la reserva del martes. ")
    if opcion == "3":
        dia_de_reserva = input("Ingrese el dia de la agenda que desea ver lunes o martes: ")
        if dia_de_reserva.lower() == "lunes":
            print(f" listado de la agenda de turnos: 1°turno: {lunes1}, 2°turno: {lunes2}, 3°turno: {lunes3}, 4°turno: {lunes4} ")
    if opcion == "4":
        print(f"lunes: {contarturno_lunes} ocupados, libre {4 - contarturno_lunes}")
        print(f"martes: {contarturno_martes} ocupados, libre {3 - contarturno_martes}")
    if opcion == "5":
        print("cerrando sistema...")
    nombre = input("ingrese el nombre del operador: ")
    


#Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_cerradura = 0

agente = input("Ingrese el nombre del agente: ")
while not agente.isalpha():
    agente = input("Error, Ingrese el nombre del agente(solo letras): ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3: #corazon del juego, esto mantiene el juego andando mientras se cumplan las codiciones minimas, que es tener vida tiempo y no tener las 3 cerraduras 
    print("Menú de acciones. ")
    print("1. Forzar cerradura  (costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel (costo: -10 energía, -3 tiempo)")
    print("3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")
    menu = input(" Ingrese la accion deseada: ")
    while not menu.isdigit() and menu in ["1","2","3"]:
        menu = input("Error, Ingrese exclusivamente 1,2 o 3, para realizar las acciones. ")
    if menu == "1":
        forzar_cerradura += 1
        energia -= 20
        tiempo -= 2

        if forzar_cerradura == 3:
            alarma = True
            print("la cerradura se trabó! ")
            
        else:
            if energia < 40:
                print("riesgo de alarma! ")
                numero = input("Ingrese un numero entre 1 y 3: ")
                while not numero.isdigit():
                    numero = input("Error, ingrese un numero entre 1 y 3: ")
                if numero == "3":
                    alarma = True
                    print("Sistema bloqueado!")
            if not alarma:
              cerraduras_abiertas +=1
              print("Abriste la cerradura. ")
        print("\nEstado:")
        print(f"Energia: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    elif menu == "2":
        energia -= 10
        tiempo -= 3
        forzar_cerradura = 0
        for i in range(4):
            codigo_parcial += "A"
            print(f"hackeando cerradura ... {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"Lograste abrir una cerradura! ")
        print("\nEstado:")
        print(f"Energia: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    elif menu == "3":
        forzar_cerradura = 0
        tiempo -=1
        if alarma:
            energia = energia-10
        energia += 15
        if energia > 100:
            energia = 100
        print("Descansaste ...")
        print("\nEstado:")
        print(f"Energia: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("🚨 Sistema bloqueado! Perdiste")
        break
#Ejercicio N°5  
Vida_del_Gladiador = 100
Vida_del_Enemigo = 100
Pociones_de_Vida = 3
Ataque_Pesado = 15
Daño_base_del_enemigo = 12
Turno_Gladiador = True
menu = ""
nombre = input("Ingrese el nombre del Gladiador: ")
while not nombre.isalpha() or nombre == "":
    nombre = input("Error, ingrese el nombre Gladiador(Solo letras): ")
while Vida_del_Enemigo > 0 and Vida_del_Gladiador > 0:
    print(f"\nEstado de {nombre}... ")
    print(f"Vida de restante de {nombre}: {Vida_del_Gladiador}")
    print(f"pociones restantes de {nombre}: {Pociones_de_Vida}")
    print(f"Vida del enemigo restante: {Vida_del_Enemigo}")
    while Turno_Gladiador == True:
        print("\nMenu de acciones. ")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar ")
        menu = input("Ingrese la accion que desea realizar: ")
        while not menu.isdigit() or menu not in ["1","2","3"]: #forzar que solo se pueda usar 1,2 3, como opcion
            print("Error, la opcion debe ser entre 1 y 3. ")
            menu = input("Ingrese la accion que desea realizar: ")
        print(f"Seleccionaste la opcion: {menu}")
        if menu == "1":
            if Vida_del_Enemigo < 20:
                print("Golpe Critico! ")
                Golpe_Critico = float(Ataque_Pesado *1.5)#para cumplir con el requerimiento solicitado
                print(f"¡Atacaste al enemigo por {Golpe_Critico} puntos de daño!")
                Vida_del_Enemigo = Vida_del_Enemigo - Golpe_Critico 
            else:
                Vida_del_Enemigo -= Ataque_Pesado
                print(f"¡Atacaste al enemigo por {Ataque_Pesado} puntos de daño!")
            break #este break es indispensable para poder salir del bucle del menu
        elif menu == "2":
            for i in range(3):
                Vida_del_Enemigo -= 5
                print(" > Golpe conectado por 5 de daño")
            break #para salir del menu
        else:
            if Pociones_de_Vida > 0:
                Pociones_de_Vida -= 1
                Vida_del_Gladiador += 30
            else:
                print("¡No quedan pociones! y pierdes el turno. ")
            break #para salir del menu
    Turno_Gladiador = False
    print("¡El enemigo contraataca por 12 puntos! ")
    Vida_del_Gladiador -= Daño_base_del_enemigo
    Turno_Gladiador = True #para volver a entrar al menu
if Vida_del_Enemigo <= 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print( "DERROTA. Has caído en combate." )