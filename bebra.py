from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Визначник переможця')
button = QPushButton('Згенерувати')
text = QLabel('Натисни, щоб дізнатися переможця')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt. AlignCenter)
main_win.setLayout(line)
def show_winner():
    colors = ["червоний", "фіолетовий", "синій", "чорний", "зелений", "блакитний", "коричневий", "бордовий"]
    number = randint(0, len(colors) - 1)
    winner.setText(str(colors[number]))
    text.setText('Переможець:')
button.clicked.connect(show_winner)
main_win.show()
app.exec_()