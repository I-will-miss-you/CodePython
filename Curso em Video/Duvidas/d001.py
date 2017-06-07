nick = "username"
print('Bem Vindo {}!\n'.format(nick))

print('Digite \"Start\" na hora que quiser começar.')
print('Exit para sair...')
resposta = input("#:>")
resposta.lower()
while resposta != 'exit':
    if (resposta == 'start'):
        print('Escolha uma das opções:')
        print('MP')
        print('SV')
        print('Host')
        print('Normal Commands')
    resposta = input("#:>")