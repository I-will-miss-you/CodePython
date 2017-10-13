lista=[]
try:
    altura=int(input("digite a sua altura: "))
    while altura!=-99:
        lista.append(altura)
        altura=int(input("digite a sua altura: "))
except:
    pass
print(lista)   