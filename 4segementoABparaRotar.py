#______ function para leer vector _______
def leer():
	tam = int(input("Tamanho Vector="))
	return tam
def leerDelimitador():
	print("______Delimitando del segmento a rotar_______")
	a = int(input("Delimitador inicial a="))
	b = int(input("Delimitador final b="))
	return a,b

#______ function para generar vector _______
def llenarVector(tamanho):
	V = [None]*n
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
# ___________delimitador  derecha____________	
def segmentoDilimitadorIzquierda(V,n):
	a,b=leerDelimitador()
	if a < 0 or b >= len(V) or a>=b: #len(V) cuenta tamno de fila pongale n si gusta
		print("Fuera de Limite")
		return V
	inicio=V[a]
	for i in range(a,b):
		V[i]=V[i+1]
	V[b]=inicio		
	return V
#_________Deloimitador derecha______________	
def segmentoDilimitadorDerecha(V,n):
	a,b=leerDelimitador()
	if a < 0 or b >= len(V) or a>=b: #len(V) cuenta tamno de fila pongale n si gusta
		print("Fuera de Limite")
		return V
	ultimo=V[b]
	for i in range(b,a-1):
		V[i]=V[i-1]
	V[a]=ultimo		
	return V
# ___________funcion main________
n = leer()
print("Ingrese valores para llenar el vector: ")
vector = llenarVector(n)
print("_____Vector original_____")
mostrar(vector,n)
print("_____Rotar Segemento_____")
print(segmentoDilimitadorDerecha(vector,n))


