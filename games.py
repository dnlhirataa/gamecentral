import hangmangame
import guessinggame

def escolhe_jogo():
    print("*********************************")
    print("*******What game you will play today?*******")
    print("*********************************")

    print("(1) hangman (2) guessing game")

    jogo = int(input("which game?"))

    if(jogo == 1):
        print("Playing hangman...")
        hangmangame.jogar()
    elif(jogo == 2):
        print("Playing guessing game...")
        guessinggame.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
