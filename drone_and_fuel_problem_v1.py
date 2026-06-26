# DRONE AND FUEL PROBLEM
#QUESTION AND CONDITION GIVEN BELOW
"""
You are tracking a drone's fuel level as it flies across a series of map segments. The drone starts with a set amount of fuel. At every single segment, the drone burns a base rate of 10 fuel units, but the wind changes this amount: a positive wind helps the drone (so it burns less fuel), while a negative wind hurts the drone (so it burns more fuel). You use a loop to calculate the new fuel level after each segment. If the fuel ever hits 0 or less, the drone crashes immediately, and your code must stop and report the exact segment number where it went down. If the drone makes it through every single segment safely, your code reports the amount of fuel left over.

"""

def drone_survival(fuel, wind):
    #formula is fuel = current_fuel - (base_burn - wind)
    base_burn = 10
    current_fuel = fuel
    drone_crashed = False
    for i in range(len(wind)):
        current_fuel = current_fuel - (base_burn - wind[i])
        if current_fuel <= 0:
            drone_crashed = True
            print(f"Crashed at {i}")
            break
    if not drone_crashed:
        print(current_fuel)


drone_survival(45, [2, 5, -8, 1, -4])
