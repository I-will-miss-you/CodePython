l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

print("#" * l)
for i in range(1, a - 1):
    print("{0}{1}{0}".format("#", " " * (l - 2)))
print("#" * l)
