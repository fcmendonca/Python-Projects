import random

def jogar():

    print('********************************')
    print('Bem vindo ao jogo da adivinhação')
    print('********************************')

    numero_secreto = random.randrange(1, 101)
    numero_tentativa = 0
    rodada = 1
    pontos = 1000

    print("Escolha o nível de dificuldade.")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Qual a dificuldade desejada? \n"))

    if(nivel == 1):
        numero_tentativa = 20
    elif (nivel == 2):
        numero_tentativa = 10
    else:
        numero_tentativa = 5

    for rodada in range(1, numero_tentativa + 1):

        print('Tentativa {} de {}' .format(rodada, numero_tentativa))

        chute = int(input('Digite um número entre 1 e 100: '))

        print('Você chutou o número ', chute)

        if (chute < 1 or chute > 100):
            print("Número inválido! Digite um número entre 1 e 100. \n  ***Você perdeu uma tentativa***")
            continue

        acertou = numero_secreto == chute
        maior   = numero_secreto < chute
        menor   = numero_secreto > chute

        if (acertou):
            print('Você acertou! Sua pontuação final é: {}'.format(pontos))
            break

        else:
            if(maior):
                print("Você errou! O número digitado é maior que o número secreto")
            elif (menor):
                print("Você errou! O número digitado é menor que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print('Fim do jogo.....')

    print('O número secreto é: {}'.format(numero_secreto))

if (__name__== "__main__"):
    jogar()