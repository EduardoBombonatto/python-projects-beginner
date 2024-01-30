#advinhe um numero que o computador escolher, ele ira te retornar se é maior, menor ou se voce acertou!
import random

def palpite(x):
    numeroAleatorio = random.randint(1, x)
    palpite = 0
    while palpite != numeroAleatorio:
        palpite = int(input(f"Faca um palpite de um numero entre 1 e {x}: "))
        if palpite > numeroAleatorio:
            print("Muito alto, o numero é menor.\n")
        elif palpite < numeroAleatorio:
            print("Muito baixo, o numero é maior.\n")

    print(f"Parabens, voce acertou o numero {numeroAleatorio}!")

if __name__ == '__main__':
    x = int(input("Ate qual numero voce quer advinhar: "))
    palpite(x)