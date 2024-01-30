#o programa advinha o numero que estou pensando de 1 a x
import random

def palpite(x):
    inicio = 1
    fim = x
    resposta = ''
    while resposta != 'c' and inicio != fim:
        palpite = random.randint(inicio,fim)
        resposta = input(f'o numero {palpite} esta certo? ')
        if resposta == 'alto':
            fim = palpite - 1
        elif resposta == 'baixo':
            inicio = palpite + 1
    print(f"Voce acertou o numero {palpite}")

if __name__ == '__main__':
    x = int(input("Ate qual numero voce quer advinhar: "))
    palpite(x)