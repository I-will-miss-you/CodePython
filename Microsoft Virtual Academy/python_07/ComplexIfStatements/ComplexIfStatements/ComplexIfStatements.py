#the "elif" allows you to check for different values
#country = input("Where are you from?")

#if country.upper() == "CANADA" :
#    print("Hello")
#elif country.upper() == "GERMANY" :
#    print("Guten Tag")
#elif country.upper() == "FRANCE" :
#    print("Bonjour")
#else :
#    print("I dont no")


monday = True
freshCoffe = False

if monday :
    if not freshCoffe :
        print("Go buy a caffee!")
    print("I hate Mondays")
print("Now you can start work")



# Feitos pelo apresentador
sport = input('Enter your favorite sport: ').upper()
team = input('Enter your favorite hockey team: ').upper()


#if team == 'FLYERS':
#    print('Best team ever!!')
#elif team == 'SENATORS':
#    print('Go Sens Go!')
#elif team == 'RANGERS':
#    print('Go Rangers')
#else:
#    print('I don\'t have anything clever to say here')

#if sport == 'HOCKEY' and team == 'RANGERS':
#    print('I miss Messier')
#elif team == 'LEAFS' or team == 'SENATORS':
#    print('Good luck getting the cup this year')
#else:
#    print('I don\'t know that team')

##If the sport is hockey, and the team is the senators or leafs, display the cup message
#if sport == 'HOCKEY' and (team == 'SENATORS' or team == 'LEAFS') :
#     print('Good luck getting to the cup this year')

#sportIsHockey = False
#if sport == 'HOCKEY':
#    sportIsHockey = True

#teamIsCorrect = False
#if team == 'SENATORS' or team == 'LEAFS':
#    teamIsCorrect = True

#if sportIsHockey and teamIsCorrect:
#     print('Good luck getting to the cup this year')

if sport == 'HOCKEY':
    print('Go hockey!!!')
    if team == 'SENATORS':
        print('Good luck getting to the cup')
        print('We do love hockey!!!')