import random
from palavras import lista_palavras

#definição para pegar aleatoriamente uma palavra da lista de palavras
def get_palavra():
    palavra = random.choice(lista_palavras)
    return palavra.upper()

#definição de como o game irá se comportar
def play(palavra):
    palavra_completa = "_" * len(palavra)   #lista criada e o len se refere a uma função que retorna a quantidade de itens dessa lista
    adivinhar = False
    adivinhar_letras = [] #armazenador de letras
    adivinhar_palavras = []   #armazenador de palavras
    tentativas = 6   #número de tentativas correspondente aos pedaços do corpo no jogo da forca.
    print("Hora de jogar o game da forca!")
    print(display_enforcamento(tentativas))
    print(palavra_completa)
    print("\n")
    while not adivinhar and tentativas > 0:   #condicional enquanto não for verdade que adivinhações e tentativas seja maior que zero
        palpite = input("Adivinhe uma letra ou a palavra inteira:").upper() 
        if len(palpite) == 1 and palpite.isalpha():   #verifica se o tamanho do palpite é igual a 1 ou seja, se é uma letra + "isalpha" é um verificador se o que foi digitado é um caracter textual/letras.
            if palpite in adivinhar_letras:   #verifica se o palpite (letra) dado é repetido
                print("Você já adivinhou essa letra", palpite)
            elif palpite not in palavra:          #após a verificação acima, sobra apenas a opção da letra que não pertence a palavra.
                print(palpite, "Essa letra não é dessa palavra")
                tentativas -= 1
                adivinhar_letras.append(palpite)
            else:
                print("Bom trabalho campeão,", palpite, "é uma letra da palavra!") #Programação e frase quando uma letra pertence a palavra.
                adivinhar_letras.append(palpite)         #.append é responsável por acrescentar um elemento a lista (o palpite dado).
                palavra_as_list = list(palavra_completa)  #daqui para baixo é criado uma listas de comparação com índices para verificação ...
                indices = [i for i, letra in enumerate(palavra) if letra == palpite]
                for index in indices:
                    palavra_as_list[index] = palpite
                palavra_completa = "".join(palavra_as_list)
                if "_" not in palavra_completa:
                    adivinhar = True
        elif len(palpite) == len(palavra) and palpite.isalpha():   #verifica o tamanho da palavra digitada e se correponde ao tamanho da palavra a ser acertada + verificador se é letras.
            if palpite in adivinhar_palavras:                      #verificador 'se' o palpite está na palavra a ser adivinhada.
                print("Você já adivinhou essa palavra", palpite)
            elif palpite != palavra:                               #verificador de quando não é uma palavra
                print(palpite, "isso não é uma palavra")
                tentativas -= 1
                adivinhar_palavras.append(palpite)      #.append é responsável por acrescentar um elemento a lista (o palpite dado).
            else:
                adivinhar = True
                palavra_completa = palavra
        else:                                               #verificador para quando não é uma letra ou palavra válida.
            print("Não é um palpite válido!")   
        print(display_enforcamento(tentativas))
        print(palavra_completa)
        print("\n")
    if adivinhar:
        print("Parabéns, você adivinhou corretamente a palavra! Você venceu!") #Programação e frase quando venceu a partida.
    else:
        print("Desculpa ae, mas você perdeu. A palavra era " + palavra + ". Quem sabe na próxima!") #Programação e frase quando perdeu a partida.
        

#definição do display dos estágios do jogo da forca a serem exibidos na tela, conforme o número de tentativas erradas vai se acumulando.
def display_enforcamento(tentativas):
    stages = [  # estágio final: cabeça, tronco, ambas as mãos, e ambas as pernas
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # cabeça, tronco, ambas as mãos e uma perna
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # cabeça, tronco e ambas as mãos
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # cabeça, tronco e uma mão
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # cabeça e tronco
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # cabeça
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio incial: vazio
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tentativas]

#inicialização/reinicialização automática
def main():  
    palavra = get_palavra()
    play(palavra)
    while input("Bora jogar denovo? (S/N) ").upper() == "S":
        palavra = get_palavra()
        play(palavra)

#início da execução
if __name__ == "__main__":
    main()
