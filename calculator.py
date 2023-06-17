from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from calculator_logic import CalculatorLogic

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setup_ui()
        self.calculator_logic = CalculatorLogic()

    def setup_ui(self):
        # Create the UI elements
        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # Create buttons layout
        buttons_layout = QVBoxLayout()
        for row in buttons:
            hbox = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.button_clicked)
                hbox.addWidget(button)
            buttons_layout.addLayout(hbox)

        # Create the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(buttons_layout)

        # Set the main layout for the window
        self.setLayout(main_layout)

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        print(text)

        if text == '=':
            # Evaluate the expression and display the result
            expression = self.line_edit.text()
            result = self.calculator_logic.evaluate_expression(expression)
            self.line_edit.setText(str(result))
        else:
            # Append the clicked button text to the line edit
            self.line_edit.setText(self.line_edit.text() + text)
