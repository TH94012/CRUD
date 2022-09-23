from random import choice
from time import sleep
import palavras
def jogo():
    vitorias = derrotas = 0
    def início():
        print('=' * 40)
        print('jogo da forca em python'.title().center(40))
        print('=' * 40)
        print('   By: Thiago    \033[1;33mVersion 5.0 Especial\033[m'.center(40))
        sleep(2)

    def escolhaTema():
        print('''
    \033[1;34m
Escolha o tema

 1 - Geral
 2 - Futebol
 3 - Casa
 4 - Escola
        ''')
        tema = int()
        global PALAVRAS2
        while True:
            try:
                tema = int(input('Escolha: '))
                print()
            except:
                continue
            else:
                match tema:
                    case 1:
                        PALAVRAS2 = choice(palavras.geral)
                    case 2:
                        PALAVRAS2 = choice(palavras.futebol)
                    case 3:
                        PALAVRAS2 = choice(palavras.casa)
                    case 4:
                        PALAVRAS2 = choice(palavras.escola)
                    case _:
                        print(F'\033[1;31mERRO! tema {tema} não existe.\033[1;34m')
                        continue
                break
        print('\033[m', end='')
                

    def vitoria(palavraEs):
        correto = list()
        for l in palavraEs:
            if l not in correto and l != ' ':
                correto.append(l)
        correto = sorted(correto)
        return correto

    def vida(erros):
        if erros == 0:
            print('''    ______
    |    |
    |
    |
    |
    |
        ''')
        elif erros == 1:
            print('''    ______      
    |    |
    |    O
    |
    |
    |
        ''')
        elif erros == 2:
            print('''    ______
    |    |
    |    O
    |    |
    |
    |
        ''')
        elif erros == 3:
            print('''    ______
    |    |
    |    O
    |   /|
    |
    |
        ''')
        elif erros == 4:
            print('''    ______
    |    |
    |    O
    |   /|\\
    |
    |
        ''')
        elif erros == 5:
            print('''    ______
    |    |
    |    O
    |   /|\\
    |   /
    |
        ''')
        elif erros == 6:
            print('''    ______
    |    |
    |    O
    |   /|\\
    |   / \\
    |
        ''')

    def letras(palavraEs):
        for C in palavraEs:
            if C == ' ':
                print(C, end=' ')
            elif C in ACERTOS:
                print(C, end=' ')
            elif not C in ACERTOS:
                print('_', end=' ')
        print('\n')


    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    escolha = str()
    início()
    while True: 
        ERROS = CONT = 0
        TENTATIVA = str()
        totTen = list()
        escolhaTema()
        ACERTOS = list()
        vencer = vitoria(PALAVRAS2)
        while True:
            totTen = sorted(totTen)
            for f, contador in enumerate(alfabeto):
                if contador in ACERTOS:
                    print(F'\033[1;32m{contador}\033[m', end=' ')
                elif (not contador in ACERTOS) and (contador in totTen):
                    print(F'\033[1;31m{contador}\033[m', end=' ')
                elif (not contador in ACERTOS) and (not contador in totTen):
                    print(F'\033[1;33m{contador}\033[m', end=' ')
                if (f + 1) % 13 == 0:
                    print()
            print()
            vida(ERROS)
            if ERROS == 6:
                break
            letras(PALAVRAS2)
            while True:
                try:
                    TENTATIVA = str(input('Digite uma letra ou chute a palavra: ')).upper()
                    if TENTATIVA == '':
                        continue
                    elif TENTATIVA != ' ':
                        TENTATIVA = TENTATIVA.strip()
                except:
                    continue
                else:
                    break
            if len(TENTATIVA) == 1:
                if TENTATIVA in totTen:
                    if TENTATIVA.upper().isnumeric() == False:
                        print(F'\033[1;33mVocê ja usou a letra {TENTATIVA.upper()}. Tente novamente.\033[m')
                        sleep(1)
                    else:
                        print(F'\033[1;33mVocê ja usou o número {TENTATIVA.upper()}. Tente novamente.\033[m')
                        sleep(1)
                elif TENTATIVA == ' ':
                    print('\033[1;33mNão é necessário utilizar espaços em chutes de letras.\033[m')
                    sleep(1)
                elif TENTATIVA not in PALAVRAS2:
                    ERROS += 1
                    if not TENTATIVA in totTen:
                        totTen.append(TENTATIVA)
                elif TENTATIVA in PALAVRAS2:
                    if not TENTATIVA in ACERTOS:
                        ACERTOS.append(TENTATIVA)
                    if not TENTATIVA in totTen:
                        totTen.append(TENTATIVA)
                ACERTOS = sorted(ACERTOS)
            else:
                if TENTATIVA == PALAVRAS2:
                    break
                else:
                    ERROS += 1
            if ACERTOS == vencer:
                break
            CONT += 1
            print()
        if ERROS == 6:
            derrotas += 1
            print('\033[1;31mVocê perdeu!\033[m')
            print(F'E a palavra era "{PALAVRAS2}"')
        elif ERROS < 6:
            vitorias += 1
            if ERROS > 1:
                print(F'\033[1;32mPARABÉNS! Você ganhou com {ERROS} ERROS\033[m')
            else:
                print(F'\033[1;32mPARABÉNS! Você ganhou com {ERROS} ERRO\033[m')
        while True:
            try:
                escolha = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
            except:
                continue
            else:
                if escolha == 'N' or escolha == 'S':
                    break
        if escolha == 'N':
            break
        print()
    return [vitorias, derrotas]

if __name__ == '__main__':
    jogo()