
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
    i = 0 # Recorre alumnos
    while i < n:
        fila = []
        j = 0 # Recorre examenes
        print(f"Alumno {i+1}:")
        while j < m:
            while True:
                nota = input(f"Ingrese nota del examen {j+1} (entre 1 y 10): ")
                if nota.isdigit():
                    nota_entera = int(nota)
                    if 1 <= nota_entera <= 10:
                        fila.append(nota_entera)
                        break
                print("Error: la nota debe ser un numero entero entre 1 y 10")
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
            total_examenes += 1 # Acumulador cantidad examenes
            if nota >= 6:
                cantidad_examenes_aprobados += 1 # Acumulador cantidad aprobados
            j += 1

        # Calculos porcentaje de examenes aprobados
        porcentaje = (cantidad_examenes_aprobados * 100) / total_examenes
        indice_alumno =i+1 
        #print(f"El alumno {i+1} tiene {cantidad_examenes_aprobados} examen/es aprobado/s de {total_examenes} examenes con un porcentaje de {porcentaje:.2f}%")
        i += 1
        return indice_alumno, cantidad_examenes_aprobados, total_examenes, porcentaje

porcentaje_aprobados(matriz)

# 3. Acumulador de notas dividido en cantidad de notas, sacar mejor nota
# 4. Buscar nota especifica, guardo posiciones donde se encuentran en otra lista y la imprimo
# Completar el menu. Entrega el viernes

def mejor_promedio(matriz : list):
    """
    Que hace?\n
    Calcula el promedio de notas de cada alumno y determina cuál tiene el mejor promedio.\n
    Que recibe?\n
    Una matriz con las notas de los alumnos\n
    Que retorna?\n
    El indice del alumno con mejor promedio y el valor del promedio mas alto.
    """
    mejor_prom = 0  # Mejor promedio
    indice_mejor_prom = 0  # Indice 
    i = 0  # Recorre alumnos

    while i < len(matriz):
        alumno = matriz[i]
        acumulador_notas = 0
        cantidad_notas = 0
        j = 0
        while j < len(alumno):
            acumulador_notas += alumno[j]  # Acumulador notas
            cantidad_notas += 1
            j += 1
        
        # Calcular promedio del alumno
        promedio = acumulador_notas / cantidad_notas  

        if i == 0 or promedio > mejor_prom:  # Toma el primer alumno y lo compara
            mejor_prom = promedio
            indice_mejor_prom = i
        i += 1

    return indice_mejor_prom, mejor_prom

def buscar_nota(matriz, nota_buscada):
    """
    Que hace?\n
    Busca una nota.\n
    Que recibe?\n
    Una matriz con las notas de los alumnos y la nota a buscar\n
    Que retorna?\n
    Una lista con las posiciones en las que se encuentran las notas buscadas
    """
    posiciones = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == nota_buscada:
                posiciones.append((i, j))
    return posiciones