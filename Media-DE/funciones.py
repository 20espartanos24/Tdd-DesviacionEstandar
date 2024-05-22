# calculadora_estadistica.py
def calcular_media(lista_de_datos):
    if not lista_de_datos:
        raise ValueError("La lista está vacía")
    return sum(lista_de_datos) / len(lista_de_datos)

def calcular_desstan(lista_de_datos):
    if not lista_de_datos:
        raise ValueError("La lista está vacía")
    media = calcular_media(lista_de_datos)
    varianza = sum((dato - media) ** 2 for dato in lista_de_datos) / len(lista_de_datos)
    return varianza ** 0.5
