

#USING TYPE TO VERIFY STRING
print("HELLO")
print('what is your name?')
i = str(input('> '))
if type(i) == str:
    print(f'Hello {i}')
    print(type(i))


else:
    print('Please enter name')


#USING ISINSTANCE TO VERIFY STRING

print("HELLO")
print('what is your name?')
y = str(input('> '))

if isinstance(y, str):
    print(f'Helllo {y} sir')
    print('How i can help you')
