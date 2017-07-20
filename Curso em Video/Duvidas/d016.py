def lerLinhaCSV (todosArq):
    txt = ''
    for item in todosArq:
        txt += item + ";"
    return txt

quantElem=int(input("Quantidade elementos:"))
todosArq=[]
for item in range(quantElem):
    itens=input("Item {}: ".format(item + 1))
    todosArq.append(itens)
print(lerLinhaCSV(todosArq))