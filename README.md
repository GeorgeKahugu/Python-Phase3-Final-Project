# Music Management CLI Application

## DATE 11 JUNE 2024

### BY : George Kahugu

### Description of the project -

The Music Management CLI Application allows users to manage managers,artists ans songs with a music management system. Users can create managers with details such as name,gender,contact information,genre specialization and the number of artists managed. Artists can be created with details including name,gender,email,music genre,number of songs assigned and manager assigned. Additionally, users can create songs by specifying the song title and genre

## Features

### Create a Manager

    -Users can create a manager with details such as first name, last name, gender, email, phone number, genre specialization and number of artists managed.
     - Stores manager details in memory and provides a unique ID for each manager.

### Create Artist

    - Gathers details like artist name, gender,email,music genre, number of songs assigned and manager assignment.
    - Stores artist information and assigns them to a specified manager.

### Create Song

    - Enables users to add songs by entering the song title and genre.
    - Stores song details and provides each song with a unique ID.

### Get Assigned Manager

    - Retrieves and displays the manager assigned to a specific artist based on artist ID.
    - Provide details about the artist and their assigned manager.

## How to Use

### Installation

    - Clone the repository to your local machine.

### Setup

    - Ensure Python 3.8.13 or highher is installed in your machine.
    - Install the required packages by running `pipenv install'.
    -Enter the virtual environment by running 'pipenv shell'.

### Execution

    - Run the application by executing `python lib/cli.py` file in your terminal.
    - Follow the on-screen instructions to interact with the CLI application.
    -Choose options to create managers,artists,songs or retrieve manager details for an artist.

NB : Make sure to input correct details as prompted to ensure proper functionality. ID numbers are generated automatically and are used to uniquely identify each manager,artist and song.

## Contributors

- [George Kahugu](https://github.com/GeorgeKahugu)

## License

        MIT License

        Copyright (c) 2024 GeorgeKahugu

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
