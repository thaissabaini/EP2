from lista import lista_palavras
import random


numero = 5
filtradas = []

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
print (dic['sorteada'])
jogadas = 0
while jogando:
    jogadas += 1
    palavra_sorteada = dic['sorteada']
    palavra_especulada = str(input('Qual é seu palpite? '))

    if len(palavra_especulada) != 5:
        print("apenas palavras de 5 letras")
    else:
        tentativa = inidica_posicao(palavra_sorteada, palavra_especulada)
        j = 0
        for i in tentativa:
            if i == 0:
                j += 1
            if j == 5:
                print(f'*** Parabéns! Você acertou após {jogadas} tentativas')
                jogando = 0
