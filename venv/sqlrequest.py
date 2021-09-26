import sqlite3

db = sqlite3.connect('PampkinChat')
sql = db.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS users_online (
        login TEXT,
        Password TEXT,
        online INT,
        user_id TEXT
    )""")

db.commit()


def chek_User(user_login, user_password = 1):
    global sql
    global id
    print(f"USERNAME IN DB = {user_login}")
    sql.execute(f"SELECT login, Password FROM users WHERE login= '{user_login}' AND Password = '{user_password}'")
    if sql.fetchone() is None:
        print("Wrong username or passsword")
        return False
    else:
        print(f"Добро Пожаловать в Chat, {user_login}")
        # set online to 1
        sql.execute(f"UPDATE users SET online = '{1}'WHERE login= '{user_login}' ")
        db.commit()
        return True, user_login







def Disconection(user_login):
    global sql
    global id
    # set online to 0
    sql.execute(f"UPDATE users_online SET online = '{0}'WHERE login= '{user_login}' ")
    db.commit()



























"""def chek_User(user_login, user_password = 1):
    global sql
    global id
    sql.execute(f"SELECT login, Password FROM users_online WHERE login= '{user_login}' AND Password = '{user_password}'")
    if sql.fetchone() is None:
        newLogin = input("Wrong username or passsword \nIf you want to log in Press 1 else Press enter")
        if newLogin == "1":
            sql.execute(f"INSERT INTO users_online VALUES (?,?,?,?)",(user_login,user_password, 1, id))
            db.commit()
        else:
            for value in sql.execute("SELECT * FROM users_online"):
                print(value)
            print("Bye Bye")
    else:
        print(f"Добро Пожаловать в Chat, {user_login}")
        return True, user_login"""