from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sys
import os
from os import path

import mysql.connector
from mysql.connector import errorcode

import xlsxwriter

form_class, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handel_buttons()
        self.Handel_DataBase_Connection()

    def InitUI(self):
        self.setWindowTitle("Chess Manager")

    def Handel_DataBase_Connection(self):

        try:
            self.cnx = mysql.connector.connect(user='root', password='Leen2021!',
                                               host='localhost',
                                               database='mydb')
            self.cursor = self.cnx.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def eraseAllCarControls(self):
        self.red_steps.setCurrentIndex(0)
        self.blue_steps.setCurrentIndex(0)
        self.yellow_steps.setCurrentIndex(0)
        self.green_steps.setCurrentIndex(0)

    def Handel_buttons(self):
        self.btn_Add_Steps_Info.clicked.connect(self.Add_Steps_Info)

    def Add_Steps_Info(self):
        count = 1
        green = self.green_steps.currentIndex()
        yellow = self.yellow_steps.currentIndex()
        red = self.red_steps.currentIndex()
        blue = self.blue_steps.currentIndex()

        # Execute the SQL command
        self.cursor.execute("""INSERT INTO steps(green,yellow,red,blue)
                                VALUES(%s,%s,%s,%s)""", (green,yellow,red,blue))

        self.cnx.commit()
        print("Insertion Data Into DataBase Is Done")

        # Erase All Controls Contents
        self.eraseAllCarControls()

        while count < 7:
            count = count+1
        else:
            self.cursor.execute("SELECT player4 FROM users ORDER BY idusers DESC LIMIT 1")
            player4 = self.cursor.fetchall()
            print(player4[0][0])

            self.cursor.execute("SELECT player3 FROM users ORDER BY idusers DESC LIMIT 1")
            player3 = self.cursor.fetchall()
            print(player3[0][0])

            self.cursor.execute("SELECT player2 FROM users ORDER BY idusers DESC LIMIT 1")
            player2 = self.cursor.fetchall()
            print(player2[0][0])

            self.cursor.execute("SELECT player1 FROM users ORDER BY idusers DESC LIMIT 1")
            player1 = self.cursor.fetchall()
            print(player1[0][0])

            self.txt_Anonymous_green.setText(player4[0][0])
            self.txt_Anonymous_yellow.setText(player3[0][0])
            self.txt_Anonymous_blue.setText(player2[0][0])
            self.txt_Anonymous_red.setText(player1[0][0])

