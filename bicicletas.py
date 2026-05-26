print("Bienvenido al sistema de gestión de bicicletas")
capacidad_maxima = 25
bicis_disponibles = 25
viajes_activos = 0
ejecutando = True
#ciclo Principal
while ejecutando:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Bicicletas disponibles")
    print("2. Arrendar bicicletas (Salida)")
    print("3. Devolver bicicletas (Entrada)")
    print("4. Historial de viajes activos")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Opción no válida, por favor, ingrese un número entre 1 y 5")
        continue
    #opción 1 Bicis disponibles
    if opcion == 1:
        print(f"\n[INFO] Cantidad actual de bicicletas disponibles: {bicis_disponibles}")
    #Opción 2 Arrendar bicicletas
    elif opcion == 2:
        print(f"\n--- Arrendar bicicletas (Disponibles: {bicis_disponibles})---")
        if bicis_disponibles == 0:
            print("Lo sentimos, no quedan bicicletas disponibles")
        else:
            try:
                cantidad_a_arrendar = int(input("¿Cuántas bicicletas desea arrendar?: "))
                if cantidad_a_arrendar <= 0:
                    print("Error: la cantidad a arrendar debe ser mayor a 0")
                elif cantidad_a_arrendar > bicis_disponibles:
                    print(f"No hay suficientes bicletas, puede arrendar hasta: {bicis_disponibles}")
                else:
                    bicis_disponibles -= cantidad_a_arrendar
                    viajes_activos += cantidad_a_arrendar
                    print(f"Arriendo exitoso, ha retirado {cantidad_a_arrendar} bicis")
            except ValueError:
                print("Error, debe ingresar un númento entero")
    #opcion 3 -Devolver bicicleta
    elif opcion == 3:
        diferencia = capacidad_maxima-bicis_disponibles
        print(f"\n--- DEVOLVER BICICLETA (espacio libre en estación: {diferencia})")
        try:
            cantidad_a_devolver = int(input("¿Cuántas bicicletas desea devolver?:"))
            if cantidad_a_devolver <= 0:
                print("Error: La cantidad a devolver debe ser mayor a 0")
            elif bicis_disponibles + cantidad_a_devolver > capacidad_maxima:
                print(f"Error: No se pueden devolver tantas bicicletas, supera capacidad maxima de 25 bicis")
            else:
                bicis_disponibles += cantidad_a_devolver
                viajes_activos -= cantidad_a_devolver
                print(f"Devolución exitosa ha regresado {cantidad_a_devolver} bicicletas")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")