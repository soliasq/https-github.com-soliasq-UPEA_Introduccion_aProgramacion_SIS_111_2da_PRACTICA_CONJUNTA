def dimension():
    n=int(input("ingrese la dimension del vector:"))
    return n


def llenar(n):
    v=[0]*n
    for i in range(n):
        v[i]=int(input(f"V{[i]}= "))
    return v        

def mostrar(v,n):
    for i in range(n):
        print(v[i], end=" ")

def seleccion(v,n):
    for k in range(n):
        menor=v[k]
        M=k
        for j in range(k+2,n):
            if v[j]<menor:
                menor=v[j]
                M=j
        
        v[M]=v[k]
        v[k]=menor
    return v
        
             
n=dimension()
vector=llenar(n)
print("_____Mostrar Vector Original_____")
mostrar(vector,n)
print()
print("_________Metodo  Seleccion_________")
print(seleccion(vector,n))
