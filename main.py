import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class Focus(QWidget):
    def __init__(self):
        super(Focus, self).__init__()

        self.arrow = 1

        self.setFixedSize(300, 50)
        self.setWindowTitle('Фокус со словами')

        self.input_text = QLineEdit(self)
        self.input_text.move(10, 10)
        self.input_text.resize(120, 30)

        self.button = QPushButton('->', self)
        self.button.resize(30, 30)
        self.button.move(135, 10)
        self.button.clicked.connect(self.convert)

        self.output_text = QLineEdit(self)
        self.output_text.move(170, 10)
        self.output_text.resize(120, 30)

    def convert(self):
        if self.arrow:
            self.output_text.setText(self.input_text.text())
            self.input_text.clear()

            self.button.setText('<-')

            self.arrow = 0
        else:
            self.input_text.setText(self.output_text.text())
            self.output_text.clear()

            self.button.setText('->')

            self.arrow = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Focus()
    widget.show()
    sys.exit(app.exec())