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
	print("[")
	for i in range(f):
		for j in range(c):
			print(M[i][j],end=",")
		print()
	print("]")
	
def mostrarPrincipalSuperior(M, f,c):
    mayor=M[0][0]
    menor=M[0][c-1]
    for i in range(f):
        for j in range(c):
            if(i==j):
                if M[i][j]>mayor:
                    mayor=M[i][j]
            if i + j == c-1:           
                if M[i][j]<menor:
                    menor=M[i][j]

  
    print("Mayor  de la diagona principal es =",mayor)
    print("Menor  de la diagona secundaria es =",menor)

#______ function main _______
f,c = leer()
print("Ingrese valores para llenar Matriz: ")
matriz = llenarMatriz(f,c)
print("_____Mostrar Original_____")
mostrar(matriz,f,c)
print("_____ Diagonal Princial y secundario_____")
mostrarPrincipalSuperior(matriz, f,c)

