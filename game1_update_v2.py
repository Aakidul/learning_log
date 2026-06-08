import random
import os
import pandas as pd
os.system("clear")

logo = """
 /$$       /$$   /$$  /$$$$$$  /$$   /$$ /$$     /$$       /$$   /$$ /$$   /$$ /$$      /$$
| $$      | $$  | $$ /$$__  $$| $$  /$$/|  $$   /$$/      | $$$ | $$| $$  | $$| $$$    /$$$
| $$      | $$  | $$| $$  \__/| $$ /$$/  \  $$ /$$/       | $$$$| $$| $$  | $$| $$$$  /$$$$
| $$      | $$  | $$| $$      | $$$$$/    \  $$$$/        | $$ $$ $$| $$  | $$| $$ $$/$$ $$
| $$      | $$  | $$| $$      | $$  $$     \  $$/         | $$  $$$$| $$  | $$| $$  $$$| $$
| $$      | $$  | $$| $$    $$| $$\  $$     | $$          | $$\  $$$| $$  | $$| $$\  $ | $$
| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$ \  $$    | $$          | $$ \  $$|  $$$$$$/| $$ \/  | $$
|________/ \______/  \______/ |__/  \__/    |__/          |__/  \__/ \______/ |__/     |__/
                                                                                           
                                                                                           
                                                                                           


WECOME TO POOL OF NUMBERS GAME, YOU ENTER RANDOM NUMBERS BETWEEN 1 TO 1000 AND IF THAT EXISTS IN THE GAMES POOL COLLECTION OF 100 YOU WIN

"""

print(logo)

def pool():
    pool_of_numbers = []
    for i in range(1, 101):
        r = random.randint(1, 1000)
        pool_of_numbers.insert(i, int(r))
        if i == 100:
            break


    return pool_of_numbers




history_data = []

while True:
    print("ENTER STATS TO CHECK STATISTICS")
    i = input("ENTER LUCKY NUMBER:< ")

    if i.upper() == "STATS":
        wins = history_data.count(1)
        losses = history_data.count(0)

        print("Wins:", wins)
        print("Losses:", losses)
        continue

    try:
        num = int(i)
    except ValueError:
        print("Enter a number or STATS")
        continue

    pool_data = pool()

    if num in pool_data:
        print("YOU WON !!!")
        history_data.append(1)
    else:
        print("YOU LOST")
        history_data.append(0)
