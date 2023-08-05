import random

def jogar():
    print("***************************")
    print("Bem vindo ao joguinho de numeros!!")
    print("Digite um número de 0 a 10 e tente a sorte!")
    print("***************************")


    Value = (random.randrange (11))
    total_de_tentativas = 0
    pontos = 100

    print("Selecione a dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Nível de dificuldade:"))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativas {} de {}". format(rodada, total_de_tentativas))
        chute_str = input("Digite o numero: ")
        print("você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 0 or chute > 10):
            print("Você deve digitar um número entre 0 a 10")
            continue

        acertou = chute == Value
        maior = chute > Value
        menor = chute < Value

        if (acertou):
            print("você acertou, parabéns!!")
            print("Sua pontuação foi {}".format(pontos))
            break
        else:
            if (maior):
                print("você errou, que pena. O seu chute foi maior que o número secreto")
            elif (menor):
                print("você errou, que pena. O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(Value - chute)
            pontos = pontos - pontos_perdidos

    if total_de_tentativas == 0:
        print("O número correto é:", Value)

        print("O número correto é:", Value)

        print("Muito Obrigado por jogar!!")
        print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()
