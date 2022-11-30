from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QApplication
from workflow.quote_generation import QuoteGeneration
from time import sleep
import pyperclip


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
            self.tr("Джентльмены"),
            self.tr("Крестный отец"),
            self.tr("Неприкасаемые"),
            self.tr("Матрица"),
            self.tr("Бойцовский клуб"),
        ]
        self.comboBox_2.addItems(self.list_films)

    def clickedbutton(self):
        self.ui.pushButton.clicked.connect(self.generateText)
        self.ui.pushButton_2.clicked.connect(self.copy_to_clipboard)
        
    def generateText(self):
        self.dzhentelmens = "dzhentlmeny-the-gentlemen"
        self.krestnyi_otec_the_godfather = "krestnyi-otec-the-godfather"
        self.neprikasaemye = "1-1-neprikasaemye-the-intouchables"
        self.matrica_the_matrix = "matrica-the-matrix"
        self.boicovskii_klub = "boicovskii-klub-fight-club"

        self.item_film = self.ui.comboBox_2.currentText()
        
        
        if self.item_film == "Джентльмены":
            self.quote = QuoteGeneration("https://citaty.info/movie/dzhentlmeny-the-gentlemen")
            self.x = self.quote.generation()
            self.ui.label.setText(self.x)

        elif self.item_film == "Крестный отец":
            self.quote = QuoteGeneration("https://citaty.info/movie/krestnyi-otec-the-godfather")
            self.x = self.quote.generation()
            self.ui.label.setText(self.x)

        elif self.item_film == "Неприкасаемые":
            self.quote = QuoteGeneration("https://citaty.info/movie/1-1-neprikasaemye-the-intouchables")
            self.x = self.quote.generation()
            self.ui.label.setText(self.x)

        elif self.item_film == "Матрица":
            self.quote = QuoteGeneration("https://citaty.info/movie/matrica-the-matrix")
            self.x = self.quote.generation()
            self.ui.label.setText(self.x)

        elif self.item_film == "Бойцовский клуб":
            self.quote = QuoteGeneration("https://citaty.info/movie/boicovskii-klub-fight-club")
            self.x = self.quote.generation()
            self.ui.label.setText(self.x)
        
    
    def copy_to_clipboard(self):
        self.x = self.ui.label.text()
        pyperclip.copy(self.x)
        print(self.x)

