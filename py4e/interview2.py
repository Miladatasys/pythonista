def obtener_pares_0_a_50() :
    result = []
    for i in range(0, 51):
        if i % 2 == 0:
            result.append(i)
    return result