#jogo simples de pedra papel e tesoura, que nao pode empatar
import random

def jokenpo():
    usuario = input('escolha: (R para pedra, S para tesoura e P para papel)')
    computador = random.choice(['R', 'S', 'P'])
    while usuario == computador:
        usuario = input('escolha: (R para pedra, S para tesoura e P para papel)')
        computador = random.choice(['R', 'S', 'P'])

    if  regras(usuario, computador):
        print('Parabens voce venceu!')
        print(f"computador: {computador} voce:{usuario}")
    else:
        print('Que pena, voce perdeu!')
        print(f"computador: {computador} voce: {usuario}")


def regras(player1, player2):
    #retorne 'true' se player1 venceu
    if (player1 == 'R' and player2 == 'S') or (player1 == 'S' and player2 == 'P') or (player1 == 'P' and player2 == 'R'):
        return True
    else:
        return False

if __name__ == '__main__':
    jokenpo()