print("Bienvenido al sistema de gestión de bicicletas")
capacidad_maxima = 25
bicis_disponibles = 25
viajes_activos = 0
ejecutando = True

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
        print("Opción no válida")
        continue

    if opcion == 1:
        print(f"\n[INFO] Cantidad actual de bicicletas disponibles: {bicis_disponibles}")
    elif opcion == 2:
        print(f"\n--- Arrendar bicicletas (Disponibles {bicis_disponibles})---")
        if bicis_disponibles == 0:
            print("Lo sentimos, no quedan bicicletas disponibles")
        else:
            try:
                cantidad_arrendar = int(input("¿Cuántas bicicletas deseas arrendar?: "))
                if cantidad_arrendar <= 0:
                    print("Error; la cantidad a arrendar debe ser mayor a 0")
                elif cantidad_arrendar > bicis_disponibles:
                    print(f"No hay suficientes bicicletas, puede arrendar hasta: {bicis_disponibles}")
                else:
                    bicis_disponibles -= cantidad_arrendar
                    viajes_activos += cantidad_arrendar
                    print(f"Arriendo exitoso, ha retirado {cantidad_arrendar} bicis")
            except ValueError:
                print("Error, debe ingresar un numero valido")
    elif opcion == 3:
        diferencia = capacidad_maxima-bicis_disponibles
        print(f"\n--- DEVOLVER BICICLETA (Espacio libre en estación: {diferencia})")
        try:
            cantidad_devolver = int(input("¿Cuántas bicicletas desea devolver?:"))
            if cantidad_devolver <= 0:
                print("Error, La cantidad a devolver debe ser mayor a 0")
            elif bicis_disponibles + cantidad_devolver > capacidad_maxima:
                print(f"Error, No hay capacidad para tantas bicicletas")
            else:
                bicis_disponibles += cantidad_devolver
                viajes_activos -= cantidad_devolver
                print(f"Devolución exitosa; ha regresado {cantidad_devolver} bicicletas")
        except ValueError:
            print("Error, debe ingresar un numero valido")
    elif opcion == 4:
        print(f"\n[HISTORIAL] Actualmente hay {viajes_activos} bicicleta(s) en uso por los usuarios")

