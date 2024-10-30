#______ function para leer tamaño del vector _______
def leer():
    tam = int(input("Tamaño del vector = "))
    return tam

#______ function para generar vector _______
def llenarVector(tamanho):
    V = [0] * tamanho
    for i in range(tamanho):
        x = int(input(f"Elemento {i+1} = "))
        V[i] = x
    return V

#______ function para mostrar vector _______
def mostrar(V, n):
    print("[", end="")
    for i in range(n):
        print(V[i], end=", " if i < n - 1 else "")
    print("]")
def separacion(lista):
    if len(lista)<1:
         return []
    #else:
    #   return lista
    izquierda = []
    derecha = []
    pivote=lista[0]
    for i in range(1,len(lista)):
        if lista[i]<pivote:
            izquierda.append(lista[i])
        else:
            derecha.append (lista[i])
    #print(izquierda)
    #print(derecha)
    #print(pivote)
    return izquierda, pivote,derecha

def quickSortOr(lista):
    if len(lista) < 2:
        return lista
 
    izquierda, pivote, derecha = separacion(lista)
    return quickSortOr(izquierda) + [pivote] + quickSortOr(derecha)

#______ function main _______
n = leer()
print("Ingrese valores para llenar el vector:")
vector = llenarVector(n)

print("_____Mostrar Original_____")
mostrar(vector, n)
#______ show function merge _______
print("_____ Mostrar quickSort _____")
print(quickSortOr(vector))