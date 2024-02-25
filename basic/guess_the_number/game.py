import random

def is_valid(n):
    return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100


def input_num():
    while True:
        guess = input('Range: ')
        if is_valid(guess):
            return int(guess)
        else:
            print('Input the number from 1 to 100')


def compare_num(down_num, up_num):
    num = random.randint(down_num, up_num)
    total = 0
    while True:
        n = input_num()
        total += 1
        if n < num:
            print('Nope! Your answer is less than number, try again!')
        elif n > num:
            print('Nope! Your answer is more than number, try again!')
        else:
            print('YEP!!! You used', total,  'tries, gratz!' )
            break


def continue_game():
    ans = input('Wanna try again ("y"/"n")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Only "y" or "n" please \n')
        elif ans in ('n', 'н'):
            print('See you soon!')
            return False
        else:
            return True


def game(): # Запуск игры
    print('Welceome to the "Guess the number" game!')
    while True:
        print('Input the range for game \n(from 1 to 100):\n')
        x, y = input_num(), input_num()
        if x > y:
            x, y = y, x
        print('Input the number from', x, 'to', y, '\n')
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break

game()