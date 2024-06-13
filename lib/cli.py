# lib/cli.py
from manager import Manager
from artist import Artist
from song import Song

#Initializing lists and dictionaries
managers = []
artists = []
songs =[]
manager_dict = {}
artist_dict = {}
song_dict = {}


def create_manager():
      first_name = input("First Name: ")
      last_name = input("Last Name: ")
      gender = input ("Gender: ")
      Email = input ("Email: ")
      phone_number = input ("Phone Number: ")
      Team=input("Team: ")
      No_of_Artists_Assigned=int(input("Number of Artists Assigned: "))

      manager=Manager(first_name, last_name, gender, Email, phone_number, Team, No_of_Artists_Assigned)
      manager.save()
      managers.append(manager)
      manager_dict[manager.id] = manager
      print(f"Manager {manager.first_name} {manager.last_name} created with ID {song.id}")

def get_assigned_manager():
 
        print("Various Artists assigned to a manager with their various Songs and Genre :")
        Artist_name = input ("Artist Name :")
        Gender = input ("Gender :")
        Email = input ("Email :")
        Genre_of_Music= input ("Genre of Music :")
        No_of_Songs_Assigned= input ("No of Songs Assigned :")
        get_assigned_manager = input ("Manager Assigned :")
        Exit_app = input ("Exit app :")
           
        

if __name__ == "__main__":
    get_assigned_manager()

