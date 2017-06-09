num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if i % 2 == 0:
        print('{} - par'.format(i))
    else:
        print('{} - ímpar'.format(i))


for i in range(num):
    if i % 2 == 0:
        print('{} - par'.format(i))
    else:
        print('{} - ímpar'.format(i))


i = 0
while i < 10:
    print(i)
    i += 1

print("************")

for i in range(10):
    print(i)