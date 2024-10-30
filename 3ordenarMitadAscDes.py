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


def rotarIzquierdaMitad(V, n):
    mitad = n // 2
    primero = V[0]  
   
    for i in range(mitad - 1):
        V[i] = V[i + 1]
    V[mitad - 1] = primero  

def rotarDerechaMitad(V, n):
    mitad = n // 2
    ultimo = V[n - 1]  
 
    for i in range(n - 1, mitad, -1):
        V[i] = V[i - 1]
    V[mitad] = ultimo 

#______ function para mostrar el desplazamiento _______
def mostrarDesplazamiento(V, n):
  
    rotarIzquierdaMitad(V, n)

    rotarDerechaMitad(V, n)

    return V

#______ function main _______
n = leer()
print("Ingrese valores para llenar el vector:")
vector = llenarVector(n)

print("_____Mostrar Original_____")
mostrar(vector, n)

# Aplicar el desplazamiento en ambas mitades
res = mostrarDesplazamiento(vector, n)
print("_____Mostrar Desplazamiento_____")
mostrar(res, n)



