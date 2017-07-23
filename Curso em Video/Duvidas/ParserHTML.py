def find_tag_starting_in_index(string, index):
    nome = ''
    for e in range(index + 1, len(string)):
        if e == '>':
            break
        nome += string[e]
    if nome[0] == '/':
        nome = nome[1:]
    return nome


def detect_if_is_opening(string, index):
    return string[index + 1] == '/'


n = int(input())
for i in range(n):
    entrada = input()
    tag_opened = False
    tagname = ''
    entre_setas = True
    texto = ''
    for ee in range(len(entrada)):
        if entrada[ee] == '<':
            entre_setas = True
            tag_opened = detect_if_is_opening(entrada, ee)
            if tag_opened:
                tagname = find_tag_starting_in_index(entrada, ee)
        elif entrada[ee] == '>':
            entre_setas = False
        elif not entre_setas:
            texto += entrada[ee]
        if texto != '' and entre_setas:
            print(texto)
            texto = ''
