listaElementos = [2, 4, 68, 3, 5856, 784, 38459, 787, 999999]

def obtenerMaximo(lista: list):
    if len(lista) > 0:
        max = lista[0]

        for num in lista:
            if num > max:
                max = num
        
        return max
    return -1

listaExample = [9999, 1, 1000000000]

def obtenerMinimo(lista: list):
    #si la lista tiene almenos un elemento
    if len(lista) > 0:
        #El minimo inicia con el valor del primer elemento de la lista
        min = lista[0]
        #Este ciclo pasa por cada elemento de la lista que tiene
        for num in lista:
            #  si el mayor que el minimo entonce el minimo es igual
            if num < min:
                min = num

        return min
    
    #de lo contrario retorna -1
    return -1

min = 5

def obtenerMinimoDeDosListas(lista1:list, lista2:list):

    #Verificar si las listas estan vacia
    if len(lista1) > 0 and len(lista2) > 0: #booleanosin 
        #El minimo inicia con el primer elemento
        min = lista1[0]
        #El ciclo va a recorrer la lista uno a uno elemento.
        for num in lista1:
            # si el numero es menor que el anterior
            if num < min:
                min = num

        #El ciclo va a recorrer la lista
        for num in lista2:
            if num < min:
                min = num

        return min
    
    return -1

def obtenerMaximoDeDosListas(lista1:list, lista2:list):

    #Verificar si las listas estan vacia
    if len(lista1) > 0 and len(lista2) > 0: #booleanosin 
        #El minimo inicia con el primer elemento
        min = lista1[0]
        #El ciclo va a recorrer la lista uno a uno elemento.
        for num in lista1:
            # si el numero es menor que el anterior
            if num > min:
                min = num

        #El ciclo va a recorrer la lista
        for num in lista2:
            if num > min:
                min = num

        return min
    
    return -1

print(obtenerMaximoDeDosListas(listaElementos, listaExample))