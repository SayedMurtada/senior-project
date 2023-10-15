import sqlite3
from User import User

class DataBase:

    def __init__(self, name, db_type, host=None, username=None, password=None, path=None):
        self.name     = name
        self.db_type  = db_type
        self.host     = host
        self.username = username
        self.password = password
        self.path     = path

    def columns_sqlite(self, tables):
        if(sqlite3.connect(self.path)):
            result = []
            conn = sqlite3.connect(self.path)
            cur = conn.cursor()
            l = len(tables)
            for m in range(l):
                cur.execute("PRAGMA table_info('"+tables[m]+"');")
                schema = cur.fetchall()
                x = len(schema)
                for i in range(x):
                    sum =[]
                    sum.append(m)
                    sum.append(schema[i][1])
                    sum.append(schema[i][5])
                    result.append(sum)

            conn.close()
            return result
        else:
            print("Failed")
            return None



    def tables_sqlite(self):
        if (sqlite3.connect(self.path)):
            result = []
            conn = sqlite3.connect(self.path)
            cur = conn.cursor()
            cur.execute('''SELECT name, sql FROM sqlite_master
                            WHERE type='table'
                            ORDER BY name;''')
            schema = cur.fetchall()

            x = len(schema)
            for i in range(x):
                result.append(schema[i][0])
            # print(schema[0][0])
            conn.close()
            #print(*result, sep="\n")
            return result
        else:
            print("Failed")
            

class DataBase_Manage:

    def __init__(self, path="Data.sqlite3"):
        self.path     = path

    def connect(self):
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()
        print("connected")

    def add_user(self, user, pass_word):
        self.connect()

        table_name = "user"
        sr_col     = "Sr"
        user_col   = "username"
        pass_col   = "Pass"
        email_col  = "email"

        quary = "INSERT INTO {tn} ({user}, {password}, {email}) VALUES ('"+user.name+"','"+ pass_word+"','"+user.email+"')"

        try:
            self.c.execute(quary.\
                format(tn=table_name, user=user_col, password=pass_col, email=email_col))
        except sqlite3.IntegrityError:
            print('ERROR')
        self.conn.commit()
        self.conn.close()


    def get_user(self, username):
        self.connect()
        table_name = "user"
        sr_col     = "Sr"
        user_col   = "username"
        pass_col   = "Pass"
        email_col  = "email"
        quary      = 'SELECT * FROM {tn} WHERE {user}="'+username+'"'

        self.c.execute(quary.\
        format(tn=table_name, sr=sr_col, user=user_col, password=pass_col, email=email_col))
        user_row = self.c.fetchone()
        user = User(user_row[1], user_row[3])
        print(user_row)
        self.conn.close()
        return user, user_row[2]
    
    def add_db_host(self, usr, db):
        self.connect()

        table_name  = "Databases"

        sr_col      = "Sr"
        usr_col     = "User"
        name_col    = "Name"
        db_type_col = "type"
        host_col    = "Host"
        user_col    = "Username"
        password_col    = "Password"
        path_col    = "Path"

        quary = "INSERT INTO {tn} ({usr}, {name}, {type}, {host}, {username}, {password}) VALUES ('"+usr+"','"+db.name+"','"+db.db_type+"','"+ db.host+"','"+db.username+"','"+db.password+"')"
        print(quary)
        try:
            self.c.execute(quary.\
                format(tn=table_name, usr=usr_col, name=name_col, type=db_type_col, host=host_col, username=user_col, password=password_col))
        except sqlite3.IntegrityError:
            print('ERROR')
            return(False)

        self.conn.commit()
        self.conn.close()
        return(True)

    def add_db_path(self, usr, db):
        self.connect()

        table_name  = "Databases"

        sr_col      = "Sr"
        usr_col     = "User"
        name_col    = "Name"
        db_type_col = "type"
        path_col    = "Path"

        quary = "INSERT INTO {tn} ({usr}, {name}, {type}, {path}) VALUES ('"+usr+"','"+db.name+"','"+db.db_type+"','"+db.path+"')"

        try:
            self.c.execute(quary.\
                format(tn=table_name, usr=usr_col, name=name_col, type=db_type_col, path=path_col))
        except sqlite3.IntegrityError:
            print('ERROR')
            return(False)

        self.conn.commit()
        self.conn.close()
        return(True)

    def get_db(self, username):
        self.connect()
        print("hi")
        table_name = "Databases"
        usr_col     = "User"

        quary      = 'SELECT * FROM {tn} WHERE {user}="'+username+'"'

        self.c.execute(quary.\
        format(tn=table_name, user=usr_col))
        db = self.c.fetchall()
        self.conn.close()
        return db

    

    def check_user(self, user, password):
        self.connect()
        _, pass_word = self.get_user(user)
        if pass_word == password :
            self.conn.close()
            return True
        self.conn.close()
        return False

        

    def close(self):
        self.conn.commit()
        self.conn.close()


