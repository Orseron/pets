import random
import time

answer = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже',	'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос!')
print()
time.sleep(1.5)
name = input('Как тебя зовут?\n')
print('Привет,', name + '!')
print()

def lucky_me():
    while True:
        question = input('Напиши свой вопрос: ')
        if question.isdigit():
            print('Вопрос должен сожержать текст')
            lucky_me()
        for i in range(3):
            print('Думаю...')
            time.sleep(0.5)
        print()
        print('Придумал!', random.choice(answer))
        anothertry()

def anothertry():
    print()
    time.sleep(1)
    again = input('Ещё вопросы есть? (д/н) ')
    if again.isdigit():
        print('Введи только "д" или "н"')
        anothertry()
    elif again == 'н':
        print('Ещё увидимся!')
        exit()
    elif again == 'д':
        print()
        lucky_me()
    else:
        print('Введи только "д" или "н"')
        anothertry()

lucky_me()