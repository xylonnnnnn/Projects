import matplotlib.pyplot
import pandas
import os

data = {'X': [0, 1, 5, 10, 15, 20, 25], 'Y': [0, 1, 10, 2, 30, 4, 50]}
data_frame = pandas.DataFrame(data)
matplotlib.pyplot.plot(data_frame['X'], data_frame['Y'])
matplotlib.pyplot.title('Граф')
matplotlib.pyplot.xlabel('Ось X')
matplotlib.pyplot.ylabel('Ось Y')

matplotlib.pyplot.savefig('plot.png')
test = os.path.exists('plot.png')
print(f"Файл сохранён: {test}")
