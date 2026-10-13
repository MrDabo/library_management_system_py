import random
import string

def str_input(prompt): 
    while True:
        input_value = input(f'{prompt}: ')
        if not input_value:
            print(f'Please {prompt.lower()}')
        else: break
    return input_value

def int_input(prompt, start, end):
    while True: 
        input_value = input(f'{prompt}: ')
        if not input_value.isdigit():
            print('Please enter only numeric characters')
        else:
            input_value = int(input_value)
            if not start <= input_value <= end:
                print(f'Please enter a value between {start} and {end}')
            else:
                break
    return input_value

def return_prompt():
    input('Enter any key to return to the main menu')

id_chars = string.digits + string.ascii_letters
def generate_id(start, length):
    id = start.upper()
    for x in range(length - len(id)):
        id += random.choice(id_chars)
    return id