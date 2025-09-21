#Jogo feito para interface no terminal, não uma interface gráfica chique, é bem simples.

palavra = "olho"
tentativas_jogador = []
chances = 6
stop = False
vitoria = False


while stop == False:

    print(f"\nVocê tem {chances} chances\n")
    for letra in palavra:
        if letra.lower() in tentativas_jogador:
            print(letra, end=" ")

        else:
            print("_", end=" ")


    tentativa = str(input("\nDigite uma letra: "))
    tentativas_jogador.append(tentativa.lower())
    
    if tentativa.lower() not in palavra:
        chances -= 1

    stop = True
    vitoria = True
    for letra in palavra:
        if letra.lower() not in tentativas_jogador:
            stop = False
            vitoria = False

    if chances == 0:
        print(f"\nVocê Perdeu! A palavra era '{palavra}'")
        stop = True
    
    if vitoria == True:
        print(f"\nParabéns! Você ganhou, a palavra era '{palavra}'\n")




    

    