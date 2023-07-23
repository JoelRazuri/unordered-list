"""
     Escribir una función que reciba una lista desordenada y un elemento, que:
        a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de coincidencias encontradas.
        b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
        c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
        por parámetro y devuelva una lista con las posiciones.

"""


def busqueda(lista, elemento):

    contador = 0

    for item in lista:
        if item == elemento:
            contador += 1

    return contador


# print(busqueda([1,3,2,4,5,2,3,4,5,2,5,2,2], 1))

def primer_coincidencia(lista, elemento):

    for i in range(0,len(lista)):
        if lista[i] == elemento:
            posicion = i + 1
            break
        else:
            posicion = 'null'

    print(f"Lista: {lista}")
    print(f"\nPrimer aparición del valor '{elemento}' en la posición: {posicion}")

# primer_coincidencia([1,3,2,4,5,2,3,4,5,2,5,2,2], 3)


def coincidencias(lista, elemento):

    lista_coincidencias = []
    
    for i in range(0,len(lista)):
        if lista[i] == elemento:
            lista_coincidencias.append(i+1)

    print(f"Lista: {lista}\n")
    print(f"Lista de posiciones de coincidencias con el valor '{elemento}', {lista_coincidencias}")


# coincidencias([1,3,2,4,5,2,3,4,5,2,5,2,2], 2)