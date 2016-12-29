import datetime


#today = datetime.date.today()

#print(today)
#print(today.year)
#print(today.month)
#print(today.day)

#strftime allows you to specify the date format
# Ver documentação em strftime.org
#print(today.strftime("%d / %b / %y"))
#print(today.strftime("%d - %y - %b"))
#print(today.strftime("%y ; %b ; %d"))
#print(today.strftime("%a %d, %b de %y"))
#print(today.strftime("%c"))
#print(today.strftime("please attend our event %a, %b %d in the year %y") )

#Também pode ser assim apesar de não muito pratico
#currentDate = datetime.date
#print(currentDate.today())
#print(currentDate.today().year)
#print(currentDate.today().month)
#print(currentDate.today().day)

#birthday = input("What is your birthday? (mm/dd/yyyy)")
#birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()
## Why did we list datetime twice?
## Because we are calling the strptime function
## which is part of the datetime class
## which is in the datetime module
#print("Your birth month is " + birthdate.strftime('%B'))

#myBirthday = datetime.datetime.strptime("19/11/1984","%m/%d/%Y").date()
#currentDate = datetime.date.today()

#difference = currentDate - myBirthday
#print(difference.days)


agora = datetime.datetime.now()
print(agora)
print(agora.hour)
print(agora.minute)
print(agora.second)
print(datetime.datetime.strftime(agora,"%H:%M:%S"))

