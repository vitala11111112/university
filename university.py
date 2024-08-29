import sqlite3
class University():
    def __init__(self):
        self.con = sqlite3.connect("university.db")
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS university(id INT,name TEXT,age INT,grade INT)""")
        self.con.commit()
    def insert(self,id:int,name:str,age:int,grade:int):
        self.cur.execute(f"""INSERT INTO university(id,name,age,grade) values({id},'{name}',{age},{grade});""")
        self.con.commit()
    def update(self,grade:str,id:int):
        self.cur.execute(f"""UPDATE university SET grade = {grade} WHERE id = {id} ;""")
        self.con.commit()
    def delete(self,id:int):
        self.cur.execute(f"""DELETE FROM university WHERE id = {id};""")
        self.con.commit()
    def filter(self):
        self.cur.execute("""SELECT name FROM university WHERE age > 18""")
        students = self.cur.fetchall()
        self.con.commit()
        return students
    def summ(self):
        self.cur.execute("""SELECT * FROM university""")
        students = self.cur.fetchall()
        self.con.commit()
        return len(students)
    def read(self):
        self.cur.execute("""SELECT * FROM university""")
        students = self.cur.fetchall()
        self.con.commit()   
        return students   
    def find(self,name:str):
        self.cur.execute(f"""SELECT * FROM university WHERE name = '{name}' ;""")
        students = self.cur.fetchall()
        self.con.commit() 
        return students
if __name__ == "__main__":
    obj = University()
    run = ""
    function = ""
    while True:
        run = input()
        function = input()
        if run == "exit":
            break
        
        elif run == "run":
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
