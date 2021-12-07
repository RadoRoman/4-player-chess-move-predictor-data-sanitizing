import sqlite3
import pandas as pd
import json
import os, sys

#path = os.getcwd()
#x = os.path.abspath(os.path.join(path, os.pardir))
#print(x)
#sys.path.insert(1, x+'\\scraper')

#from scraper import scraper as tester

#Run this only once - to create the tables

#create a connection



def getChessDb(JSON):

    conn = sqlite3.connect('chessDB.db')
    cursorObj = conn.cursor()
    cursorObj.execute("select name from sqlite_master where type='table' and name='game'")
    x = cursorObj.fetchall()
    if len(x) == 0:
        cursorObj.execute(""" CREATE TABLE game (
                                "id" INTEGER PRIMARY KEY,
                                "game_id" INTEGER(10) NOT NULL,
                                "username" VARCHAR(255)  NOT NULL,
                                "round_nr" VARCHAR(5)  NOT NULL,
                                "moves_time" TEXT NOT NULL,
                                "color" VARCHAR(10)  NOT NULL
        )""")

    for GameNr in JSON.keys():
        for data in JSON[GameNr]:
            username = data['username']
            round_nr = data['round_nr']
            moves_time = data['moves-time']
            color = data['color']

            cursorObj.execute("""INSERT INTO game(game_id, username, round_nr, moves_time, color) VALUES 
                                (?,?,?,?,?)""",
                              (GameNr, username, round_nr, moves_time, color))
    conn.commit()
    conn.close()
#getChessDb()
