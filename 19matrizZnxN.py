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
def matrizZ(M, n):
    k=0
    for i in range(n):
        
        for j in range(n):
            if i==0:
                k=k+1 
                M[0][j]=k
            elif i+j==n-1:
                k=k+1
                M[i][j]=k
            
            if i==n-1:
                k=k+1
                M[n-1][j]=k
        
    


    return M

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


