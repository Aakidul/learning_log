import random
import os
import pandas as pd
os.system("clear")

logo = """
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



def save_stats_data(data: int):
    with open('data.csv', 'a') as f:
        f.write(str(data) + '\n')

while True:
    i = int(input("ENTER LUCKY NUMBER:<  "))
    pool_data = pool()

    if i in pool_data:
        print('YOU WON')
        save_stats_data(1)

    else:
        print('LOST')
        save_stats_data(0)
