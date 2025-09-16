import matplotlib.pyplot
import pandas
import os

def create_plot(x_data, y_data, filename = 'plot.png', title = 'График', x_label = 'Ось X', y_label = 'Ось Y'):
    """
    Создает и сохраняет график на основе переданных данных.

    Функция принимает массивы данных по осям X и Y, создает линейный график
    с использованием matplotlib и сохраняет его в файл PNG.

    Args:
        x_data (list): Массив значений для оси X
        y_data (list): Массив значений для оси Y
        filename (str, optional): Имя файла для сохранения. По умолчанию 'plot.png'
        title (str, optional): Заголовок графика. По умолчанию 'График'
        x_label (str, optional): Подпись оси X. По умолчанию 'Ось X'
        y_label (str, optional): Подпись оси Y. По умолчанию 'Ось Y'

    Returns:
        bool: True если файл успешно создан, False в случае ошибки

    Raises:
        Exception: Любые исключения, возникающие в процессе создания графика
    """
    try:
        if len(x_data) != len(y_data):
            print("Ошибка - длины массивов X и Y не совпадают")
            return False

        if not x_data or not y_data:
            print("Ошибка - массивы данных пустые")
            return False

        data_frame = pandas.DataFrame({'X': x_data, 'Y': y_data})

        matplotlib.pyplot.plot(data_frame['X'], data_frame['Y'])
        matplotlib.pyplot.title(title)
        matplotlib.pyplot.xlabel(x_label)
        matplotlib.pyplot.ylabel(y_label)

        matplotlib.pyplot.savefig(filename)

        file_exists = os.path.exists(filename)
        if file_exists:
            print(f"График сохранен в файл: {filename}")
        else:
            print(f"Ошибка: файл {filename} не создан")

        return file_exists

    except Exception as e:
        print(f"Ошибка при создании графика: {e}")
        return False


def main():
    """
    Основная функция для демонстрации работы create_plot.

    Создает тестовые данные и вызывает функцию create_plot для генерации графика.
    Выводит информацию о результате операции.
    """
    data = {'X': [0, 1, 5, 10, 15, 20, 25], 'Y': [0, 1, 10, 2, 30, 4, 50]}

    graph = create_plot(
        x_data = data['X'],
        y_data = data['Y']
    )

    print(f"Файл сохранён: {graph}")

if __name__ == "__main__":
    main()
