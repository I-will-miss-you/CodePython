import requests
import json

key = 'apikey=plsBanMe'
r = '\033[31m'  # fonte vermelha (red)
n = '\033[m'  # Cor 'normal'


def existefilmes(titulo):
    quant = 0

    try:
        req = requests.get(f"http://www.omdbapi.com/?s={titulo}&type=movie&{key}")
        resposta = json.loads(req.text)
        if resposta['Response'] == 'True':
            quant = resposta['totalResults']
    except:
        print('Conexao falhou')
    return quant


def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        print('Pesquisando na pagina', i)
        try:
            req = requests.get(f"http://www.omdbapi.com/?s={titulo}&type=movie&page={str(i)}&{key}")
            resposta = json.loads(req.text)

            if resposta['Response'] == 'False':
                break
            else:
                for filme in resposta['Search']:
                    title = filme['Title']
                    ano = filme['Year']
                    string = f"{title} ({ano})"
                    lista.append(string)
        except:
            print('Conexao falhou')
    return lista


sair = False
while not sair:
    op = input('Pesquise por um filme ou digite SAIR: ')
    if op.lower() == 'sair':
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print(f'Filmes encontrados: {len(lista_de_filmes)}')
        for filme in lista_de_filmes:
            print(filme)
