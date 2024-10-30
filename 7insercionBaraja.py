#______ function para leer vector _______
def leer():
    tam = int(input("Tamanho Vector="))
    return tam

#______ function para generar vector _______
def llenarVector(tamanho):
	V = [0]*n
	for i in range(n):
		x=int(input(f"{[i]}="))
		V[i]=x
	return V
#______ function mostrar vector _______
def mostrar(V, n):
	print("[",end="")
	for i in range(n):
		print(V[i],end=",")
	print("]")
	
def insercion(V,n):
	for i in range(1,n):
		e = V[i]
		k = i - 1
		while(k>=0 and e < V[k]):
			V[k+1]=V[k]
			k = k-1
		V[k+1] = e

	return V
# ___________funcion main________
n = leer()
print("Ingrese valores para llenar el vector: ")
vector = llenarVector(n)
print("_____Vector original_____")
mostrar(vector,n)
print("_____metod de insercion_____")
print(insercion(vector,n))


