import sqlite3
# Run this only once - to create the tables
conn = sqlite3.connect('chessDB.db')
cursorObj = conn.cursor()
cursorObj.execute("""CREATE TABLE "users" (
                        "id"	TEXT,
                        "name"	TEXT,
                        PRIMARY KEY("id")
                     )""")

cursorObj.execute("""CREATE TABLE "games" (
                        "player_id"	TEXT,
                        "game_moves"	TEXT,
                        "gameNr"	INTEGER PRIMARY KEY AUTOINCREMENT,
                        FOREIGN KEY("player_id") REFERENCES "users"("id")
                     )""")

# Add sample users
sampleUserData = [{"id": 1, "name": "uuyytee"},
                    {"id": 2, "name": "george56789"},
                    {"id": 3, "name": "papabellotas2"},
                    {"id": 4, "name": "kuprabhu",},
                 ]

sqlite_insert_with_param = """INSERT INTO users
                          (id, name) 
                          VALUES (?, ?);"""
for user in sampleUserData:
    data_tuple = (user["id"], user["name"])
    cursorObj.execute (sqlite_insert_with_param, data_tuple)
    conn.commit()