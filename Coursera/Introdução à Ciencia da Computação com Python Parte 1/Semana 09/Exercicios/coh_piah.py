import re
from math import pow, sqrt


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    soma = 0
    for i in range(6):
        soma += sqrt(pow(as_a[i] - as_b[i], 2))
    return soma / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    total_sentencas = len(sentencas)

    frases = []
    soma_caracter_sentencas = 0
    for sentenca in sentencas:
        soma_caracter_sentencas += len(sentenca)
        frases += separa_frases(sentenca)
    total_frases = len(frases)

    palavras = []
    soma_caracter_frases = 0
    for frase in frases:
        soma_caracter_frases += len(frase)
        palavras += separa_palavras(frase)
    total_palavras = len(palavras)

    soma_tamanho_palavras = 0
    for palavra in palavras:
        soma_tamanho_palavras += len(palavra)

    total_palavras_diferentes = n_palavras_diferentes(palavras)
    total_palavras_unicas = n_palavras_unicas(palavras)

    # wal = Tamanho medio de palavra
    wal = soma_tamanho_palavras / total_palavras
    # ttr = Relação Type-Token
    ttr = total_palavras_diferentes / total_palavras
    # hlr = Razão Hapax Legomana
    hlr = total_palavras_unicas / total_palavras
    # sal = tamanho médio de sentença
    sal = soma_caracter_sentencas / total_sentencas
    # sac = complexidade média da sentença
    sac = total_frases / total_sentencas
    # pal = tamanho medio de frase
    pal = soma_caracter_frases / total_frases
    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista = []
    for texto in textos:
        lista.append(compara_assinatura(calcula_assinatura(texto), ass_cp))
    return lista.index(min(lista)) + 1
