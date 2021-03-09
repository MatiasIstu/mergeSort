def mergeSort(lista1,lista2,listaOrdenada):
    # Las dos listas ya estan ordenadas. Lo unico que hay que hacer es ir metiendo 
    # los elementos ordenadamente en la lista nueva. El primer paso del mergesort ya esta hecho. 

    # Para implementar el mergesort, voy a necesitar definir un indice para cada lista
    x = 0
    y = 0

    while x < len(lista1) and y < len(lista2):
        #Si la cadena que esta en lista1[x] va antes que la que esta en lista2[y] 
        #Entonces
        if lista1[x] < lista2[y]:
            listaOrdenada.append(lista1[x])
            x+=1

        else:
            listaOrdenada.append(lista2[y])
            y+=1
        # Paso a la siguiente posicion de la lista ordenada
       

    # Dependiendo del tamaño de las listas, puede que sobren valores en alguna de las dos

    while x < len(lista1):
        listaOrdenada.append(lista1[x])
        x+=1 

    while y < len(lista2):
        listaOrdenada.append(lista2[y])
        y+=1
     

lista1 = ['Cristiano', 'Drogba', 'Kaka', 'Leo', 'Lukaku']
lista2 = ['Armani', 'Bebeto', 'Mascherano', 'Rojo']

listaOrdenada = []
mergeSort(lista1,lista2,listaOrdenada)
print(listaOrdenada)


