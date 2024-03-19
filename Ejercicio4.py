def restar_polinomios(polinomio1, polinomio2):
    resultado = []

    for termino1 in polinomio1:
        coeficiente1, exponente1 = termino1
        encontrado = False

        for termino2 in polinomio2:
            coeficiente2, exponente2 = termino2
            if exponente1 == exponente2:
                resultado.append((coeficiente1 - coeficiente2, exponente1))
                encontrado = True
                break

        if not encontrado:
            resultado.append((coeficiente1, exponente1))

    for termino2 in polinomio2:
        coeficiente2, exponente2 = termino2
        encontrado = False

        for termino1 in polinomio1:
            coeficiente1, exponente1 = termino1
            if exponente1 == exponente2:
                encontrado = True
                break

        if not encontrado:
            resultado.append((-coeficiente2, exponente2))

    resultado = [(coef, exp) for coef, exp in resultado if coef != 0]
    resultado.sort(key=lambda x: x[1], reverse=True)
    return resultado


def dividir_polinomios(polinomio1, polinomio2):
    cociente = []
    resto = polinomio1.copy()

    while len(resto) > 0 and resto[0][1] >= polinomio2[0][1]:
        coeficiente_resto, exponente_resto = resto[0]
        coeficiente_divisor, exponente_divisor = polinomio2[0]

        cociente.append((coeficiente_resto / coeficiente_divisor, exponente_resto - exponente_divisor))

        resto = restar_polinomios(resto, [(coeficiente_resto / coeficiente_divisor * coef, exponente_resto - exponente_divisor) for coef, exponente in polinomio2])

    resto = [(coef, exp) for coef, exp in resto if coef != 0]
    cociente = [(coef, exp) for coef, exp in cociente if coef != 0]

    return cociente, resto


def eliminar_termino(polinomio, exponente):
    return [(coef, exp) for coef, exp in polinomio if exp != exponente]


def termino_existe(polinomio, exponente):
    return any(exp == exponente for _, exp in polinomio)


# Ejemplo de uso
polinomio1 = [(1, 7), (-1, 0), (6, 2)]  # 3x^2 - 5x + 4
polinomio2 = [(4, 9), (6, 3), (3, 1)]   # x^2 + 2x + 1

resultado_resta = restar_polinomios(polinomio1, polinomio2)
print("Resta de polinomios:", resultado_resta)

cociente, resto = dividir_polinomios(polinomio1, polinomio2)
print("División de polinomios:")
print("Cociente:", cociente)
print("Resto:", resto)

exponente_eliminar = 2
nuevo_polinomio = eliminar_termino(polinomio1, exponente_eliminar)
print(f"Polinomio después de eliminar término con exponente {exponente_eliminar}:", nuevo_polinomio)

exponente_buscado = 1
existe = termino_existe(polinomio1, exponente_buscado)
print(f"¿Existe término con exponente {exponente_buscado} en el polinomio? {existe}")