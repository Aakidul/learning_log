
import os

os.system('clear')

logo = """


  ░██████  ░█████████     ░███    ░███████   ░██████████ ░███     ░███ ░██     ░██   ░██████   ░██     ░██ 
 ░██   ░██ ░██     ░██   ░██░██   ░██   ░██  ░██         ░████   ░████ ░██     ░██  ░██   ░██  ░██    ░██  
░██        ░██     ░██  ░██  ░██  ░██    ░██ ░██         ░██░██ ░██░██ ░██     ░██ ░██         ░██   ░██   
░██  █████ ░█████████  ░█████████ ░██    ░██ ░█████████  ░██ ░████ ░██ ░██     ░██  ░████████  ░███████    
░██     ██ ░██   ░██   ░██    ░██ ░██    ░██ ░██         ░██  ░██  ░██ ░██     ░██         ░██ ░██   ░██   
 ░██  ░███ ░██    ░██  ░██    ░██ ░██   ░██  ░██         ░██       ░██  ░██   ░██   ░██   ░██  ░██    ░██  
  ░█████░█ ░██     ░██ ░██    ░██ ░███████   ░██████████ ░██       ░██   ░██████     ░██████   ░██     ░██ 
                                                                                                           
                                                                                                           
                                                                                                           


"""


print(logo)
print('\n')







def main(data):

    def loop_for_user(data_for_grade):
             while True:
                 user_i1 = str(input('ENTER ALPHABET:  ')).lower()
                 if user_i1 in data_for_grade.keys():
                     output = data_for_grade.get(user_i1)
                     print(f'Results: {output}')

                 else:
                    print('Enter valid grade data !')



    if data:
        loop_for_user(data)


    elif not data:
        data_for_grade = {'a': 'above 96%', 'b': 'above 86%', 'c': 'above 70%', 'd': 'above 60%', 'e': 'above 50%', 'f': 'failed'}
        loop_for_user(data_for_grade)


    else:
        print('Invalid data format')





print('choose between')
print('1. Add data to grading system')
print('2. Check grades')

user_i2 = int(input('> '))


if isinstance(user_i2, int):
    if user_i2 == 1:

        data_for_main = {}
        alphabets_for_grades = ['a', 'b', 'c', 'd', 'e', 'f']
        for i in range(0, 6):
            current_alpha = alphabets_for_grades[i]
            user_i3 = str(input(f'ENTER GRADE FOR {current_alpha} : '))
            data_for_main[current_alpha] = user_i3
        main(data_for_main)


    elif user_i2 == 2:
        x3 = {}
        main(x3)


    else:
        print('choosen fucntion does not exists.')
else:
    print('please enter right input')
