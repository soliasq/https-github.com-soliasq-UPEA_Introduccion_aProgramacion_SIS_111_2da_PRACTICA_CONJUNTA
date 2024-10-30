#______ function para leer vector _______
def leer():
    f = int(input("Tamanho filas="))
    c = int(input("Tamanho Columnas="))
    return f,c

#______ function para generar vector _______
def llenarMatriz(f,c):
    M = [[0]*c for i in range(f)]
    for i in range(f):
        for j in range(c):
            x=int(input(f"M[{i}][{j}]="))
            M[i][j]=x
    return M

#______ function mostrar vector _______
def mostrar(M, f,c):
    print("[")
    for i in range(f):
        for j in range(c):
            print(M[i][j],end=",")
        print()
    print("]")
    
def leerFila():
    print("__________Fila  a Ordenar___________")
    d = int(input("# de Fila = "))
    return d
def mostrarFilaAsc(M, f,c):
    x=leerFila()
    if x < 0 or x >= f:
        print("Número de fila no válido.")
        return M
    for i in range(c-1):
        for j in range(0,c-i-1):
            
            if M[x][j]> M[x][j+1]:
                aux=M[x][j]
                M[x][j]=M[x][j+1]
                M[x][j+1]=aux
            

    return M

#______ function main _______
f,c = leer()
print("Ingrese valores para llenar Matriz: ")
matriz = llenarMatriz(f,c)
print("_____Mostrar Original_____")
mostrar(matriz,f,c)
print("f_____ Diagonal fila  K={k}_____")
mostrarFilaAsc(matriz, f,c)
mostrar(matriz,f,c)

