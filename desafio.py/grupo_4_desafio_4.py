# ------------------------------Grupo 4--------------------------------------------------------



from funciones import agregar_inmueble, editar_inmueble, eliminar_inmueble, cambiar_estado_inmueble, buscar_inmuebles_por_presupuesto, validar_inmueble, calcular_precio_inmueble, ingresar_inmueble, ingresar_presupuesto, agregar_inmueble, editar_inmueble, eliminar_inmueble, cambiar_estado_inmueble



lista_inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
                   {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
                   {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
                   {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
                   {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

print("Bienvenido a la gestión de inmuebles.")

while True:
    print("\n¿Qué deseas realizar?")
    print("1. Agregar un inmueble")
    print("2. Editar un inmueble")
    print("3. Eliminar un inmueble")
    print("4. Cambiar el estado de un inmueble")
    print("5. Buscar inmuebles por presupuesto")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        nuevo_inmueble = ingresar_inmueble()
        agregar_inmueble(lista_inmuebles, nuevo_inmueble)
    elif opcion == '2':
        indice_editar = int(input("Contando del 0 hacía adelante, ingrese el índice para editar el inmueble: "))
        inmueble_editado = ingresar_inmueble()
        editar_inmueble(lista_inmuebles, indice_editar, inmueble_editado)
    elif opcion == '3':
        indice_eliminar = int(input("Contando del 0 hacía adelante, ingrese el índice para eliminar el inmueble: "))
        eliminar_inmueble(lista_inmuebles, indice_eliminar)
    elif opcion == '4':
        indice_cambiar_estado = int(input("Contando del 0 hacía adelante, ingrese el índice para cambiar el estado del inmueble: "))
        nuevo_estado = input("Ingrese el nuevo estado del inmueble: ").capitalize()
        cambiar_estado_inmueble(lista_inmuebles, indice_cambiar_estado, nuevo_estado)
    elif opcion == '5':
        presupuesto_busqueda = ingresar_presupuesto()
        inmuebles_encontrados = buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto_busqueda)
        print("Inmuebles encontrados:")
        for inmueble in inmuebles_encontrados:
            print(inmueble)
    elif opcion == '6':
        print("Muchas gracias por usar nuestro sistema de gestión de inmuebles!!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

