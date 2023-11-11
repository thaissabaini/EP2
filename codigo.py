from lista import lista_palavras
import random
import colorama
from colorama import init, Fore, Back, Style

colorama.init()

numero = 5
filtradas = []

print(f' ===========================\n|                           |\n| Bem-vindo ao Insper Termo |\n|                           |\n ==== Design de Software === \n\nComandos: desisto\n\n Regras:\n\n  - Você tem {Fore.RED}6{Fore.RESET} tentativas para acertar uma palavra aleatória de 5 letras.\n  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n    . {Fore.BLUE}Azul{Fore.RESET}   : a letra está na posição correta;\n    . {Fore.YELLOW}Amarelo{Fore.RESET}: a palavra tem a letra, mas está na posição errada;\n    . Branco : a palavra não tem a letra.\n  - Os acentos são ignorados;\n  - As palavras podem possuir letras repetidas.\n\nSorteando uma palavra...\nJá tenho uma palavra! Tente adivinhá-la!\n\nVocê tem 6 tentaviva(s)')
def inidica_posicao(palavra_sorteada, palavra_especulada):
    palavra_especulada = palavra_especulada.lower()
    palavra_sorteada= palavra_sorteada.lower()
    lista = []

    if len(palavra_sorteada) != len(palavra_especulada):
        return []

    for i in range(len(palavra_especulada)):
        if palavra_especulada[i] == palavra_sorteada[i]:
            lista.append(0)
        elif palavra_especulada[i] in palavra_sorteada and palavra_especulada[i] != palavra_sorteada[i]:
            lista.append(1)
        else:
            lista.append(2)
    return lista
 
for palavra in lista_palavras:
    palavra = palavra.lower() 
    palavra = palavra.strip("!?,.@")  
    if len(palavra) == numero and palavra not in filtradas:
        filtradas.append(palavra)

jogando = 1
dic = {'n': len(filtradas[0]),  'tentativas': len(filtradas[0]) + 1, 'especuladas': [],  'sorteada': random.choice(filtradas)}

divisor = ' --- --- --- --- ---'
linha1 ='|   |   |   |   |   |'
linha2 ='|   |   |   |   |   |'
linha3 ='|   |   |   |   |   |'
linha4 ='|   |   |   |   |   |'
linha5 ='|   |   |   |   |   |'
linha6 ='|   |   |   |   |   |'

linhas = [divisor, linha1, linha2, linha3, linha4, linha5, linha6]

jogadas = 0
while jogando:
    palavra_sorteada = dic['sorteada']

    palavra_especulada = str(input('Qual é seu palpite? '))
    if palavra_especulada == 'desisto':
        if input('Tem certeza que deseja desistir da rodada? [s|n] ') == 's':
            print(f'>>> Que deselegante desistir, a palavra era: {palavra_sorteada}\n')
            pergunta = str(input('Jogar novamente? [s|n] '))
            if pergunta == 's':
                dic = {'n': len(filtradas[0]),  'tentativas': len(filtradas[0]) + 1, 'especuladas': [],  'sorteada': random.choice(filtradas)}
                jogadas = 0
            else:
                print('\n\n\nAté a próxima!')
                jogando = 0

    elif len(palavra_especulada) != 5:
        print("apenas palavras de 5 letras")
    elif palavra_especulada not in filtradas:
        print('palavra desconhecida')
    elif palavra_especulada not in dic['especuladas']:
        jogadas += 1
        dic['especuladas'].append(palavra_especulada)
        resta = int(len(filtradas[0]) + 1) - jogadas
        tentativa = inidica_posicao(palavra_sorteada, palavra_especulada)
        certo = 0
        for i in tentativa:
            if i == 0:
                certo += 1
        else:
            if resta == 0:
                print('Perdeu')
                pergunta = str(input('Jogar novamente? [s|n] '))
                if pergunta == 's':
                    dic = {'n': len(filtradas[0]),  'tentativas': len(filtradas[0]) + 1, 'especuladas': [],  'sorteada': random.choice(filtradas)}
                    jogadas = 0
                else:
                    jogando = 0
            print('\nInsper :: TERMO\n')
            
            for i in range (len(linhas)):
                if i == jogadas:
                    linha_nova = '| '
                    for j in range (len(tentativa)):
                        if tentativa[j] == 0:
                            linha_nova += Fore.BLUE + f'{palavra_especulada[j]}' + Fore.RESET + ' | '
                        elif tentativa[j] == 1:
                            linha_nova += Fore.YELLOW + f'{palavra_especulada[j]}' + Fore.RESET+ ' | '
                        else:
                            linha_nova += f'{palavra_especulada[j]}' + ' | '
                    linhas[i] = linha_nova
                if i != 0:
                    print(linhas[i])
                print(divisor)
            if certo == 5:
                print(f'\n★ ★ ★ PARABÉNS! Você acertou após {jogadas} tentativa(s) ★ ★ ★')
                jogando = 0
            else:
                print(f'\nVocê tem {resta} tentativa (s)')
            if resta == 0:
                print(f' A palavra correta era {palavra_sorteada}.')
    else:
        print('Palavra já testada!')

colorama.deinit()
        
