
from test import cursor, conn      

class Manager:

    def __init__(self, first_name, last_name, gender, Email, Phone_Number, Team, No_of_Artists_Assigned, id=None):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._Email = Email
        self._Phone_Number = Phone_Number
        self._Team = Team
        self._No_of_Artists_Assigned = No_of_Artists_Assigned

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, value):
        self._Email = value

    @property
    def Phone_Number(self):
        return self._Phone_Number

    @Phone_Number.setter
    def Phone_Number(self, value):
        self._Phone_Number = value

    @property
    def Team(self):
        return self._Team

    @Team.setter
    def Team(self, value):
        self._Team = value

    @property
    def No_of_Artists_Assigned(self):
        return self._No_of_Artists_Assigned

    @No_of_Artists_Assigned.setter
    def No_of_Artists_Assigned(self, value):
        self._No_of_Artists_Assigned = value

    @classmethod
    def create_table(cls):
        '''This method will create a Manager table in our db'''
        sql = """
            CREATE TABLE Manager (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT,
            Email TEXT,
            Phone_Number TEXT NOT NULL,
            Team TEXT,
            No_of_Artists_Assigned INTEGER
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
           DROP TABLE IF EXISTS Manager
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO Manager (
            first_name,
            last_name,
            gender,
            Email,
            Phone_Number,
            Team,
            No_of_Artists_Assigned
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self._first_name, self._last_name, self._gender, self._Email, self._Phone_Number, self._Team, self._No_of_Artists_Assigned))
        conn.commit()
        
        self._id = cursor.lastrowid
        print(self._id)

    def delete(self):
        if self._id is None:
            raise ValueError("Manager must have an id to be deleted")
        sql = "DELETE FROM Manager WHERE id = ?"
        cursor.execute(sql, (self._id,))
        conn.commit()
        self._id = None

    @classmethod
    def find_by_id(cls, manager_id):
        sql = "SELECT * FROM Manager WHERE id = ?"
        cursor.execute(sql, (manager_id,))
        row = cursor.fetchone()
        if row:
            return cls(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                gender=row[3],
                Email=row[4],
                Phone_Number=row[5],
                Team=row[6],
                No_of_Artists_Assigned=row[7]
            )
        return None

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM Manager"
        cursor.execute(sql)
        rows = cursor.fetchall()
        managers = []
        for row in rows:
            manager = cls(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                gender=row[3],
                Email=row[4],
                Phone_Number=row[5],
                Team=row[6],
                No_of_Artists_Assigned=row[7]
            )
            managers.append(manager)
        return managers

   

    def __repr__(self):
        return f"<Manager('{self._first_name}', '{self._last_name}', '{self._gender}')>"


