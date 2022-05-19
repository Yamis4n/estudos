def insertion_sort(lista):
    n = len(lista)
    for i in range(n-1):
        compar = lista[i+1]
        index = i+1
        k = i
        while compar < lista[k] and k >= 0:
                lista[k+1] = lista[k]
                index = k
                k -=1
        lista[index] = compar
        print(lista)
    return lista

def main():
    lista = [2,34,5,1,6,78,4,20,23,45,32,50]
    insertion_sort(lista)
main()