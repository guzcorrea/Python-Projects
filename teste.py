import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget, 
                               QVBoxLayout, QLineEdit, QPushButton)

from pathlib import Path
import qdarktheme


ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'icon.png'



class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        
        self.display = QLineEdit()
        self.layout.addWidget(self.display)
       
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '+',
            '0', '.', '=', '-',
        ]
    
        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_click)
            self.layout.addWidget(button)

    
        self.central_widget.setLayout(self.layout)
    
    def button_click(self):
        button = self.sender()
        current_text = self.display.text()  
        
        if button.text() == '=':
            try:
                result = eval(current_text)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:      
            self.display.setText(current_text + button.text())
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    window = Calculator()
    
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)
    
    app.setStyleSheet(qdarktheme.load_stylesheet('dark'))
    
    window.show()
    sys.exit(app.exec())