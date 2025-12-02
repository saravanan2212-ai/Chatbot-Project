import sqlite3, time

def init_db(path='chatlogs.db'):
    conn = sqlite3.connect(path)
    conn.execute('''CREATE TABLE IF NOT EXISTS logs
        (id INTEGER PRIMARY KEY, session TEXT, user TEXT, bot TEXT, ts INTEGER)''')
    conn.commit()
    conn.close()

def log(session, user, bot, path='chatlogs.db'):
    conn = sqlite3.connect(path)
    conn.execute("INSERT INTO logs(session,user,bot,ts) VALUES(?,?,?,?)",
                 (session, user, bot, int(time.time())))
    conn.commit()
    conn.close()
