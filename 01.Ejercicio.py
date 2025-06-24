"""
Crear un programa python con un menu, con tres opciones. 
1 Agregar alumnos a una lista de alumnos, 
2. mostrar todos los alumnos, 
3 cerrar. El programa debe pedir el nombre del alumno.

"""
# Lista para guardar alumnos
lista_alumnos = []

# Bandera del menú
activo = True

while activo:
    print("\n--- Menú de Alumnos ---")
    print("[1] Agregar alumno")
    print("[2] Mostrar todos los alumnos")
    print("[3] Cerrar")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ")
        lista_alumnos.append(nombre)
        print("Alumno agregado correctamente.")

    elif opcion == "2":
        print("\nLista de alumnos:")
        for alumno in lista_alumnos:
            print(f"- {alumno}")

    elif opcion == "3":
        print("Programa finalizado.")
        activo = False

    else:
        print("Opción no válida.")


