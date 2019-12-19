# Artist's Word Count Statistics

A program to calculate some statistics about the artist's number of words across all of their songs.

## Prerequisites

This project makes use of the Genius API, and so an account must be created with them to gain a client access token. This can be done by following [this link](https://genius.com/signup_or_login).

Once collected, the client access key can be used by entering it into the following lines of code on lines 7 and 8:

```
# ENTER CLIENT ACCESS TOKEN HERE
genius = lyricsgenius.Genius("YOURCLIENTACCESSTOKEN")
```

Python must be installed on your local machine (This program was developed in Python 3.8), as well as five libraries using the following commands on the command line (I believe the json library is included by default but I included it here just in case):

```
pip install lyricsgenius
pip install json
pip install matplotlib
pip install seaborn
pip install numpy
```

## Running the Project

Once the prerequisites have been satisfied, the project can be ran from the command line by redirecting to the Artist_Word_Count directory and running the following command:

```
python Artist_Word_Count.py
```

Upon running the program, there will be a prompt for you to enter an artist. Input the desired artist, and press the return key.

The program will then contact the API to collect the lyrics for every song developed by that artist, which may take a while.

Upon completion, some statistics about number of words per song such as the mean and standard deviation will be printed to the console, and a histogram and boxplot displaying the distribution of the words per song will be saved to the directory.

## Side notes

The program takes into consideration remixes and live recordings, and excludes these from the final dataset if they are found. This could also be expanded for acoustic performances, demos etc.

If an artist is entered that Genius does not recognise, the program will halt. I was going to implement a method to catch this error and prompt for another artist but I unfortunately did not have the time.