from test import cursor, conn

class Song:

    def __init__(self, Song_title, Genre, id=None):
        self.id = id
        self.Song_title = Song_title
        self.Genre = Genre

#Calling the property Methods
    @property
    def Song_title(self):
        return self._Song_title
    
    @Song_title.setter
    def Song_title(self, value):
        if not value:
            raise ValueError("Song title cannot be empty")
        self._Song_title= value
    
    @property
    def Genre(self):
        return self._Genre
    
    @Genre.setter
    def Genre(self, value):
        if not value:
            raise ValueError("Genre cannot be empty")
        self._Genre=value

#Calling the class methods using CRUD operations specifically(create,delete,get all and find by id) as per the brief  
# 
# Creating The Table    
    @classmethod
    def create_table(cls):
        '''This method will create a Song table in our db'''
        sql = """
            CREATE TABLE IF NOT EXISTS Song (
            id INTEGER PRIMARY KEY,
            Song_title TEXT NOT NULL,
            Genre TEXT NOT NULL
            )
        """

        cursor.execute(sql)
        conn.commit()

#Dropping the Table
    @classmethod
    def drop_table(cls):
        sql = """
           DROP TABLE IF EXISTS Song
        """ 
        cursor.execute(sql)
        conn.commit()


#Saving the Table    
    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO Song (Song_title, Genre)
                VALUES (?, ?)
            """
            cursor.execute(sql, (self.Song_title, self.Genre))
            self.id = cursor.lastrowid
        else:
            sql = """
                UPDATE Song
                SET Song_title = ?, Genre = ?
                WHERE id = ?
            """
            cursor.execute(sql, (self.Song_title, self.Genre, self.id))
        conn.commit()

#Deleting the Table
    def delete(self):
        if self.id is None:
            raise ValueError("Song does not exist")
        sql = "DELETE FROM Song WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        self.id = None
   

    @classmethod
    def create (cls,Song_title, Genre):
        song = cls(id, Song_title, Genre)
        song.save()
        return song
    
    @classmethod
    def get_all(cls):
        sql= "SELECT * FROM Song"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(id=row[0], Song_title= row[1], Genre=row[2]) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        sql = "SELECT * FROM Song WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if row:
            return cls(
                id=row[0], 
                Song_title=row[1],
                Genre=row[2])
        return None
    
    def __repr__(self):
        return f"<Song('{self.Song_title}', '{self.Genre}'>"
         