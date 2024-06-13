
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
      email = input ("Email: ")
      phone_number = input ("Phone Number: ")
      genre=input("Genre: ")
      no_of_artists_assigned=int(input("Number of Artists Assigned: "))

      manager=Manager(first_name, last_name, gender, email, phone_number, genre, no_of_artists_assigned)
      manager.save()
      managers.append(manager)
      manager_dict[manager.id] = manager
      print(f"Manager {manager.first_name} {manager.last_name}")

#creating artist class in cli
def create_artist():
    artist_name = input("Artist Name: ")
    gender = input("Gender: ")
    email = input("email: ")
    genre_of_music = input("Genre of Music: ")
    no_of_songs_assigned = int(input("Number of Songs Assigned: "))
    manager_assigned = input("Manager Assigned(first_name last_name): ")

    artist = Artist(artist_name=artist_name, gender=gender, email=email, genre_of_music=genre_of_music, no_of_songs_assigned=no_of_songs_assigned, manager_assigned=manager_assigned)
    artist.save()
    artists.append(artist)
    artist_dict[artist.id] = artist
    print(f"Artist {artist.artist_name} created with ID {artist.id}")

#creating a song in the CLI
def create_song():
    song_title = input("Song Title: ")
    genre = input("Genre: ")
    song= Song(song_title, genre)
    song.save()
    songs.append(song)
    song_dict[song.id] = song
    print(f"Song {song.song_title} created with ID {song.id}")

#get the assigned manager in the CLI
def get_assigned_manager():
    artist_id = int(input("Enter Artist ID: "))
    artist = artist_dict.get(artist_id)
    if artist:
         manager = manager_dict.get(artist.manager_assigned)
         if manager:
            print(f"Artist: {artist.artist_name}, Song Genre: {artist.genre_of_music}, Manager:{manager.first_name} {manager.last_name}")
         else:
            print(f"Manager with ID {artist.manager_assigned} was found")
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

