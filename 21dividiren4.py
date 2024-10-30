#______ function para leer vector _______
def leer():
    n = int(input("Tamanho Matriz cuadrada="))

    return n

#______ function para generar vector _______
def llenarMatriz(f,c):
    M = [[0]*c for i in range(f)]
    return M

#______ function mostrar vector _______
def mostrar(M, f,c):
    print("[")
    for i in range(f):
        for j in range(c):
            print(M[i][j],end=" , ")
        print()
    print("]")
def generarMmatrizDividida(matriz,N):
    if N % 2 != 0:
        print("N debe ser un número par para dividir la matriz en cuadrantes iguales.")
        return  # Termina la función si N es impar
    
    #matriz = [[0] * N for _ in range(N)]
    contador = 1
    mitad = N // 2

    # Llenado del primer cuadrante (superior izquierdo) - primeros números
    for i in range(mitad):
        for j in range(mitad):
            matriz[i][j] = contador
            contador += 1

    # Llenado del tercer cuadrante (inferior derecho) - cuartos números
    for i in range(mitad, N):
        for j in range(mitad, N):
            matriz[i][j] = contador
            contador += 1

    # Llenado del segundo cuadrante (superior derecho) - terceros números
    for i in range(mitad):
        for j in range(mitad, N):
            matriz[i][j] = contador
            contador += 1

    # Llenado del cuarto cuadrante (inferior izquierdo) - segundos números
    for i in range(mitad, N):
        for j in range(mitad):
            matriz[i][j] = contador
            contador += 1

    # Imprimir la matriz
    for fila in matriz:
        print(fila)




#______ function main _______
c = leer()
f = c# puedes usar n se gustas  ya k esuna mtriz cuadrada
print("Generando  Matriz: ")
matriz = llenarMatriz(f,c)
print("_____Mostrar Original_____")
mostrar(matriz,f,c)
print("f_____ Mostrar Matriz dividida en 4 partes_____")
generarMmatrizDividida(matriz, c)
