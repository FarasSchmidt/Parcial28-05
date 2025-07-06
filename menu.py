from modulo import *

matriz = []
cargada = False

while True:
    print("MENU")
    print("1. Cargar matriz de notas")
    print("2. Mostrar porcentaje de aprobados por alumno")
    print("3. Mostrar mejor promedio")
    print("4. Buscar nota")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            while True:
                n_str = input("Ingrese la cantidad de alumnos: ")
                if n_str.isdigit() and int(n_str) > 0:
                    n = int(n_str)
                    break
                else:
                    print("Ingrese un número entero mayor a 0.")

            while True:
                m_str = input("Ingrese la cantidad de exámenes: ")
                if m_str.isdigit() and int(m_str) > 0:
                    m = int(m_str)
                    break
                else:
                    print("Ingrese un número entero mayor a 0.")

            matriz = cargar_matriz_notas(n, m)
            cargada = True

        case "2":
            if cargada:
                resultados = porcentaje_aprobados(matriz)
                for alumno, aprobados, total, porcentaje in resultados:
                    print(f"El alumno {alumno + 1} tiene {aprobados} examenes aprobados de {total} con un porcentaje de {porcentaje:.2f}%")
            else:
                print("Debe cargar primero la matriz.")

        case "3":
            if cargada:
                indice, promedio = mejor_promedio(matriz)
                print(f"El alumno {indice + 1} tiene el mejor promedio con {promedio:.2f}")
            else:
                print("Debe cargar primero la matriz.")

        case "4":
            if cargada:
                while True:
                    nota_str = input("Ingrese la nota a buscar (1-10): ")
                    if nota_str.isdigit():
                        nota = int(nota_str)
                        if 1 <= nota <= 10:
                            break
                        else:
                            print("La nota debe ser entre 1 y 10.")
                    else:
                        print("Entrada inválida. Debe ingresar un número entero.")

                posiciones = buscar_nota(matriz, nota)

                if len(posiciones) > 0:
                    for posicion in posiciones:
                        print("Nota encontrada en fila", posicion[0] + 1, ", columna", posicion[1] + 1)
                else:
                    print("La nota no se encuentra en la matriz.")
            else:
                print("Debe cargar primero la matriz.")

        case "5":
            print("Saliendo del programa.")
            break

        case _:
            print("Opcion invalida intente nuevamente.")