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

def burbuja(lista:list[int]):
    cant_elementos =len(lista) #devuelve el numero de elementos de la lista

    for i in range(cant_elementos):       
        for j in range(cant_elementos): 
            if lista[j] > lista[i]:
               # 5       >     1
                aux = lista[j] # 5
                lista[j]= lista[i] #1
                lista[i]= aux #5
            print(lista) 

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
    if numero==1 or numero == 0:
        return [0]
  
    lista_nueva= [0,1]

    for i in range(2, numero):
        lista_nueva.append(lista_nueva[-1]+ lista_nueva[-2])

    return lista_nueva    

lista_numeros = [5,1,14,46,7,10]   
numero_ejemplo= 5
numero_ejemplo_2=1    
numero_ejemplo_3=0 

print(ordenar_list(lista_numeros))
#print(factorial(numero_ejemplo))
#print(serie_de_fibonacci(numero_ejemplo))
#print(serie_de_fibonacci(numero_ejemplo_2))
#print(serie_de_fibonacci(numero_ejemplo_3))
#burbuja(lista_numeros)