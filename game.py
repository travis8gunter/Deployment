import sqlite3

def dict_factory(cursor, row):
 fields = []
 for column in cursor.description:
    fields.append(column[0])

 result_dict = {}
 for i in range(len(fields)):
    result_dict[fields[i]] = row[i]

 return result_dict

class GamesDB:
    def __init__(self,filename):
        #connect to DB file
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def getAll(self):
        self.cursor.execute("SELECT * FROM games")
        return self.cursor.fetchall()
    
    def getOne(self,game_id):
        data = [game_id]
        self.cursor.execute("SELECT * FROM games WHERE id = ?",data)
        return self.cursor.fetchone()

    def create(self,title, genre, rating, multiplayer, price):
        data = [title, genre, rating, multiplayer, price]
        #add a new game to our db
        self.cursor.execute("INSERT INTO games(title, genre, rating, multiplayer, price)VALUES(?,?,?,?,?)",data)
        self.connection.commit()
        return True
    
    def update(self, title, genre, rating, multiplayer, price, game_id):
        data = [title, genre, rating, multiplayer, price, game_id]
        self.cursor.execute("UPDATE games SET title = ?, genre = ?, rating = ?, multiplayer = ?, price = ? WHERE id = ?", data)
        self.connection.commit()

    def delete(self, game_id):
       data = [game_id]
       self.cursor.execute("DELETE FROM games WHERE id = ?", data)
       self.connection.commit()
       return True
    
    def createUser(self,fisrt_name,last_name,email,password):
        data = [first_name, last_name, email, password]
   #add new user to our DB
        self.cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES(?,?,?,)",data)
        self.connection.commit()

    def get_user_by_email(self,email):
        data = [email]
        self.cursor.execute("SELECT * FROM users WHERE email = ?", data)
        user = self.cursor.fetchone()
        return 


    def close(self):
       self.connection.close()
       return True
    

