#______ function para leer vector _______
def leer():
    f = int(input("Tamanho filas="))
    c = int(input("Tamanho filas="))
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
    print("")
    for i in range(f):
        for j in range(c):
            print(M[i][j],end=",")
        print()
    print("]")
    
def mostrarPrincipalAsc(M, f,c):
    for i in range(f):
        for j in range(c-1):
            if(i==j):
                for  k in range(i,f):
                    if M[j]> M[k]:
                        aux=M[j]
                        print(aux)
                        M[j]=M[k]
                        M[k]=aux
    return M

#______ function main _______
f,c = leer()
print("Ingrese valores para llenar Matriz: ")
matriz = llenarMatriz(f,c)
print("_____Mostrar Original_____")
mostrar(matriz,f,c)
print("_____ Diagonal Princial y secundario_____")
mostrarPrincipalAsc(matriz, f,c)
mostrar(matriz,f,c)
#res=mostrarDesplazamiento(matriz,n)
#print("_____Mostrardesplazamiento_____")
#print(res)
