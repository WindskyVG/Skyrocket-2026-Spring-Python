def hello():#def means define, and right now hello() is the function. so we're defining to print the following messages
    #a function call is just the function’s name followed by parentheses, maybe with some number of arguments in between the parentheses.
    #When the program execution reaches these calls, it will jump to the first line in the function and begin executing the code there.
    # When it reaches the end of the function, the execution returns to the line that called the function and continues moving through the code as before.
    # Prints three greetings
    print('Good morning!')
    print('Good afternoon!')
    print('Good evening!')

hello()
hello()
print('ONE MORE TIME!')
hello()

print("----------------------------")

def say_hello_to(name):
    # Prints three greetings to the name provided
    print('Good morning, ' + name)
    print('Good afternoon, ' + name)
    print('Good evening, ' + name)

say_hello_to('Sophia')
say_hello_to('Alice')
say_hello_to('Bob')

import random

def get_answer(answer_number):
    # Returns a fortune answer based on what int answer_number is, 1 to 9
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'

print('Ask a yes or no question:')
input('>')
r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)