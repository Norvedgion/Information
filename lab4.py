# Импорт необходимых модулей из библиотек PyQt5 и Matplotlib
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Определение класса главного окна приложения
class MainWindow(QMainWindow):
    # Метод инициализации класса
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Настройка заголовка окна
        self.setWindowTitle('График')
        # Создание фигуры и холста для графика Matplotlib
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        # Создание центрального виджета и размещение холста в вертикальном макете
        cental_widget = QWidget()
        layout = QVBoxLayout()
        cental_widget.setLayout(layout)

        layout.addWidget(self.canvas)

        self.setCentralWidget(cental_widget)
        # Создание кнопки для отображения графика
        self.plot_button = QPushButton('Нарисовать график')
        self.plot_button.clicked.connect(self.plot_data)
        # Создание элементов интерфейса для ввода диапазона и функций
        self.range_label = QLabel('Диапазон:')
        self.range_start_input = QLineEdit('0')
        self.range_end_input = QLineEdit('1')

        self.add_function_button = QPushButton('Добавить функцию в список')
        self.function_input = QLineEdit('*Введите функцию для добавление в список*')
        self.function_widget = QComboBox()
        self.function_widget.addItems(['x', '2**x', 'x**(1/2)', 'x**3'])
        self.add_function_button.clicked.connect(self.add_function)
        # Создание элементов интерфейса для ввода количества точек на графике
        self.point_amount = QLabel('Количество точек на графике:')
        self.point_input = QLineEdit('100')
        # Создание кнопок для очистки графика и сохранения данных в файл
        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        self.file_button = QPushButton('Сохранить точки в файл')
        self.file_button.clicked.connect(self.file_save)
        # Размещение элементов интерфейса в вертикальном макете
        layout.addWidget(self.function_widget)
        layout.addWidget(self.range_label)
        layout.addWidget(self.range_start_input)
        layout.addWidget(self.range_end_input)
        layout.addWidget(self.point_amount)
        layout.addWidget(self.point_input)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.file_button)
        layout.addWidget(self.add_function_button)
        layout.addWidget(self.function_input)

    # Метод для создания массивов x и y для построения графика
    def vectors(self):
        try:
            expression = self.function_widget.currentText()
        except NameError:
            expression = 'x'

        try:
            range_start = float(self.range_start_input.text())
            range_end = float(self.range_end_input.text())
            points = int(self.point_input.text())
        except ValueError:
            range_start = 0
            range_end = 1
            points = 50

        functions = {}
        exec(f'def f(x): return {expression}', functions)

        x = np.linspace(range_start, range_end, points)
        function = functions['f']
        try:
            y = [function(value) for value in x]
        except NameError:
            y = [value for value in x]

        return x, y

    # Метод для построения графика на холсте
    def plot_data(self):

        x, y = self.vectors()
        axes = plt.subplot()
        axes.plot(x, y)
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        # Обновление холста для отображения нового графика
        self.centralWidget().layout().itemAt(0).widget().draw()

    # Метод для очистки графика
    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        plt.grid(True)
        self.canvas.draw()

    # Метод для сохранения данных в файл
    def file_save(self):
        x, y = self.vectors()
        file = open('qwerty.txt', 'w')
        file.write('x     ' + '  ' + 'y\n')
        for i in range(len(x)):
            a, b = map(str, (x[i], y[i]))
            a, b = a[0:6], b[0:6]
            if len(a) < 6:
                a += '0' * (6 - len(a))
            if len(b) < 6:
                b += '0' * (6 - len(b))
            file.write(a + '  ' + b + '\n')

    # Метод для добавления пользовательской функции в выпадающий список
    def add_function(self):
        text_x = self.function_input.text()
        self.function_widget.addItems([text_x])

# Создание экземпляра приложения и главного окна
app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()


