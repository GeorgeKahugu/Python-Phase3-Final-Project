from test import cursor, conn

class Artist:

    def __init__(self, artist_name, gender, email, genre_of_music, no_of_songs_assigned, manager_assigned,id=None):
        self.id = id
        self.artist_name = artist_name
        self.gender = gender
        self.email = email
        self.genre_of_music = genre_of_music
        self.no_of_songs_assigned = no_of_songs_assigned
        self.Manager_Assigned = manager_assigned

    
    @property
    def artist_name(self):
        return self._artist_name

    @artist_name.setter
    def artist_name(self, value):
        if not isinstance(value,str):
            raise TypeError("Artist Name must be a string")
        self._artist_name = value

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self,value):
        if value not in ["Male", "Female", "Other"]:
            raise ValueError("Gender must be Male, Female or Other")
        self._gender = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self._email = value
    
    @property
    def genre_of_music(self):
        return self._genre_of_music
    
    @genre_of_music.setter
    def genre_of_music(self, value):
        if not isinstance(value, str):
            raise TypeError("Genre of Music must be a string")
        self._genre_of_music = value

    @property
    def no_of_songs_assigned(self):
        return self._No_of_songs_assigned
    @no_of_songs_assigned.setter
    def no_of_songs_assigned(self, value):
        if not isinstance(value, int):
            raise TypeError("No of songs assigned must be an integer")
        self._no_of_songs_assigned = value

    @property
    def manager_assigned(self):
        return self._manager_assigned
    
    @manager_assigned.setter
    def manager_assigned(self, value):
        if not isinstance(value, str):
            raise TypeError("Manager Assigned must be a string")
        self._manager_assigned = value
    
     
    #implementation of the classmethods 
    @classmethod
    def create_table(cls):
        '''This method will create an Artist table in our db'''
        sql = """
            CREATE TABLE Artist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_Name TEXT NOT NULL,
            gender TEXT,
            email TEXT,
            genre_of_Music TEXT,
            no_of_songs_assigned INTEGER,
            manager_assigned TEXT     
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
            artist_Name ,
            gender,
            email,
            genre_of_music ,
            no_of_songs_assigned,
            manager_assigned     
            )VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(sql, (self.artist_name, self.gender,  self.email, self.genre_of_music, self.no_of_songs_assigned, self.manager_assigned))
        conn.commit()
       
        self.id = cursor.lastrowid    
        print(f"artist{self.artist_name} created with ID {self.id}")
       
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
        sql = "SELECT * FROM Artist"
        cursor.execute(sql)
        rows = cursor.fetchall()
        artists = []
        for row in rows:
            artist = cls(
                id = row[0],
                artist_Name = row[1],
                gender = row[2],
                email = row[3],
                genre_of_music = row[4],
                No_of_songs_Assigned = row[5],
                Manager_Assigned = row[6]
            )
            artists.append(artist)
        return artists
        


    
    def __repr__(self):
        return f"<artist('{self.artist_name}', '{self.gender}, '{self.email}')>"
         