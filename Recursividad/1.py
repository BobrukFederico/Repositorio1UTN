def calcular_potencia(base: int = 2, potencia: int = 2):
    if potencia == 0:
        return 1
    elif potencia == 1:
        return base
    else:
        return base * calcular_potencia(base, potencia-1)
    

print(calcular_potencia(4,3))