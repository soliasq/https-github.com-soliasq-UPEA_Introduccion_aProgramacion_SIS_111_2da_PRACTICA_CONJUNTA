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
def merge_sort(a):
    #n = len(a) NO LO USAREMOS ESTAMOS ENVIANDO COMO PARAMETRO
    
    # Caso base: si el arreglo tiene un solo elemento, ya está ordenado
    if n == 1:
        return a

    # Dividir el arreglo en dos mitades sin usar primitivas
    mitad = n // 2
    arrayOne = [0] * mitad  # Crear el primer sub-arreglo de tamaño mitad
    arrayTwo = [0] * (n - mitad)  # Crear el segundo sub-arreglo

    # Copiar elementos manualmente a arrayOne y arrayTwo
    for i in range(mitad):
        arrayOne[i] = a[i]
    
    for i in range(mitad, n):
        arrayTwo[i - mitad] = a[i]

    # Llamadas recursivas para ordenar cada mitad
    arrayOne = merge_sort(arrayOne)
    arrayTwo = merge_sort(arrayTwo)

    # Combinar (merge) las dos mitades ordenadas
    return merge(arrayOne, arrayTwo)

def merge(a, b):
    n = len(a) + len(b)
    c = [0] * n  # Crear un arreglo 'c' de tamaño suficiente para almacenar a y b combinados
    
    i = 0  # Índice para el arreglo `a`
    j = 0  # Índice para el arreglo `b`
    k = 0  # Índice para el arreglo `c`

    # Mientras ambos arreglos tengan elementos
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c[k] = b[j]
            j += 1
        else:
            c[k] = a[i]
            i += 1
        k += 1

    # Copiar los elementos restantes de `a`, si los hay
    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de `b`, si los hay
    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1

    return c


#______ function main _______
n = leer()
print("Ingrese valores para llenar el vector:")
vector = llenarVector(n)

print("_____Mostrar Original_____")
mostrar(vector, n)
#______ show function merge _______
print("_____ Mostrar Merge _____")
print(merge_sort(vector))

