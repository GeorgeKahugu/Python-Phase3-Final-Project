#Imports
from song import Song
from artist import Artist
from manager import Manager
from test import conn, cursor

#Dropping and create the tables
Manager.drop_table()
Manager.create_table()

Artist.drop_table()
Artist.create_table()

Song.drop_table()
Song.create_table()

# Retrieve a manager by id
manager_id = 1
retrieved_manager = Manager.find_by_id(manager_id)
print(retrieved_manager)

#checking if a manager exists
if retrieved_manager is not None:
    print(retrieved_manager)

# Update a manager's first name
    retrieved_manager.first_name = "Clive"
    print(f"Updated manager's first name to:{retrieved_manager.first_name}")

# Delete the manager
    # retrieved_manager.delete()

# Verify deletion
    # deleted_manager = Manager.find_by_id(Manager.id)
    # print(deleted_manager)  

# Retrieve an artist by id
artist_id = 1
retrieved_artist = Artist.find_by_id(artist_id)
print(retrieved_artist)

#checking if an artist exists
if retrieved_artist is not None:
    print(retrieved_artist)

# Update an Artist name
    retrieved_artist.artist_name = ""
    print(f"Updated artists's name to:{retrieved_artist.artist_name}")

# Delete the artist
    retrieved_artist.delete()

# Verify deletion
    deleted_artist = Artist.find_by_id(Artist.id)
    print(deleted_artist)  
    
#Adding and Saving a Song to the Database
song1 = Song("Greatful", "RnB")
song1.save()

song2 = Song("Miracle", "Gospel")
song2.save()

song3=Song("Getit", "Rap")
song3.save()

# Find song by ID
retrieved_song = Song.find_by_id(song1.id)
print(retrieved_song)

# Get all songs
all_songs = Song.get_all()
print(all_songs)

# Delete a song by ID
# song1.delete()


#Adding Managers to the Database
manager1 = Manager("Clive", "Brown", "Male", "clivebrown@iworld.com",  "+1972345672", "HipHop", 2)

manager2 = Manager("Nadia", "Ross", "Female", "nadiaross@iworld.com", "+1975467231", "RnB", 2)

manager3 = Manager("James", "Roberts", "Male", "jamesroberts@iworld.com", "+2547865432", "Rap", 2)

manager4 = Manager("Samantha", "Williams", "Female", "samanthawilliams@iworld.com", "+1873785218", "Gospel", 2)


#Adding Artists to the Database
artist1 = Artist("Breezy", "Male", "breezy@artistworld.com", "RnB", 2, "Nadia Ross",1)
artist2 = Artist (  "Ivy", "Female", "Ivy@artistworld.com", "Rnb", 2, "Nadia Ross",2)





#Manager
manager1.save()
manager2.save()
manager3.save()
manager4.save()

#Artist
artist1.save()
artist2.save()


