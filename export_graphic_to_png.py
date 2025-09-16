import matplotlib.pyplot
import pandas
import os

def create_plot(x_data, y_data, filename = 'plot.png', title = 'График', x_label = 'Ось X', y_label = 'Ось Y'):
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
    data = {'X': [0, 1, 5, 10, 15, 20, 25], 'Y': [0, 1, 10, 2, 30, 4, 50]}

    graph = create_plot(
        x_data = data['X'],
        y_data = data['Y']
    )

    print(f"Файл сохранён: {graph}")

if __name__ == "__main__":
    main()