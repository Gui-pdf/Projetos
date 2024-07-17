import random

def minesweeper(h,v,desafio = 5):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    

    def gerardificuldade(n):
        dif = []
        for i in range(n):
            dif.append(0)
        dif.append(1)
        return dif


    def geratriz(i,j,blank = False):
        r = random.choice(dificuldade)
        if blank == True:
            return('■')
        return(r)


    def gerarmatriz(x,y,blank = False):
        matriz = [[geratriz(i,j,blank) for i in range(x)] for j in range(y)]
        return matriz


    def detectar(i,j,bombas):
        bombastotal = 0

        if bombas[j][i] == 1:
            return('X')
        
        else:
            for y in range(-1,2):
                for x in range(-1,2):
                    try:
                        if bombas[j+y][i+x] == 1 and i+x >= 0 and j+y >=0:
                            bombastotal += 1
                    except:
                        continue
        return str(bombastotal)
                        



    def campominado(bombas):
        matriz = []
        for j in range(len(bombas)):
            linha = []
            for i in range(len(bombas[0])):
                linha.append(detectar(i,j,bombas))
            matriz.append(linha)
        return matriz


    def printfinal(matriz):
        print('  ', end='')
        [print(i,end=' ') for i in range(len(matriz[0]))]
        print('')
        count = 0
        for j in matriz:
            print(alfabeto[count] , end=' ')
            for i in j:
                print(i, end=' ')
            print('')
            count += 1
        print('')

    def revelar(i, j):
        if matrizbombas[j][i] != 'V':
            matrizjogo[j][i] = matrizfinal[j][i]
            if matrizbombas[j][i] != 1:
                matrizbombas[j][i] = 'V'

            if matrizjogo[j][i] == '0':
                    for y in range(-1,2):
                        for x in range(-1,2):
                            try:
                                if (i+x) >= 0 and (j+y) >= 0:
                                    revelar(i+x,j+y)
                            except:
                                continue
        
        
        

    def tratar(resposta):
        r1 = resposta[0]
        r2 = resposta[1]

        if r1 in alfabeto:
            j = alfabeto.index(r1)
            i = int(r2)
        elif r2 in alfabeto:
            i = int(r1)
            j = alfabeto.index(r2)
        else:
            print('erro no tratamento')
        return (i, j)
    
    def vitoria():
        for i in matrizbombas:
            if 0 in i:
                break
        else:
            print('Você venceu!')
            return True
    dificuldade = gerardificuldade(desafio)
    matrizbombas = gerarmatriz(h,v)
    matrizfinal = campominado(matrizbombas)
    matrizjogo = gerarmatriz(h,v,True)

    while True:
        try:
            printfinal(matrizjogo)
            tile = input('Insira as coordenadas: ').upper()
            if tile == 'BREAK':
                break
            conferir = tratar(tile)
            revelar(conferir[0],conferir[1])

            
            

            if matrizbombas[conferir[1]][conferir[0]] == 1:
                print('Você perdeu!')
                printfinal(matrizjogo)
                break

            if vitoria():
                printfinal(matrizjogo)
                break
        except:
            print('Erro! Tente novamente')

minesweeper(10,10,5)
