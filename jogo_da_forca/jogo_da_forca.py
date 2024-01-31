#jogo da forca em ingles
from palavras import palavras
import random
import string

def tem_elemento(conjunto):
    return any(conjunto)

def palavra_valida(palavras):
    palavra = random.choice(palavras)
    #nao escolhe as palavras com '-' ou ' '
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
    return palavra.upper()

def jogoForca():
    palavra = palavra_valida(palavras)
    letras_palavras = set(palavra)
    alfabeto = set(string.ascii_uppercase) #letras do alfabeto
    letras_usadas = set() #letras ja usadas no jogo
    tentativas = 6

    while tentativas > 0 and tem_elemento(letras_palavras):
        print('Voce usou essas letras: ', ' '.join(letras_usadas))
        lista_palavras = [letras if letras in letras_usadas else '_' for letras in palavra]
        print('Palavra atual ', ' '.join(lista_palavras))

        letra_usuario = input('Advinhe uma letra: ').upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in letras_palavras:
                letras_palavras.remove(letra_usuario)
            else:
                tentativas -= 1
                print(f'Voce tem mais {tentativas} tentativas')
        elif letra_usuario in letras_usadas:
            print('Voce ja usou essa letras, por favor tente outra')
        else:  
            print('Caracter invalido, tente novamente')
        print()
        
    if tentativas > 0:
        print(f"Voce ganhou, a palavra era {palavra}")
    else:
        print(f"Voce perdeu, a palavra era {palavra}")

if __name__ == '__main__':
    jogoForca()