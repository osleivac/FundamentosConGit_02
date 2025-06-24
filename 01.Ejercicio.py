"""
Crear un programa python con un menu, con tres opciones. 
1 Agregar alumnos a una lista de alumnos, 
2. mostrar todos los alumnos, 
3 cerrar. El programa debe pedir el nombre del alumno.

"""
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Cerrar")

def agregar_alumno(lista_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    lista_alumnos.append({"nombre": nombre})
    print(f"Alumno '{nombre}' agregado correctamente.")



