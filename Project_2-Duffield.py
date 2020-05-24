# Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Hra funguje následovně:

# Počítač vygeneruje tajné 4místné číslo. Každá číslice tohoto čísla musí být jiná.
# Počítač vždy vyzve uživatele, aby hádal toto číslo.
# Počítač vyhodnotí tip uživatele a vrátí počty shod.

# Pokud uživatel uhádne správné číslo i správnou pozici, jedná se o "bulls".
# Pokud je pozice jiná, ale číslice je správná, jedná se o "cows".
import random
from datetime import datetime


def greet_user():
    print('Hi there!')
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")


def generate_number():
    numbers = range(10)
    random_number = random.sample(numbers, k=4)
    print(random_number)
    return random_number


def get_user_guess():
    user_input = input('Enter a 4 digit number: ')
    print(user_input)
    if user_input.isdigit() and len(user_input) == 4:
        return user_input
    else:
        print('Zadané číslo není správné. Zkus znovu.')
        return get_user_guess()


def get_number_of_bulls(random_number, user_input):
    count_bulls = 0
    for index, number in enumerate(user_input):
        if number == str(random_number[index]):
            count_bulls += 1
    print('bulls: ', count_bulls)
    return count_bulls


def get_number_of_cows(random_number, user_input):
    count_cows = 0
    for number in set(user_input):  # kdyby uzivatel zadal nespravne cislo obsahujuce opakujuce se cislice
        if int(number) in random_number:
            count_cows += 1
    print('cows: ', count_cows)
    return count_cows


def evaluate_user_game(random_number, guess_count):
    user_input = get_user_guess()
    count_cows = get_number_of_cows(random_number, user_input)
    count_bulls = get_number_of_bulls(random_number, user_input)
    if count_bulls == 4:
        print(f"Correct, you've guessed the right number in {guess_count} guesses!")
    else:
        guess_count += 1
        evaluate_user_game(random_number, guess_count)


def measure_gametime(time_start):
    time_end = datetime.now()
    gametime = (time_end - time_start).seconds
    hours, remainder = divmod(gametime, 3600)
    minutes, seconds = divmod(remainder, 60)
    print('It took you {:01} hours, {:01} minutes and {:01} seconds to quess the right number.'.format(int(hours), int(minutes), int(seconds)))


def play_again():
    answer = input('Do you want to play again? (Y/N): ')
    if answer in ['Y', 'y', 'yes']:
        return play_game()
    elif answer in ['N', 'n', 'no', 'not']:
        print('Goodbye!')
    else:
        return play_again()


def play_game():
    greet_user()
    random_number = generate_number()
    guess_count = 1
    time_start = datetime.now()
    evaluate_user_game(random_number, guess_count)
    measure_gametime(time_start)
    play_again()

play_game()

