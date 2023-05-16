
# -----------------------------------------EL MÁS GRANDE DEL FUTBOL ARGENTINO------------------------------------------------------->

equipos_argentinos = [
    "River", "Boca", "Independiente", "Racing", "San Lorenzo", "Estudiantes", "Velez", "Huracan", "Newell's", "Rosario Central", 
    "Lanús", "Banfield", "Gimnasia", "Atletico Tucumán", "Colón", "Talleres", "Belgrano", "Central Cordoba", "Argentinos", "Chacarita"
]

print("¿Quién es más grande del fútbol Boca Juniors?")
print("Vamos a ver, ingrese los siguientes datos:")

intentos = 0
while intentos < 2:
    nombre = input("Ingrese su nombre: ")
    equipo = input("Ingrese su equipo, fanático: ").strip().capitalize()

    if equipo in equipos_argentinos:
        print("\nDe Boca Juniors:")
        try:
            boca_inter = int(input("Cantidad de Copas Intercontinentales: "))
            boca_nac = int(input("Cantidad de Copas Nacionales: "))
            boca_torneos = int(input("Cantidad de Torneos Nacionales: "))
            boca_desc = int(input("Cantidad de Descensos: "))
            boca_ganados = int(input(f"Cantidad de Partidos Ganados contra {equipo}: "))

            print(f"\nDe {equipo}:")
            try:
                equipo_inter = int(input("Cantidad de Copas Intercontinentales: "))
                equipo_nac = int(input("Cantidad de Copas Nacionales: "))
                equipo_torneos = int(input("Cantidad de Torneos Nacionales: "))
                equipo_desc = int(input("Cantidad de Descensos: "))
                equipo_ganados = int(input("Cantidad de Partidos Ganados contra Boca Juniors: "))

                puntaje_boca = boca_inter * 10 + boca_nac * 5 + boca_torneos * 3 - boca_desc * 5 + boca_ganados * 2
                puntaje_equipo = equipo_inter * 10 + equipo_nac * 5 + equipo_torneos * 3 - equipo_desc * 5 + equipo_ganados * 2

                if puntaje_boca > puntaje_equipo:
                    print("\n¡Boca Juniors es el equipo más grande, se acabó la mentira!")
                elif puntaje_equipo > puntaje_boca:
                    print(f"{equipo} es el equipo más grande, ya quisieras!")
                else:
                    print("\n¡Los dos equipos son igual de grandes, pero no es así, todos sabemos que es Boquita jrs!")
                break
            except ValueError:
                print("Pusiste un número en vez de tu equipo. ¡Vamos de nuevo, fanático!")
        except ValueError:
            print("Pusiste un número en vez de un nombre. ¡Vamos de nuevo!")
    else:
        intentos += 1
        if intentos < 2:
            print("Tu equipo está mal escrito. Inténtelo otra vez.")
        else:
            print("Tu equipo está muerto, o está descendido o juega en otro país no es campeón mundialista.")

# -----------------------------------------------------------------------------

# equipos_argentinos = [
#     "River", "Boca", "Independiente", "Racing", "San Lorenzo", "Estudiantes", "Velez", "Huracan", "Newell's", "Rosario Central", 
#     "Lanús", "Banfield", "Gimnasia", "Atletico Tucumán", "Colón", "Talleres", "Belgrano", "Central Cordoba", "Argentinos", "Chacarita"
# ]

# print("¿Quién es más grande del fútbol Boca Juniors?")
# print("Vamos a ver, ingrese los siguientes datos:")

# intentos = 0
# while intentos < 2:
#     nombre = input("Ingrese su nombre: ")
#     equipo = input("Ingrese su equipo, fanático: ").strip().capitalize()

#     if equipo in equipos_argentinos:
#         print("\nDe Boca Juniors:")
#         try:
#             boca_inter, boca_nac, boca_torneos, boca_desc, boca_ganados = [
#                 int(input(f"Cantidad de {attr}: ")) for attr in ["Copas Intercontinentales", "Copas Nacionales", "Torneos Nacionales", "Descensos", f"Partidos Ganados contra {equipo}"]
#             ]

#             print(f"\nDe {equipo}:")
#             try:
#                 equipo_inter, equipo_nac, equipo_torneos, equipo_desc, equipo_ganados = [
#                     int(input(f"Cantidad de {attr}: ")) for attr in ["Copas Intercontinentales", "Copas Nacionales", "Torneos Nacionales", "Descensos", "Partidos Ganados contra Boca Juniors"]
#                 ]

#                 puntaje_boca = boca_inter * 10 + boca_nac * 5 + boca_torneos * 3 - boca_desc * 5 + boca_ganados * 2
#                 puntaje_equipo = equipo_inter * 10 + equipo_nac * 5 + equipo_torneos * 3 - equipo_desc * 5 + equipo_ganados * 2

#                 if puntaje_boca > puntaje_equipo:
#                     print("\n¡Boca Juniors es el equipo más grande, se acabó la mentira!")
#                 elif puntaje_equipo > puntaje_boca:
#                     print(f"{equipo} es el equipo más grande, ya quisieras!")
#                 else:
#                     print("\n¡Los dos equipos son igual de grandes, pero no es así, todos sabemos que es Boquita jrs!")
#                 break
#             except ValueError:
#                 print("Pusiste un número en vez de tu equipo. ¡Vamos de nuevo, fanático!")
#         except ValueError:
#             print("Pusiste un número en vez de un nombre. ¡Vamos de nuevo!")
#     else:
#         intentos += 1
#         if intentos < 2:
#             print("Tu equipo está mal escrito. Inténtelo otra vez.")
#         else:
#             print("Tu equipo está muerto, o está descendido o juega en otro país no es campeón mundialista.")

