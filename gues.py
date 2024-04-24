import random 

x = 'Welcome to number guesing game.'
y = 'You onle have ten attempts to gues the correct number.'
print(x.upper())
print(y.capitalize())

lower_n = 0
upper_n = 1000
max_attempts = 10

#generate the secret number.455
secret_number = random.randint(lower_n, upper_n)
print(secret_number)

#get users gues
def get_gues():
    while True:
        try:
            guess = int(input(f'Gues any ranging  number between {lower_n} and {upper_n}:\n'))
            if lower_n <= guess <= upper_n:
                return guess
            else:
                print('Invalid input. Enter a number within the specified range.')
        except ValueError:
            print('Invalid input. Enter the correct number.')

#validate users gues 
def check_gues(guess, secret_number):
    if guess == secret_number:
        return 'correct'
    elif guess > secret_number:
        return 'Guessed too high'
    else:
        return 'Guessed too low'

#track players attempts 
def track_attempts():
    attempts = 0
    won = False 

    while attempts < max_attempts:
        attempts += 1
        guesses = get_gues()
        results = check_gues(guesses, secret_number)

        if results  == 'correct':
            print(f'congaltulation youve guesed the correct number in {attempts} attempts')
            won = True
            break

        else:
            print(f'{results}, try again. you have {max_attempts - attempts} attempts left')
    
    if not won:
        print(f'sorry youve lost the game.\n The secret number was{secret_number}')

track_attempts()