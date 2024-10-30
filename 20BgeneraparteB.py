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
    
def generateMatrix(matrix,n):

    
    for j in range(n):
        matrix[0][j] = j + 1

    num = n + 1  # Comenzar la numeración después de n

    for i in range(1, n - 1):
        for j in range(n):
            if j < n - 1 - i:
                matrix[i][j] = 1
            elif j == n - 1 - i:
                matrix[i][j] = num
                num += 1
            else:
                matrix[i][j] = 3

    for j in range(n):
        if j < n - 1:
            matrix[n - 1][j] = num
            num += 1
        else:
            matrix[n - 1][j] = num  # Cambiar a `num` en lugar de 3 para el último elemento

    return matrix




#______ function main _______
c = leer()
f = c# puedes usar n se gustas  ya k esuna mtriz cuadrada
print("Generando  Matriz: ")
matriz = llenarMatriz(f,c)
print("_____Mostrar Original_____")
mostrar(matriz,f,c)
print("f_____ Mostrar Matriz Z_____")
generateMatrix(matriz, c)
mostrar(matriz,f,c)

