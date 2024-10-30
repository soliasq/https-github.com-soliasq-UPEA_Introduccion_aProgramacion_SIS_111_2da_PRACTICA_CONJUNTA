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
    
def leerFila():
    print("__________Fila  a Ordenar___________")
    d = int(input("# de Fila = "))
    return d
def matrizZ(matriz, size):
    for i in range(size):
        for j in range(size):
            if j <= i:  # Solo llenar la parte diagonal y hacia la izquierda
                matriz[i][j] = 5 - (i - j)  # Calcular el valor a asignar

    return matriz


#______ function main _______
c = leer()
f = c# puedes usar n se gustas  ya k esuna mtriz cuadrada
print("Generando  Matriz: ")
matriz = llenarMatriz(f,c)
print("_____Mostrar Original_____")
mostrar(matriz,f,c)
print("f_____ Mostrar Matriz Z_____")
matrizZ(matriz, c)
mostrar(matriz,f,c)




