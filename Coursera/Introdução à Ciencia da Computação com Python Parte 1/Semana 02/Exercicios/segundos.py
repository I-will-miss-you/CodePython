tot_segundos = int(
    input("Por favor, entre com o número de segundos que deseja converter: "))

dias = tot_segundos // 86400
rest_segundos = tot_segundos % 86400
horas = rest_segundos // 3600
rest_segundos = tot_segundos % 3600
minutos = rest_segundos // 60
rest_segundos = rest_segundos % 60

print (dias, "dias,", horas, "horas,", minutos, "minutos e", rest_segundos, "segundos.")
