import sqlite3


def Chess_db(JSON):

    conn = sqlite3.connect('chessDB.db')
    cursorObj = conn.cursor()
    cursorObj.execute("select name from sqlite_master where type='table' and name='game'")
    x = cursorObj.fetchall()
    if len(x) == 0:
        cursorObj.execute(""" CREATE TABLE game (
                                "id" INTEGER PRIMARY KEY,
                                "game_id" INTEGER(20) NOT NULL,
                                "username" VARCHAR(255)  NOT NULL,
                                "round_nr" INTEGER(10)  NOT NULL,
                                "moves" VARCHAR(255) NOT NULL,
                                "time" TEXT NOT NULL,
                                "color" VARCHAR(10)  NOT NULL
        )""")

    for GameNr in JSON.keys():
        for data in JSON[GameNr]:
            username = data['username']
            round_nr = data['round_nr']
            moves = data['moves']
            time = data['time']
            color = data['color']

            cursorObj.execute("""INSERT INTO game(game_id, username, round_nr, moves, time, color) VALUES 
                                (?,?,?,?,?,?)""",
                              (GameNr, username, round_nr, moves, time, color))
    conn.commit()
    conn.close()

