import requests
import json

#
#    Foi usada a API: www.omdbapi.com
#

key = '&apikey=plsBanMe'

r = '\033[31m'  # fonte vermelha (red)
n = '\033[m'  # Cor 'normal'


def execute(query):
    try:
        request = requests.get(f"http://www.omdbapi.com/?{query}{key}")
        info = json.loads(request.text)
        return info
    except Exception as e:
        print(f"ERRO: {e}")
        return {}


def printInfo(info):
    print('\n', '=x=' * 40, '\n')
    print(f"{r}Título:{n} {info['Title']}")
    print(f"{r}Ano:{n} {info['Year']}")
    print(f"{r}Diretor:{n} {info['Director']}")
    print(f"{r}Released:{n} {info['Released']}")
    print(f"{r}Runtime:{n} {info['Runtime']}")

    genres = str(info['Genre']).split(',')
    print(f"{r}Genre:{n} ")
    for genre in genres:
        print(f" - {genre.strip()}")

    actors = str(info['Actors']).split(',')
    print(f"{r}Atores:{n} ")
    for actor in actors:
        print(f" - {actor.strip()}")

    print(f"{r}Writer:{n} {info['Writer']}")
    print(f"{r}Nota:{n} {info['imdbRating']}")
    print(f"{r}Poster:{n} {info['Poster']}")


def run():
    name = input("Nome do filme: ")
    movies = execute(f's={name}')
    for movie in movies['Search']:
        info = execute("i=" + movie['imdbID'])
        printInfo(info)


def start():
    sair = False
    while not sair:
        run()
        print()
        sair = True if input(
            "Para realizar uma nova pesquisa basta clicar 'ENTER',"
            " para sair da app degite 'sair': ").strip().lower() == 'sair' else False


# Iniciar a aplicação
start()
