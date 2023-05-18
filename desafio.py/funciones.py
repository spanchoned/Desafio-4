# ------------------------------Grupo 4---------------------------------------------------------



def agregar_inmueble(lista, inmueble):
    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("El inmueble se agregó correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación y no se puede agregar.")

def editar_inmueble(lista, indice, inmueble):
    if validar_inmueble(inmueble):
        if indice >= 0 and indice < len(lista):
            lista[indice] = inmueble
            print("El inmueble se editó correctamente.")
        else:
            print("El índice especificado está fuera de rango y no se puede editar.")
    else:
        print("El inmueble no cumple con las reglas de validación, no se puede editar.")

def eliminar_inmueble(lista, indice):
    if indice >= 0 and indice < len(lista):
        del lista[indice]
        print("El inmueble se eliminó correctamente.")
    else:
        print("El índice especificado está fuera de rango y no se puede eliminar el inmueble.")

def cambiar_estado_inmueble(lista, indice, nuevo_estado):
    if indice >= 0 and indice < len(lista):
        lista[indice]['estado'] = nuevo_estado
        print("El estado del inmueble se cambió correctamente.")
    else:
        print("El índice especificado está fuera de rango y no se puede cambiar el estado del inmueble.")

def buscar_inmuebles_por_presupuesto(lista, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista:
        if inmueble['estado'] in ['Disponible', 'Reservado']:
            precio = calcular_precio_inmueble(inmueble)
            if precio <= presupuesto:
                inmueble_con_precio = inmueble.copy()
                inmueble_con_precio['precio'] = precio
                inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados

def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    return True

def calcular_precio_inmueble(inmueble):
    zona = inmueble['zona']
    antiguedad = 2023 - inmueble['año']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = int(inmueble['garaje'])

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    
    return precio

def ingresar_inmueble():
    inmueble = {}
    inmueble['año'] = int(input("Ingrese el año del inmueble: "))
    inmueble['metros'] = int(input("Ingrese los metros cuadrados del inmueble: "))
    inmueble['habitaciones'] = int(input("Ingrese la cantidad de habitaciones del inmueble: "))
    inmueble['garaje'] = input("Ingrese si el inmueble tiene garaje (True/False): ").lower() == 'true'
    inmueble['zona'] = input("Ingrese la zona del inmueble (A, B o C): ").upper()
    inmueble['estado'] = input("Ingrese el estado del inmueble (Disponible, Reservado o Vendido): ").capitalize()
    return inmueble

def ingresar_presupuesto():
    presupuesto = float(input("Ingrese el presupuesto máximo: "))
    return presupuesto



def agregar_inmueble(lista, inmueble):
    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("El inmueble se agregó correctamente:")
        print("Año:", inmueble['año'])
        print("Metros cuadrados:", inmueble['metros'])
        print("Habitaciones:", inmueble['habitaciones'])
        print("Garaje:", inmueble['garaje'])
        print("Zona:", inmueble['zona'])
        print("Estado:", inmueble['estado'])
    else:
        print("El inmueble no cumple con las reglas de validación y no se puede agregar.")

def editar_inmueble(lista, indice, inmueble):
    if validar_inmueble(inmueble):
        if indice >= 0 and indice < len(lista):
            lista[indice] = inmueble
            print("El inmueble se editó correctamente:")
            print("Año:", inmueble['año'])
            print("Metros cuadrados:", inmueble['metros'])
            print("Habitaciones:", inmueble['habitaciones'])
            print("Garaje:", inmueble['garaje'])
            print("Zona:", inmueble['zona'])
            print("Estado:", inmueble['estado'])
        else:
            print("El índice especificado está fuera de rango y no se puede editar el inmueble.")
    else:
        print("El inmueble no cumple con las reglas de validación y no se puede editar.")

def eliminar_inmueble(lista, indice):
    if indice >= 0 and indice < len(lista):
        inmueble_eliminado = lista[indice]
        del lista[indice]
        print("El inmueble se eliminó correctamente:")
        print("Año:", inmueble_eliminado['año'])
        print("Metros cuadrados:", inmueble_eliminado['metros'])
        print("Habitaciones:", inmueble_eliminado['habitaciones'])
        print("Garaje:", inmueble_eliminado['garaje'])
        print("Zona:", inmueble_eliminado['zona'])
        print("Estado:", inmueble_eliminado['estado'])
    else:
        print("El índice especificado está fuera de rango y no se puede eliminar el inmueble.")

def cambiar_estado_inmueble(lista, indice, nuevo_estado):
    if indice >= 0 and indice < len(lista):
        inmueble = lista[indice]
        inmueble['estado'] = nuevo_estado
        print("El estado del inmueble se cambió correctamente:")
        print("Año:", inmueble['año'])
        print("Metros cuadrados:", inmueble['metros'])
        print("Habitaciones:", inmueble['habitaciones'])
        print("Garaje:", inmueble['garaje'])
        print("Zona:", inmueble['zona'])
        print("Estado:", inmueble['estado'])
    else:
        print("El índice especificado está fuera de rango y no se puede cambiar el estado del inmueble.")
