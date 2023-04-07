import sqlite3


class TodoDB:

    con = None

    @staticmethod
    def connectToDatabase():
        try:
            TodoDB.con = sqlite3.connect('todo.db', check_same_thread=False)
            c = TodoDB.con.cursor()
            c.execute(f'CREATE TABLE IF NOT EXISTS tasks '
                      f'(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                      f'todo_content TEXT NOT NULL,'
                      f'todo_date TEXT NOT NULL,'
                      f'todo_time TEXT,'
                      f'completed NUMERIC NOT NULL,'
                      f'reg_date TEXT NOT NULL)')
            c.execute(f'CREATE TABLE IF NOT EXISTS users '
                      f'(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                      f'user_name TEXT NOT NULL,'
                      f'user_gender TEXT NOT NULL,'
                      f'user_id TEXT NOT NULL,'
                      f'user_pw TEXT NOT NULL,'
                      f'user_email TEXT NOT NULL,'
                      f'user_mobile TEXT NOT NULL,'                      
                      f'reg_date TEXT NOT NULL)')
            TodoDB.con.commit()
        except Exception as e:
            print(e)

    def readTodos(self):
        c = TodoDB.con.cursor()
        c.execute('SELECT * FROM tasks')
        res = c.fetchall()
        return res

    def insertTodo(self, values):
        c = TodoDB.con.cursor()
        c.execute('INSERT INTO tasks (todo_content, todo_date, todo_time, completed, reg_date)'
                  ' VALUES (?, ?, ?, ?, ?)', values)
        TodoDB.con.commit()
        return c.lastrowid

    def deleteTodo(self, id):
        c = TodoDB.con.cursor()
        c.execute(f'DELETE FROM tasks WHERE id={id}')
        TodoDB.con.commit()

    def updateTodo(db, values):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_content=?, todo_date=?, todo_time=?,'
                  ' completed=? WHERE id=?', values)
        TodoDB.con.commit()

    def updateTaskState(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET completed=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()

    def updateTodoContent(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_content=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()

    def updateTodoDate(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_date=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()

    def updateTodoTime(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_time=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()

    def readUsers(self):
        c = TodoDB.con.cursor()
        c.execute('SELECT * FROM users')
        res = c.fetchall()
        return res

    def insertUser(self, values):
        c = TodoDB.con.cursor()
        c.execute('INSERT INTO users (user_name, user_gender, '
                  'user_id, user_pw, '
                  'user_email, user_mobile, reg_date)'
                  ' VALUES (?, ?, ?, ?, ?, ?, ?)', values)
        TodoDB.con.commit()
        return c.lastrowid

    def deleteUser(self, id):
        c = TodoDB.con.cursor()
        c.execute(f'DELETE FROM users WHERE id={id}')
        TodoDB.con.commit()

    def updateUser(db, values):
        c = TodoDB.con.cursor()
        c.execute('UPDATE users SET user_name=?, user_gender=?, user_pw=?,'
                  'user_email=?, user_mobile=? WHERE id=?', values)
        TodoDB.con.commit()

"""
import sqlite3

class TodoDB:  # 혹시 뭔가 상속 받으면 TodoDB(DB): 이런 식으로 작성
    # 클래스 정의(클래스 변수: "붕어빵 틀") => 객체 생성(객체 or 멤버 변수: "붕어빵") self 메서드

    # 클래스 변수
    con = None

    def connectToDatabase(self):
        try:  # 항상 예외 처리를 해야 함
            TodoDB.con = sqlite3.connect('todo.db', check_same_thread=False)  # DB 생성
            c = TodoDB.con.cursor()  # 커서: 명령 준비!!!
            c.execute('CREATE TABLE IF NOT EXISTS tasks '  # SQL: standard Query Language 
                      # < 대·소문자 구분은 없음 but 관례: 기본 문법은 대문자, 변수는 소문자 사용
                      '('
                      'id INTEGER PRIMARY KEY AUTOINCREMENT, '  # id를 정수로 PRIMARY KEY 설정(식별자)
                      'todo_content TEXT NOT NULL,'
                      'todo_date TEXT NOT NULL,'
                      'todo_time TEXT NOT NULL,'
                      'completed NUMERIC NOT NULL,'  # 과거는 질문임. Is completed? >> YES(0 제외) or NO(0)
                      'reg_date TEXT NOT NULL'
                      ')')
            c.execute('CREATE TABLE IF NOT EXISTS users '  # 테이블 이름은 주로 복수
                      '('
                      'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                      'user_name TEXT NOT NULL,'
                      'user_gender TEXT NOT NULL,'
                      'user_id TEXT NOT NULL,'
                      'user_pw TEXT NOT NULL,'
                      'user_email TEXT NOT NULL,'
                      'user_mobile TEXT NOT NULL,'
                      'reg_date TEXT NOT NULL'
                      ')')
            TodoDB.con.commit()  # 이걸 해야지 메모리에서 하드디스크로 넘어감!
        except Exception as e:  # Exception: 예외를 처리하는 최상위 클래스, e는 객체
            print(e)

    def readTodos(self):
        c = TodoDB.con.cursor()
        c.execute('SELECT * FROM tasks')  # *: 전부 불러오기
        res = c.fetchall()  # 표(2차원 배열)
        return res

    def insertTodo(self, values):
        c = TodoDB.con.cursor()
        c.execute('INSERT INTO tasks ('  # 속성 목록(생략 가능=모든 것 가능), 값 목록
                  'todo_content, todo_date, todo_time, completed, reg_date'
                  ') VALUES (?,?,?,?,?)', values)  # 순서대로 대입
        TodoDB.con.commit()
        return c.lastrowid

    def deleteTodo(self, id):
        c = TodoDB.con.cursor()
        c.execute(f'DELETE FROM tasks WHERE id={id}')
        TodoDB.con.commit()

    def updateTodo(self, values):
        c = TodoDB.con.cursor()
        c.execute(f'UPDATE tasks SET todo_content=?, todo_date=?, todo_times=?,'
                  f'completed=? WHERE id=?', values)
        TodoDB.con.commit()
"""