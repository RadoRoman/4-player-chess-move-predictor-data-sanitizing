import pytest


import json
import os, sys
import re

pathOS = os.getcwd()



def test_DB():
    import sqlite3

    conn = sqlite3.connect('chessDB.db')

    cursorObj = conn.cursor()
    cursorObj.execute("select name from sqlite_master where type='table' and name='game'")
    x = cursorObj.fetchall()
    assert len(x) != False

    cursorObj.execute("""SELECT game_id FROM game GROUP BY game_id""")
    x = cursorObj.fetchall()
    assert len(x) > 0

    conn.close()

def test_colorParser():
    from scraper.main import color_parser


    assert color_parser("color: rgb(192, 149, 38)") == 'Yellow'
    assert color_parser("color: rgb(65, 133, 191)") == 'Blue'
    assert color_parser("color: rgb(65, 133, 191)") != 'Red'
    assert color_parser("color: rgb(192, 149, 38)") != 'Green'


def test_DB2():
    import sqlite3

    conn = sqlite3.connect('chessDB.db')

    cursorObj = conn.cursor()
    cursorObj.execute("SELECT name from sqlite_master where type='table' and name='game'")
    x = cursorObj.fetchall()
    assert len(x) != False

    cursorObj.execute("""SELECT round_nr FROM game""")
    x = cursorObj.fetchall()
    assert len(x) > 10

    conn.close()
