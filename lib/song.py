from test import cursor, conn

class Song:

    def __init__(self, id, Song_title, Genre):
        self.id = id
        self.Song_title = Song_title
        self.Genre = Genre
        
    @classmethod
    def create_table(cls):
        '''This method will create a Song table in our db'''
        sql = """
            CREATE TABLE Song (
            id INTEGER PRIMARY KEY,
            Song_title TEXT NOT NULL,
            Genre TEXT NOT NULL
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
           DROP TABLE IF EXISTS Song
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            CREATE TABLE Song (
            id INTEGER PRIMARY KEY,
            Song_title TEXT NOT NULL,
            Genre TEXT NOT NULL
            )
        """

        cursor.execute (sql, (self.Song_title, self.Genre))
        conn.commit()
       
        
       
    
    def __repr__(self):
        return f"<Artist('{self.Song_title}', '{self.Genre}'>"
         