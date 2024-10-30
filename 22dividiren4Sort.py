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

def burbuja(lista):
    n = len(lista)
    # Implementar el algoritmo de burbuja
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                
                temp = lista[j]         
                lista[j] = lista[j+1]   
                lista[j+1] = temp 

def dividirOrdenarMatriz(N, matriz):
    mitad = N // 2

    # Extraer elementos de cada cuadrante
    cuadrante1 = [matriz[i][j] for i in range(mitad) for j in range(mitad)]
    cuadrante2 = [matriz[i][j] for i in range(mitad) for j in range(mitad, N)]
    cuadrante3 = [matriz[i][j] for i in range(mitad, N) for j in range(mitad)]
    cuadrante4 = [matriz[i][j] for i in range(mitad, N) for j in range(mitad, N)]

    # Ordenar cada cuadrante usando el algoritmo de burbuja
    burbuja(cuadrante1)
    burbuja(cuadrante2)
    burbuja(cuadrante3)
    burbuja(cuadrante4)

    # Volver a colocar los elementos ordenados en la matriz
    index = 0
    for i in range(mitad):
        for j in range(mitad):
            matriz[i][j] = cuadrante1[index]
            index += 1

    index = 0
    for i in range(mitad):
        for j in range(mitad, N):
            matriz[i][j] = cuadrante2[index]
            index += 1

    index = 0
    for i in range(mitad, N):
        for j in range(mitad):
            matriz[i][j] = cuadrante3[index]
            index += 1

    index = 0
    for i in range(mitad, N):
        for j in range(mitad, N):
            matriz[i][j] = cuadrante4[index]
            index += 1

    # Imprimir la matriz resultante
    for fila in matriz:
        print(fila)


lista = [
    [6, 1, 3, 19, 24, 21],
    [8, 5, 2, 26, 23, 20],
    [7, 9, 4, 22, 27, 25],
    [28, 30, 33, 12, 11, 10],
    [32, 29, 35, 15, 14, 13],
    [31, 34, 36, 16, 18, 17]
]
#______ function main _______
c = leer()
f = c# puedes usar n se gustas  ya k esuna mtriz cuadrada

# aca solo llena de ceros la matriz
matriz = llenarMatriz(f,c)
matriz=lista
print("Generando  Matriz: ")
print("_____Mostrar Original_____")
mostrar(matriz,f,c)

print("_____ Mostrar Matriz dividida en 4 partes_____")
dividirOrdenarMatriz(f, matriz)
