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

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("id must be an integer")
        self._id = value
    
    @property
    def Artist_Name(self):
        return self._Artist_Name


    @Artist_Name.setter
    def Artist_Name(self, value):
        if not isinstance(value,str):
            raise TypeError("Artist Name must be a string")
        self._Artist_Name = value

    @property
    def Gender(self):
        return self._Gender
    
    @Gender.setter
    def Gender(self,value):
        if value not in ["Male", "Female", "Other"]:
            raise ValueError("Gender must be Male, Female or Other")
        self._Gender = value

    @property
    def Email(self):
        return self._Email
    @Email.setter
    def Email(self,value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self._Email = value
    
    @property
    def Genre_of_Music(self):
        return self._Genre_of_Music
    
    @Genre_of_Music.setter
    def Genre_of_Music(self, value):
        if not isinstance(value, str):
            raise TypeError("Genre of Music must be a string")
        self._Genre_of_Music = value

    @property
    def No_of_songs_Assigned(self):
        return self._No_of_songs_Assigned
    @No_of_songs_Assigned.setter
    def No_of_songs_Assigned(self, value):
        if not isinstance(value, int):
            raise TypeError("No of songs assigned must be an integer")
        self._No_of_songs_Assigned = value

    @property
    def Manager_Assigned(self):
        return self._Manager_Assigned
    
    @Manager_Assigned.setter
    def Manager_Assigned(self, value):
        if not isinstance(value, str):
            raise TypeError("Manager Assigned must be a string")
        self._Manager_Assigned = value
    
     
    #implementation of the classmethods 
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
            No_of_songs_Assigned INTEGER,
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
            Manager_Assigned     
            )VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(sql, (self.Artist_Name, self.Gender,  self.Email, self.Genre_of_Music, self.No_of_songs_Assigned, self.Manager_Assigned))
        conn.commit()
       
        self.id = cursor.lastrowid
        print(self.id)
       
    def delete(self):
        if self.id is None:
            raise Exception("You can't delete an Artist that doesn't exist")
        sql = "DELETE FROM Artist WHERE id = ?"
        cursor.execute(sql, (self._id,))
        conn.commit()
        self.id = None


    @classmethod
    def find_by_id(cls, artist_id):
        sql = "SELECT * FROM Artist WHERE id = ?"
        cursor.execute(sql, (artist_id,))
        row = cursor.fetchone()
        if row:
            return cls(
                Artist_name=row[1],
                Gender=row[2],
                Email=row[3],
                Genre_of_Music=row[4],
                No_of_songs_assigned=row[5],
                Manager_assigned=row[6],
                id=row[0]
            )
        return None
     
    @classmethod
    def get_all(cls):
        sql = "SELECT FROM Artist"
        cursor.execute(sql)
        rows = cursor.fetchall()
        artists = []
        for row in rows:
            artist = cls(
                id = row[0],
                Artist_Name = row[1],
                Gender = row[2],
                Email = row[3],
                Genre_of_Music = row[4],
                No_of_songs_Assigned = row[5],
                Manager_Assigned = row[6]
            )
            artists.append(artist)
        return artists
        


    
    def __repr__(self):
        return f"<Artist('{self.Artist_Name}', '{self.Gender}, '{self.Email}')>"
         