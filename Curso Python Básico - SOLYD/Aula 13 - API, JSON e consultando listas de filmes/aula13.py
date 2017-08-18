import requests
import json


#
# Google Books APIs
#

your_key = 'A sua chave - ver: https://support.google.com/googleapi/answer/6158857?hl=pt-BR'

def pesquisa(query):
    try:
        req = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q={query}&key={your_key}")
        dicionario = json.loads(req.text)
        print('\nLISTA DE LIVROS: \n')
        for items in dicionario['items']:
            print(' « = » ' * 20, '\n')
            # VOLUME INFO
            #  print(f"\033[31mVolume Info:\033[m {items['volumeInfo']}")

            # TITLE
            print(f"\033[31mTitle:\033[m {items['volumeInfo']['title']}")

            # AUTHORS
            print(f"\033[31mAuthors:\033[m ", end='')
            try:
                for author in items['volumeInfo']['authors']:
                    print(f"{author}")
            except:
                print('NaN')

            # PUBLISHER
            try:
                publisher = items['volumeInfo']['publisher']
            except:
                publisher = 'NaN'
            print(f"\033[31mPublisher:\033[m {publisher}")

            # PUBLISHED DATE
            try:
                publishedDate = items['volumeInfo']['publishedDate']
            except:
                publishedDate = 'NaN'
            print(f"\033[31mPublished Date:\033[m {publishedDate}")

            # DESCRIPTION
            print(f"\033[31mDescription:\033[m", end=' ')
            try:
                flag = 1
                for text in items['volumeInfo']['description']:
                    print(text, end='')
                    flag += 1
                    if flag % 200 == 0:
                        print()
                print()
            except:
                print('NaN')
            print()
    except Exception as e:
        print(f'\033[31m"ERRO: {e}" \033[m')


sair = False
while not sair:
    query = input('Digite o assunto do livro: ')
    pesquisa(query)
    sair = True if input("Degite 'sair' para sair da aplicação: ").strip().lower() == 'sair' else False
    print()
