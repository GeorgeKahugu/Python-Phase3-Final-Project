from test import cursor, conn

class Manager:

    def __init__(self, id, first_name, last_name, gender, Email, Phone_Number, No_of_Artists_Assigned):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.Email = Email
        self.Phone_Number = Phone_Number
        self.No_of_Artists_Assigned = No_of_Artists_Assigned


        
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
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT,
            Email TEXT,
            Phone_Number TEXT NOT NULL,
            No_of_Artists_Assigned INTEGER
            )
        """

        cursor.execute(sql, (self.first_name, self.last_name, self.gender, self.Email, self.Phone_Number, self.No_of_Artists_Assigned ))
        conn.commit()
    
    def __repr__(self):
        return f"<Manager('{self.first_name}', '{self.last_name}', '{self.gender}>"
         