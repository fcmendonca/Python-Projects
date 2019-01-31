import forca
import adivinhacao
print('********************************')
print('*******Escolha o seu jogo*******')
print('********************************')

print("(1) Forca (2) Adivinhação")

jogo = int(input("Digite o número correspondente ao jogo escolhido: "))

if (jogo == 1):
    print("Jogando forca...")
    forca.jogar()
else:
    print("Jogando adivinhação...")
    adivinhacao.jogar()
