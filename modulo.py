def cargar_matriz_notas(n : int, m : int) -> list: #n = cantidad alumnos m = notas
    """
    Que hace?\n
    Carga datos a una matriz\n
    Que recibe?\n
    n(cantidad de alumnos)-> int m(cantidad de notas)-> int\n
    Que retorna?\n
    Una matriz 
    """
    matriz = []
    i = 0
    while i < n:
        fila = []
        j = 0
        print(f"Alumno {i+1}:")
        while j < m:
            while True:
                nota = input(f"Ingrese nota del examen {j+1} (entre 1 y 10): ")
                if nota.isdigit():
                    nota_entera = int(nota)
                    if 1 <= nota_entera <= 10:
                        fila.append(nota_entera)
                        break
                print("Error: la nota debe ser un numero entero entre 1 y 10.")
            j += 1
        matriz.append(fila)
        i += 1
    return matriz

matriz = cargar_matriz_notas(3, 2)
print(matriz)

def porcentaje_aprobados(matriz : list):
    """
    Que hace?\n
    Calcula y muestra el porcentaje de aprobados\n
    Que recibe?\n
    Una matriz con cantidad de alumnos y sus notas\n
    Que retorna?\n
    Hace un print con el alumno, cantidad de aprobados sobre el total y el porcentaje
    """
    i = 0
    while i < len(matriz):
        alumno = matriz[i]
        total_examenes = 0
        cantidad_examenes_aprobados = 0
        j = 0
        while j < len(alumno):
            nota = alumno[j]
            total_examenes += 1
            if nota >= 6:
                cantidad_examenes_aprobados += 1
            j += 1

        porcentaje = (cantidad_examenes_aprobados * 100) / total_examenes
        print(f"El alumno {i+1} tiene {cantidad_examenes_aprobados} examen/es aprobado/s de {total_examenes} examenes con un porcentaje de {porcentaje:.2f}%")
        i += 1

porcentaje_aprobados(matriz)