# NOTA  yo usare len para tamanho en el ejercio 
# n=len(V) usamos para leer el tamanho de vector ud puede usar usar n
#________funtion read _________
def leer():
    tam =int(input("Tamanho de Vector="))
    return tam

#________funtion llenar vector_________

def llenar(n):
    V=[0]*n
    print("________Llenar Vector__________")
    for i in range(n):
       
        V[i] = int(input(f"{[i]}="))
    return V
#________funtion mostrar matriz_________
def mostrar(V,n):
    print("[",end=" ")
    for i in range(n):
      print(V[i], end=" ") 
    print("]")
    return V

#________funtion  Merge sort_________

def mergeSort(V):
    if(len(V)==1):
        return V # metodo ya esta ordenado
    else:
        dividirDos = len(V)//2# puedes usar n//2  Tu
        sub=(b,c)
        #llamanos a la funcones  merge
        sortedArray=merge(mergeSort(b), mergeSort(c))
#________funtion  Merge_________
#________funtion Main_________
n=leer()
vector=llenar(n)
print("__________Vector Original_________")
mostrar(vector,n)
print("__________Metodo Merge sort_________")
