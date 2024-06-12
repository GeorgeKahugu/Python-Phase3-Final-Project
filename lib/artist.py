from test import cursor, conn

class Artist:

    def __init__(self, Artist_name, Gender, Email, Genre_of_Music, No_of_songs_assigned, Manager_assigned, id= None):
        self.id = id
        self.Artist_Name = Artist_name
        self.Gender = Gender
        self.Email = Email
        self.Genre_of_Music = Genre_of_Music
        self.No_of_songs_Assigned = No_of_songs_assigned
        self.Manager_Assigned = Manager_assigned

     
    @classmethod
    def create_table(cls):
        '''This method will create an Artist table in our db'''
        sql = """
            CREATE TABLE Artist (
            id INTEGER PRIMARY KEY,
            Artist_Name TEXT NOT NULL,
            Gender TEXT,
            Email TEXT,
            Genre_of_Music TEXT,
            No_of_songs_Assigned INTEGER
            Manager_Assigned TEXT     
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
           DROP TABLE IF EXISTS Artist
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
           INSERT INTO Artist(
            Artist_Name ,
            Gender,
            Email,
            Genre_of_Music ,
            No_of_songs_Assigned,
            Manager_Assigned,     
            )VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(sql, (self.Artist_Name, self.Gender,  self.Email, self.Genre_of_Music, self.No_of_songs_Assigned, self.Manager_Assigned))
        conn.commit()
       
        self.id = cursor.latrowid
        print(self.id)
       
    
    def __repr__(self):
        return f"<Artist('{self.Artist_Name}', '{self.Gender}, '{self.Email}'>"
         