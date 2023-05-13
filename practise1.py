def search_max(array: dict) -> (int, str):
    max, res = 0, ''
    for i, j in array.items():
        if j > max:
            max, res = j, i

    return max, res


res = {}


print('Голосование за автомобиль года!\n\n')


for i_car in range(int(input('Сколько моделей авто участвуют в голосовании?: '))):
    model = str(input(f'Введите модель {i_car + 1}-го автомобиля: ')).strip()
    res[model] = 0
else:
    print('\nГолосование создано!')
    models = ' '.join([i for i in res.keys()])
    print(f'Выберите модель из списка: {models}')
    print('Для подсчета голосов введите 0\n')


while True:
    vote = str(input('Ваш выбор: ')).strip()

    if not vote:
        print('Голосование завршено!')

        votes, best_model = search_max(res)

        print(f'Лучший автомобиль: {best_model}')
        print(f'Количество голосов: {votes}')
        break

    try:
        res[vote] += 1
    except KeyError as er:
        print(f'Ошибка: {er}')
    else:
        print('Ваш голос принят')
