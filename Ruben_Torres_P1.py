herramientas = []
existencias = []
menu = 0
encontrado =  False
while menu != 8:
    print("1. Carga Inicial de Herramientas: ")
    print("2. Carga de Existencias: ")
    print("3. Visualización de Inventario: ")
    print("4. Consulta de Stock (existencias): ")
    print("5. Reporte de Agotados: ")
    print("6. Alta de Nuevo Producto: ")
    print("7. Actualización de Stock (Venta/Ingreso): ")
    print("8. Salir: ")
    menu = int(input("Elija la accion deseada.  "))
    if menu == 1:
        cantidad = int(input("Ingrese la cantidad de herramientas que desea ingresar: "))
        if cantidad > 0:
            for i in range(cantidad):
                articulo = input("Ingrese el nombre de la herramienta: ").lower()
                while True:
                    if len(articulo) <=1:
                        print("Error, nombre invalido . ")
                        articulo = input("Ingrese el nombre de la herramienta: ").lower()
                    elif articulo in herramientas:
                        print("Error, articulo duplicado. ")
                        articulo = input("Ingrese el nombre de la herramienta: ").lower()
                    else:
                        herramientas.append(articulo)
                        break
            print(herramientas)
        else:
            print("Error, tiene que ingresar al menos 1 en la cantidad de herramientas. ")
    if menu == 2:
        existencias = []
        if len(herramientas) > 0:
            for i in range(len(herramientas)):
                print(f"herramienta : {herramientas[i]}")
                unidades = input("Ingrese la cantidad de existencias de la herramienta mencionada: ")
                while not unidades.isdigit():
                    print("Error! por favor ingrese un numero valido. ")
                    unidades = input("Ingrese la cantidad de existencias de la herramienta mencionada: ")
                unidades = int(unidades)
                while unidades < 0:
                    print("Error, Ingrese un numero de existencia de 0 o mayor. ")
                    unidades = int(input("Ingrese la cantidad de existencias de la herramienta mencionada: "))
                existencias.append(unidades)
        else:
            print("Error! no hay herramientas cargadas, elija la opcion uno y cargue para poder cargas las existencias. ")
    if menu == 3:
        if len(herramientas) > 0 and len(herramientas) == len(existencias):
            for i in range(len(herramientas)):
                print(f"Herramienta: {herramientas[i]} - existencias: {existencias[i]}")
        else:
            print("Error, no hay herramientas y/o existencias .")
    if menu == 4:
        buscar = input("Ingrese la herramienta que desea buscar: ")
        if len(herramientas) > 0 and len(existencias) > 0:
            encontrado = False
            for i in range(len(herramientas)):
                if herramientas[i] == buscar.lower():
                    encontrado = True
                    print(f"herramienta: {herramientas[i]} existencias: {existencias[i]}.")
            if not encontrado:    
                print(f"Herramienta no encontrada. ")
        else:
            print("Herramienta no encontrada.")
    if menu == 5:
        agotados = []
        if len(herramientas) > 0:
            for i in range(len(herramientas)):
                if existencias[i] == 0:
                   agotados.append(herramientas[i])
            if len(agotados) > 0:
                print(f"Los siguientes productos estan agotados: {agotados}")
            else:
                print("Todavia queda stock en todas las herramientas. ")
        else:
            print("Error, No hay herramientas cargadas. ")
    if menu == 6:
        if len(herramientas) > 0:
            nueva_herramienta = input("Ingrese el nombre de la nueva herramienta: ")
            while not nueva_herramienta.isalpha():
                print("Error, ingrese letras. ")
                nueva_herramienta = input("Ingrese un nombre de herramienta valido por favor. ")
            encontrado = False       
            for i in range(len(herramientas)):
                if herramientas[i] == nueva_herramienta:
                    encontrado = True
            if encontrado:
                print("Error, herramienta existente. ")
            else:
                cantidad = input("Ingrese la cantidad de existencias")
                while not cantidad.isdigit():
                    print("Error, no es un digito. ")
                    cantidad = input("Ingrese la cantidad de existencias")
                cantidad = int(cantidad)
                while cantidad < 0:
                    print("Error, no pueden ser numeros negativos. ")
                    cantidad = int(input("Ingrese la cantidad de existencias"))
                herramientas.append(nueva_herramienta)
                existencias.append(cantidad)
                print("Felicidades! se agrego el producto nuevo. ")
        else:
            print("Error, No hay herramientas cargadas. ")   
    if menu == 7:
        if len(herramientas) > 0 and len(existencias) > 0:
            opcion = input("Desea ingresar una venta? o un ingreso? presione v(ventas) o i(ingresos): ")
            opcion = opcion.lower()
            buscar = False
            while opcion != "v" and opcion != "i":
                print("Error, opcion incorrecta, presione v o i ...")
                opcion = input("Desea ingresar una venta? o un ingreso? presione v(ventas) o i(ingresos): ").lower()
            articulo = input("Ingrese el nombre de la herramienta: ")
            articulo = articulo.lower()
            for i in range(len(herramientas)):
                if herramientas[i] == articulo:
                    stock = i
                    buscar = True
                    break
            if buscar:
                print("Herramienta encontrada")
                print(f"herramienta: {herramientas[stock]} - existencia actual: {existencias[stock]}")
                if opcion == "i":
                    ingreso = int(input("Ingrese la cantidad de stock que desea sumar: "))
                    if ingreso > 0:                            
                        existencias[stock] += ingreso
                        print(f"Ingreso actualizado herramienta:{herramientas[stock]} nuevo stock: {existencias[stock]}")
                    else:
                        print("El ingreso debe ser mayor a 0")
                elif opcion == "v":
                    cant_ventas = int(input("Ingrese las ventas. "))
                    if existencias[stock] >= cant_ventas:
                            existencias[stock] = existencias[stock] - cant_ventas
                            print(f"Stock actualizado herramienta: {herramientas[stock]} stock actualizado: {existencias[stock]} ")
                    else:
                        print("Error, la existencia no puede menor a 0. ")
            else:
                print("Error, La herramienta no existe en el catalogo. ")
        else:
            print("Error, no hay herramientas cargadas.")
    if menu == 8:
        print("Saliendo ...")

