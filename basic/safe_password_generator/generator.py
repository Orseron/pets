import random
import time

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
abc = ''

print('Привет! \n Я - генератор надеждных паролей. \n Приступим!')
print()

def get_amount():
    amount = input('Введите количество паролей для генерации: ')
    if amount.isdigit() and int(amount) > 0:
        return int(amount)
    else:
        print('Вводи только число больше нуля')
        get_amount()


def get_length():
    length = input('Введите длину пароля (от 8 символов): ')
    if length.isdigit() and int(length) >= 8:
        return int(length)
    else:
        print('Вводи только число больше или равное 8')
        get_length()

def get_digit():
    add_digit = input('Включить в пароль цифры? (д/н): ').lower().strip()
    if add_digit == 'д':
        return add_digit
    elif add_digit == 'н':
        ...
    else:
        print('Введите только "д" или "н"')
        get_digit()


def get_lowercase():
    add_lowercase = input('Включить прописные буквы? (д/н): ').lower().strip()
    if add_lowercase == 'д':
        return add_lowercase
    elif add_lowercase == 'н':
        ...
    else:
        print('Введите только "д" или "н"')
        get_lowercase()


def get_uppercase():
    add_uppercase = input('Включить строчные буквы? (д/н): ').lower().strip()
    if add_uppercase == 'д':
        return add_uppercase
    elif add_uppercase == 'н':
        ...
    else:
        print('Введите только "д" или "н"')
        get_uppercase()


def get_punctuation():
    add_punctuation = input('Включить спецсимволы? (д/н): ').lower().strip()
    if add_punctuation == 'д':
        return add_punctuation
    elif add_punctuation == 'н':
        ...
    else:
        print('Введите только "д" или "н"')
        get_punctuation()

amount = get_amount()
length = get_length()
add_digit = get_digit()
add_lowercase = get_lowercase()
add_uppercase = get_uppercase()
add_punctuation = get_punctuation()

if add_digit == 'д':
    abc += random.choice(digits)
    chars += digits
if add_lowercase == 'д':
    abc += random.choice(lowercase_letters)
    chars += lowercase_letters
if add_uppercase == 'д':
    abc += random.choice(uppercase_letters)
    chars += uppercase_letters
if add_punctuation == 'д':
    abc += random.choice(punctuation)
    chars += punctuation

g = len(abc)

def generate_password(g, length, chars):
    password = ''
    for j in range(g, length):
        password += random.choice(chars)
    return password

print()

for j in range(amount):
    print('Генерирую...')
    time.sleep(1.2)

print()

for j in range(amount):
    password = list(generate_password(g, length, chars) + abc)
    random.shuffle(password)
    print('Твой пароль №', j+1, ': ', *password, sep='')
    time.sleep(0.3)

print()
print('До новых встреч!')