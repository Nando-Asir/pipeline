jugador = {}
enfermeria = ["Rocha","Batres","Cupillar"]
while True:
    print("1.- Anotar goles")
    print("2.- Consultar jugador")
    print("3.- Informe del equipo")
    print("4.- Salir")
    opcion= int(input("Introduce una opcion (1-3) o (4 para salir): "))
    if opcion == 1:
        try:
            nombre= input("Ingresa nombre del jugador: ").capitalize()
            goles= int(input("Ingresa número de goles: "))
            if nombre not in enfermeria:
                jugador[nombre]= goles
                print(f"El jugador {nombre} ha anotado {goles} goles.")
            else:
                print(f"El jugador {nombre} está en la enfermería.")
        except ValueError:
            print("El número debe ser entero")
    elif opcion == 2:
        buscar = input("¿Que jugador quiere consultar?: ").capitalize()
        if buscar in jugador:
            print(f"El jugador {buscar} ha marcado {jugador[buscar]} goles.")
        else:
            print(f"El jugador {buscar} no se encuentra en el diccionario.")
    elif opcion == 3:
        total = 0
        suma_goles= sum(jugador.values())
        print("Informe del equipo:")
        for jugador, goles in jugador.items():
            print(f"{jugador} ha marcado {goles} goles")
        print(f"El equipo ha marcado un total de: {suma_goles}")
    elif opcion == 4:
        print("Salimos del programa.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 3 o el 4 para salir.")