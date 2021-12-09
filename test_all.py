import pytest
import os


pathOS = os.getcwd()


#Testing the Database
def test_DB():
    import sqlite3

    #connect to the chessDB.db file
    conn = sqlite3.connect('chessDB.db')

    #cursor object
    cursorObj = conn.cursor()

    #SQL statement
    #Select all tables
    cursorObj.execute("select name from sqlite_master where type='table' and name='game'")

    #Get the result of SQL statement
    x = cursorObj.fetchall()

    #If there is any table inside the database
    assert len(x) != 0

    #SQL
    #Select all game_ids
    cursorObj.execute("""SELECT game_id FROM game GROUP BY game_id""")
    x = cursorObj.fetchall()

    #If there is any game_id
    assert len(x) > 0

    #close the connection
    conn.close()

#Testing the color parser
def test_colorParser():
    from scraper.main import color_parser

    #Test if the color parser is working properly
    assert color_parser("color: rgb(192, 149, 38)") == 'Yellow'
    assert color_parser("color: rgb(65, 133, 191)") == 'Blue'
    assert color_parser("color: rgb(65, 133, 191)") != 'Red'
    assert color_parser("color: rgb(192, 149, 38)") != 'Green'

#Testing the Database_2
def test_DB2():
    import sqlite3

    conn = sqlite3.connect('chessDB.db')

    cursorObj = conn.cursor()
    cursorObj.execute("SELECT name from sqlite_master where type='table' and name='game'")


    x = cursorObj.fetchall()
    assert len(x) != 0

    # SQL
    # Select all round_nr
    cursorObj.execute("""SELECT round_nr FROM game""")
    x = cursorObj.fetchall()

    #if there are more than 10 rounds
    assert len(x) > 10

    conn.close()


