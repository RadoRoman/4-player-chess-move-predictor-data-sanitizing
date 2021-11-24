import sqlite3


#SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
def DB():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        sqlite_create_table_query = '''CREATE TABLE chess (
                                    id INTEGER PRIMARY KEY,
                                    player_name TEXT NOT NULL,
                                    game_info TEXT NOT NULL,
                                    moves TEXT NOT NULL,
                                    game_id_nr INTEGER NOT NULL,
                                    round INTEGER NOT NULL);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
