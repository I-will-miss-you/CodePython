tot_segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horas = tot_segundos // 3600
rest_segundos = tot_segundos % 3600
minutos = rest_segundos // 60
rest_segundos = rest_segundos % 60

print(horas, "horas, ", minutos, "minutos e", rest_segundos," segundos.")