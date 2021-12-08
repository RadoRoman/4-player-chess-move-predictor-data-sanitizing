from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType


import sys
from os import path

import mysql.connector
from mysql.connector import errorcode

from manager import MainApp
import xlsxwriter

'''reaching into the ui template'''
form_class, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))
form_class2, _ = loadUiType(path.join(path.dirname(__file__), "Start.ui"))

'''define attributes'''
class StartGame(QMainWindow, form_class2):
    def __init__(self, parent=None):
        super(StartGame, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Start.clicked.connect(self.Handel_Start)
        self.window2 = None

    def Handel_Start(self):
        '''connecting to database'''
        self.cnx = mysql.connector.connect(user='root', password='Leen2021!',
                                           host='localhost',
                                           database='mydb')
        self.cursor = self.cnx.cursor()

        '''identifying the bars inputs in the first template'''
        player1 = self.txt_First_Player.text()
        player2 = self.txt_Second_Player.text()
        player3 = self.txt_Third_Player.text()
        player4 = self.txt_Fourth_Player.text()

        # Execute the SQL command
        self.cursor.execute("""INSERT INTO users(player1,player2,player3,player4)
                                VALUES(%s,%s,%s,%s)""", (player1, player2, player3, player4))

        self.cnx.commit()
        print("Insertion of players Is Done")

        #Check if all players joined the game
        if len(player1 and player2 and player3 and player4):
            self.window2 = MainApp()
            self.close()
            self.window2.show()
        else:
            self.label_MMessages.setText("please enter all players' names")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window = StartGame()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
