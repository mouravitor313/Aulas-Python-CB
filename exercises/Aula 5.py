name = input('Say your name: ')
if name == 'Rodrigo':
    age = int(input('And now, how old are you? '))
    print('Nice to meet you!')
    if age >= 18:
        print('já pode ir preso XD')
    elif age == 16:
        print('You are sixteen')
    else:
        print('You are too young')
else:
    print('You are not Rodrigo...')
    if name == 'Pedro':
        print('Hi Pedro')