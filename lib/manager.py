
from test import cursor, conn      

#Define the Manager class
class Manager:

    def __init__(self, first_name, last_name, gender, email, phone_number, genre, no_of_artists_assigned, id = None):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._email = email
        self._phone_number = phone_number
        self._genre = genre
        self._no_of_artists_assigned = no_of_artists_assigned

#Property and setter methods for the Manager attributes
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
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter 
    def phone_number(self, value):
        self._phone_number = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def no_of_artists_assigned(self):
        return self._no_of_artists_assigned

    @no_of_artists_assigned.setter
    def no_of_artists_assigned(self, value):
        self._no_of_artists_assigned = value

#Calling the class methods ORM using CRUD operations specifically(create,delete,get all and find by id) as per the brief  
#Create the manager table
    @classmethod
    def create_table(cls):
        '''This method will create a manager table in our db'''
        sql = """
            CREATE TABLE manager (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT,
            email TEXT,
            phone_number TEXT NOT NULL,
            genre TEXT,
            no_of_artists_Assigned INTEGER
            )
        """
        cursor.execute(sql)
        conn.commit()

#Drop the manager table
    @classmethod
    def drop_table(cls):
        sql = """
           DROP TABLE IF EXISTS manager
        """
        cursor.execute(sql)
        conn.commit()
        
#Save the manager to the database
    def save(self):
        sql = """
            INSERT INTO manager (
            first_name,
            last_name,
            gender,
            email,
            phone_number,
            genre,
            no_of_artists_assigned
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self._first_name, self._last_name, self._gender, self._email, self._phone_number, self._genre, self._no_of_artists_assigned))
        conn.commit()
        
        self._id = cursor.lastrowid
        print(self._id)

#Delete the manager from the database
    def delete(self):
        if self._id is None:
            raise ValueError("manager must have an id to be deleted")
        sql = "DELETE FROM manager WHERE id = ?"
        cursor.execute(sql, (self._id,))
        conn.commit()
        self._id = None

#Find a manager by ID
    @classmethod
    def find_by_id(cls, manager_id):
        sql = "SELECT * FROM manager WHERE id = ?"
        cursor.execute(sql, (manager_id,))
        row = cursor.fetchone()
        if row:
            return cls(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                gender=row[3],
                email=row[4],
                phone_number=row[5],
                genre=row[6],
                no_of_artists_assigned=row[7]
            )
        return None
    
#Get all managers from the database
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM manager"
        cursor.execute(sql)
        rows = cursor.fetchall()
        managers = []
        for row in rows:
            manager = cls(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                gender=row[3],
                email=row[4],
                phone_number=row[5],
                genre=row[6],
                no_of_artists_assigned=row[7]
            )
            manager.append(manager)
        return managers

   
#String representation of the manager
    def __repr__(self):
        return f"<manager('{self._first_name}', '{self._last_name}', '{self._gender}')>"


