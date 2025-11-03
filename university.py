import sqlite3
class University():
    def __init__(self, dbname="university.db"):
        self.dbname = dbname
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS university(
                id INT, name TEXT, age INT, grade INT)""")
            con.commit()

    def insert(self, id:int, name:str, age:int, grade:int):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO university(id,name,age,grade) VALUES (?, ?, ?, ?);",
                        (id, name, age, grade))
            con.commit()

    def update(self, grade:int, id:int):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("UPDATE university SET grade = ? WHERE id = ?;", (grade, id))
            con.commit()

    def delete(self, id:int):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM university WHERE id = ?;", (id,))
            con.commit()

    def filter(self):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT name FROM university WHERE age > 18")
            return cur.fetchall()

    def summ(self):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM university")
            return len(cur.fetchall())

    def read(self):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM university")
            return cur.fetchall()

    def find(self, name:str):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM university WHERE name = ?;", (name,))
            return cur.fetchall()
if __name__ == "__main__":
    obj = University()
    run = ""
    function = ""
    while True:
        run = input("run or exit ")
        if run == "exit":
            break
        
        elif run == "run":
            function=input("insert read update delete summ filter find ")
            if function == "insert":
                id = int(input())
                name = input()
                age = int(input())
                grade =int(input())
                obj.insert(id,name,age,grade)
            elif function == "update":
                id = int(input())
                grade = int(input())
                obj.update(grade,id)
            elif function == "delete":
                id = int(input())
                obj.delete(id)
            elif function == "summ":
                print(obj.summ())
            elif function == "filter":
                print(obj.filter())
            elif function == "read":
                for i in obj.read():
                    print(*i)
            elif function == "find":
                name = input()
                print(obj.find(name))
