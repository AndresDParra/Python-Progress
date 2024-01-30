# script que genere un array de enteros aleatorios retorne el mayor de ello, imprimir

def Cual_es_el_mayor():

    arreglo = [32,2,35460,4,5,2000,7,8,1,2]
    maximo = arreglo[0]
    for i in arreglo:
        if i > maximo:
            maximo = i
    return maximo

print(Cual_es_el_mayor())

#Ordenar todos los elementos de un arreglo de menor a mayor
