#a. Receber número inteiro
#b. Receber número inteiro positivo
#c. Receber número inteiro de no mínimo X
#d. Receber número inteiro de no máximo X
#e. Receber número inteiro numa faixa min X e max Y

def main():
    num_int = min_num()
    print(num_int)


def inteiro():
    while True:
        try:   
            n = int(input())
            return n
        except:
            print('o numero não é inteiro, tente novamente')

def int_positivo():
    n = inteiro()
    while 0 > n:
        print('numero negativo, tente novamente')
        n = inteiro()
    return n

def min_num():
    limite = inteiro('limite: ')
    n = inteiro()
    while n < limite:
        print('numero fora do limite minimo...')
    return n

    
main()
