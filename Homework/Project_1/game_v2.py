"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np


def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """Randomly guess a number
    Args:
        number (int, optional): Hidden number. Defaults to 1.
    Returns:
        int: Number of attempts
    """
    # Создаем переменные:
    # Количество попыток
    count = 0
    # минимальное число
    min_number = 0
    # максимальное число
    max_number = 100
    # предполагаемое число
    predict_number = np.random.randint(1, 101)
    # Создаём цикл
    while True:
        count += 1

        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2

        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2

        else:
            # Конец игры, число найдено
            break
    # Возвращаем результат
    return count
# Выводим результат на экран
print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает
    наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    # Создаем список для сохранения количества попыток
    count_ls = []
    # Фиксируем сид для воспроизводимости
    np.random.seed(1)
    # Загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))
    # Находим среднее количество попыток
    score = int(np.mean(count_ls))

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)


# RUN
if __name__ == '__main__':
    score_game(random_predict)
