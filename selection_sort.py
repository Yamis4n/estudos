def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor = lista[i]
        posi = i
        for k in range(i+1, n):
            if lista[k] < menor:
                menor = lista[k]
                posi = k
                
        lista[posi] = lista[i]
        lista[i] = menor
    return lista

print(selection_sort([3,4,1,5,8,0,6]))    
            