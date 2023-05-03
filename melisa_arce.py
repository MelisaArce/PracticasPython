def ordenar_list(lista:list[int])-> list[int]:
    """
    Toma una lista por parametros y la devuelve ordenada con el algoritmo de burbuja.
    """
    cant_elementos =len(lista) #devuelve el numero de elementos de la lista

    for i in range(cant_elementos-1):       
        for j in range(cant_elementos-1-i): 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

def factorial(numero:int)-> int:
    """
    Toma un numero y calcula el factorial de ese numero
    """
   
    multiplicador= 1  

    for i in range (1,numero+1):
        multiplicador = multiplicador * i

    return multiplicador
      
def serie_de_fibonacci(numero:int)->list[int]:
    """
    Toma un numero y devuelve una lista con la serie fibonacci
    """
    if numero==1:
        return [0]
    
    lista_nueva= [0,1]

    for i in range(2, numero):
        lista_nueva.append(lista_nueva[-1]+ lista_nueva[-2])

    return lista_nueva                   

