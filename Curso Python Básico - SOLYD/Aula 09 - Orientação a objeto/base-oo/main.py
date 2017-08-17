from veiculo import Veiculo
from carro import Carro
caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

#print(caminhao_rosa)
#print(type(caminhao_rosa))

print('Caminhão Rosa')
print("Cor:", caminhao_rosa.cor, "\nMarca:", caminhao_rosa.marca, "\nTanque:", caminhao_rosa.tanque)

print()

print('Carro Azul')
carro_azul = Carro('azul', 'bmw', 30)
print("Cor:", carro_azul.cor, "\nMarca:", carro_azul.marca, "\nTanque:", carro_azul.tanque)

print('\nAbastecer 35lt')
carro_azul.abastecer(35)
print("Cor:", carro_azul.cor, "\nMarca:", carro_azul.marca, "\nTanque:", carro_azul.tanque)



