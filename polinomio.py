#encontra todas as raízes inteiras de um polinomio de fatores inteiros e constante maior que zero
#Equação:  X² - 3X -4  = 0
fatores = [1,-3,-4]


def raizes_inteiras(fatores):    
    raizes = []
    
    n = -abs(fatores[-1])
    while n <= abs(fatores[-1]):
        if n != 0 and fatores[-1] % n == 0:
            raizes.append(n)
        n += 1

    valor = 0
    raizes_encontradas = encontrar_raizes(raizes, fatores, 0)
    raizes_inteiras = []
    for i in range(len(raizes)):
        if raizes_encontradas[i] == 0:
            raizes_inteiras.append(raizes[i])
    return raizes_inteiras

    
def encontrar_raizes(raizes_possiveis, fatores, index):
    if index == len(fatores):
        return [0 for i in raizes_possiveis]

    possibilidades = encontrar_raizes(raizes_possiveis, fatores, index+1)
    for i in range(len(raizes_possiveis)):
        possibilidades[i] += fatores[index]
        possibilidades[i] /= raizes_possiveis[i]
    return possibilidades
    

print(raizes_inteiras(fatores))