def filtrar_pares(numbers) :
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result

def filtrar_impares(numbers) :
    result = []
    for i in numbers:
        if i % 2 != 0:
            result.append(i)
    return result