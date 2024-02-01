import random

def qualNumero():
    numMaquina = random.sample(range(10), 4)
    numUsuario = []

    while saoNumerosDiferentes(numMaquina, numUsuario):
        numUsuario = input('Digite seu numero de 4 digitos(_ _ _ _): ')
        numUsuario = list(map(int, str(numUsuario)))
        numeroCerto = 0
        posicaoCerta = 0
        for numero in numUsuario:
            if numero in numMaquina:
                numeroCerto += 1
                if numUsuario.index(numero) == numMaquina.index(numero):
                    posicaoCerta += 1
        print(f"{numeroCerto} numero corretas, {posicaoCerta} posicoes certas")
        print()
    print(f"Parabens voce ganhou! o numero certo era {int(''.join(map(str,numMaquina)))}")

def saoNumerosDiferentes(lista1, lista2):
    if len(lista1) != len(lista2): return True

    for elemento1, elemento2 in zip(lista1, lista2):
        if elemento1 != elemento2:
            return True

    return False


    
if __name__ == '__main__':
    qualNumero()
