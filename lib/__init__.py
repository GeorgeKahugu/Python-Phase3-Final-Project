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
    retrieved_manager.delete()

# Verify deletion
    deleted_manager = Manager.find_by_id(Manager.id)
    print(deleted_manager)  

#Adding Managers to the Database
manager1 = Manager(
    "Clive", "Brown", "Male", "clivebrown@iworld.com",  "+1972345672", "Lion", 2)


manager2 = Manager(
    "Nadia", "Ross", "Female", "nadiaross@iworld.com", "+1975467231", "Panther", 2)

artist1 = Artist (
    "Rocky", "Male", "rocky1@artistworld.com", "Soul", 2, "Clive")

manager1.save()
manager2.save()

artist1.save()

print(manager1)
print(artist1)