frase = 'Curso em Vídeo Python'

print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])

print('''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap 
into electronic typesetting, remaining essentially unchanged. It was 
popularised in the 1960s with the release of Letraset sheets containing Lorem 
Ipsum passages, and more recently with desktop publishing software like Aldus 
PageMaker including versions of Lorem Ipsum.
''')

print(frase.count('o'))
print(frase.count('O'))

print(frase.upper().count('O'))

print(len(frase))

frase = '   Curso em Vídeo Python   '
print(len(frase))
print(len(frase.strip()))

frase = frase.strip()
print(frase)
print(frase.replace('Python', 'Android'))

print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))

print(frase.split())
strings = frase.split()
print(strings[0])
print(strings[2][3])

print('-'.join(frase))
print('-'.join(strings))