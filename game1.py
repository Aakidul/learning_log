import random
import os


os.system("clear")

logo = """
 ________  ________      ___    ___  _____  ________  ________  ________     
|\   ____\|\   __  \    |\  \  /  /|/ __  \|\   __  \|\   __  \|\   __  \    
\ \  \___|\ \  \|\  \   \ \  \/  / /\/_|\  \ \  \|\  \ \  \|\  \ \  \|\  \   
 \ \  \  __\ \   __  \   \ \    / /\|/ \ \  \ \  \\\  \ \  \\\  \ \  \\\  \  
  \ \  \|\  \ \  \ \  \   \/  /  /      \ \  \ \  \\\  \ \  \\\  \ \  \\\  \ 
   \ \_______\ \__\ \__\__/  / /         \ \__\ \_______\ \_______\ \_______\
    \|_______|\|__|\|__|\___/ /           \|__|\|_______|\|_______|\|_______|
                       \|___|/                                               
                                                                             
                                                                             
WECOME TO POOL OF NUMBERS GAME, YOU ENTER RANDOM NUMBERS BETWEEN 1 TO 1000 AND IF THAT EXISTS IN THE GAMES POOL COLLECTION OF 100 YOU WIN

"""



def pool():
    pool_of_numbers = []
    for i in range(1, 101):
        r = random.randint(1, 1000)
        pool_of_numbers.insert(i, int(r))
        if i == 100:
            break


    return pool_of_numbers


while True:
    i = int(input("ENTER LUCKY NUMBER:<  "))
    pool_data = pool()

    if i in pool_data:
        print('YOU WON')

    else:
        print('LOST')
