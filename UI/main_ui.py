from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QApplication
from workflow.quote_generation import QuoteGeneration
from time import sleep


class UserInterface(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.UI_DIRS = "UI/gui.ui"
        self.setupUI()
        self.clickedbutton()

    def setupUI(self):
        """ ЗАГРУЖАЕМ ИНТЕРФЕЙСТ ИЗ UI ФАЙЛА """
        self.ui = uic.loadUi(self.UI_DIRS, self)


        

        """ ФИЛЬМЫ """
        self.list_films = [
            self.tr("Джентльмены (The Gentlemen)"),
            self.tr("Крестный отец (The Godfather)"),
            self.tr("Джокер (Joker) (2012)"),
            self.tr("Сумерки (Twilight)"),
            self.tr("1+1 / Неприкасаемые (The Intouchables)"),
            self.tr("Матрица (The Matrix)"),
            self.tr("Мирный воин (Peaceful Warrior)"),
            self.tr("Бойцовский клуб (Fight Club)"),
            self.tr("Титаник (Titanic)"),
            self.tr("Ешь, молись, люби (Eat Pray Love)"),
        ]
        self.comboBox_2.addItems(self.list_films)

    def clickedbutton(self):
        self.ui.pushButton.clicked.connect(self.generateText)
        
    def generateText(self):
       
        self.quote = QuoteGeneration()
        x = self.quote.generation()
        self.ui.label.setText(x)
    

