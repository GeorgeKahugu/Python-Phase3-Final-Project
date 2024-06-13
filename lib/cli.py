
# from lib import song
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

#create manager class in cli
def create_manager():
      first_name = input("First Name: ")
      last_name = input("Last Name: ")
      gender = input ("Gender: ")
      Email = input ("Email: ")
      phone_number = input ("Phone Number: ")
      Genre=input("Genre: ")
      No_of_Artists_Assigned=int(input("Number of Artists Assigned: "))

      manager=Manager(first_name, last_name, gender, Email, phone_number, Genre, No_of_Artists_Assigned)
      manager.save()
      managers.append(manager)
      manager_dict[manager.id] = manager
      print(f"Manager {manager.first_name} {manager.last_name}")

#creating artist class in cli
def create_artist():
    Artist_name = input("Artist Name: ")
    Gender = input("Gender: ")
    Email = input("Email: ")
    Genre_of_Music = input("Genre of Music: ")
    No_of_songs_assigned = int(input("Number of Songs Assigned: "))
    Manager_assigned = input("Manager Assigned(first_name last_name): ")

    artist = Artist(Artist_name=Artist_name, Gender=Gender, Email=Email, Genre_of_Music=Genre_of_Music, No_of_songs_assigned=No_of_songs_assigned, Manager_assigned=Manager_assigned)
    artist.save()
    artists.append(artist)
    artist_dict[artist.id] = artist
    print(f"Artist {artist.Artist_Name} created with ID {artist.id}")

#creating a song in the CLI
def create_song():
    Song_title = input("Song Title: ")
    Genre = input("Genre: ")

    song= Song(Song_title, Genre)
    song.save()
    songs.append(song)
    song_dict[song.id] = song
    print(f"Song {song.Song_title} created with ID {song.id}")

#get the assigned manager in the CLI
def get_assigned_manager():
    artist_id = int(input("Enter Artist ID: "))
    artist = artist_dict.get(artist_id)
    if artist:
         manager = manager_dict.get(int(artist.Manager_Assigned))
         if manager:
            print(f"Artist: {artist.Artist_Name}, Song Genre: {artist.Genre_of_Music}, Manager:{manager.first_name} {manager.last_name}")
         else:
            print(f"Manager with ID {artist.Manager_Assigned} not found")
    else:
        print(f"Artist with ID {artist_id} not found ")

#printing the classes created 
def main():
    while True:
        print("\n1. Create Manager")
        print("2. Create Artist")
        print("3. Create Song")
        print("4. Get Assigned Manager for an Artist")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_manager()
        elif choice == '2':
            create_artist()
        elif choice =='3':
            create_song()
        elif choice == '4':
            get_assigned_manager()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.") 

if __name__ == "__main__":
   main()

