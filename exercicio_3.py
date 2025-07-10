lista = [*map (float, input ("Digite as suas notas: ").split(","))]

 
def calcular_media(lista):
    return sum(lista) / len(lista)

print (calcular_media (lista))
