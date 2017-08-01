#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

nomes = input("Nome da cidade: ").strip().split()
print("Santo" in nomes[0])
