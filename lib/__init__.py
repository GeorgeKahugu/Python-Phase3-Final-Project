from song import Song
from artist import Artist
from manager import Manager
from test import conn, cursor

Manager.drop_table()
Manager.create_table()

Artist.drop_table()
Artist.create_table()

Song.drop_table()
Song.create_table()

