
#______ function para leer vector _______
def leer():
	tam = int(input("Tamanho Vector="))
	return tam
def leerBuscar():
	print("Leer elemento a buscar")
	a = int(input("Valor ="))
	return a
#______ function para generar vector _______
def llenarVector(tamanho):
	V = [0]*n
	for i in range(n):
		x=int(input(f"[{i}]="))
		V[i]=x
	return V
#______ function mostrar vector _______
def mostrar(V, n):
	print("[",end="")
	for i in range(n):
		print(V[i],end=",")
	print("]")
#______ function kparametros ASc. _______
def buscaBinario(V):
	data = leerBuscar()# Elemento a buscar
	inicio=0
	fin=len(V)-1
	while inicio <= fin:
		mitad= (inicio + fin)//2 #obtenemos la mitad
		if  V[mitad]==data:
			buscar=V[mitad]
			#print(buscar)
			return mitad,buscar	 
		elif V[mitad]<data:
				inicio=mitad+1
		else:
			fin=mitad-1
	return -1				
				
	
	
#______ function ordenar _______
def ordenarVector(V,n):
	for i in range(n):
		for j in range(n-1):
			if V[j]>V[j+1]:
				aux = V[j]
				V[j]=V[j+1]
				V[j+1]=aux
	return V
#______ function main _______
n = leer()
print("___________________________________")
vector = llenarVector(n)
#vector=[3,5,4,2,8,2,1]
#print(vector.sort())
#n=len(vector)
print("_____Mostrar Vector Original_____")
mostrar(vector,n)
ordenarVector(vector,n)
resultado,valor = buscaBinario(vector)

if resultado != -1:
	print("___________________________________")
	print(f" El elemento es = {valor}  en la posicion = {resultado}")
		
else:
	print("___________________________________")
	print(f" No hay elemntos a mostrar")	

