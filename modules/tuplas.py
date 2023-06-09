import random

options = ('piedra','papel','tijera')

user_option = input("Piedra, papel o tijera -> ")
user_option = user_option.lower()
option_computer = random.choice(options)


#Al utilizar la funcion not, se esta diciendo que si la opcion del usuario 
#no esta en la tupla option, arroje el mensaje de error
if not user_option in options:
    print("Esa opcion no es valida")

if user_option == option_computer:
    print(user_option)
    print(option_computer)
    print('Empate')
elif user_option == 'piedra':
    if option_computer == 'tijera':
        print(user_option)
        print(option_computer)
        print('Gano el usuario')
    else:
        print(user_option)
        print(option_computer)
        print('Gano la computadora')
        print()


