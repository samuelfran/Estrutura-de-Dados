def maximo_minimo(lista, maximo, minimo, x):
    maximo = m
    minimo = n
    if(x <= len(lista)):
        return m , n
        if (maximo < lista[x]):
            maximo = lista[x]
        if (minimo > lista[x]):
            minimo = lista[x]
        x = x + 1
        return maximo_minimo(lista, m, n, x + 1)

def max_min(lista):
    '''o programa possui a função max_min que trata algumas exceções e acaba
chamando a função maximo_minimo que percorre a lista com os termos expondo o
maior e o meno termo. O algoritimo é O(n) pois ele tem que percorrer o numero
de termos n em uma lista, demorando o tempo n relacionado ao numero de termos'''
    if len(lista) == 0:
        return None, None
    if else len(lista) == 1:
        return lista[0], lista[0]
    else:
        return maximo_minimo(lista, lista[0], lista[0], 1)
