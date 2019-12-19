# import libraries
import lyricsgenius
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ENTER CLIENT ACCESS TOKEN HERE
genius = lyricsgenius.Genius("YOURCLIENTACCESSTOKEN")

# artist input, surrounded with try catch in case the artist is not found
artist = input('Please enter the name of an artist: ')

# exclude remixes and live performances, can be added to e.g. acoustic performances would require the extra parameter: "(Acoustic)"
genius.excluded_terms = ["(Remix)", "(Live)"]

# remove headers such as [Verse 1] so that the word count is not impacted
genius.remove_section_headers = True

# edit search, use the max_songs=x argument to create an upper limit and shorten search times
search = genius.search_artist(artist, sort="title")

# print search
print(search.songs)

# save artist's lyrics into a JSON file
search.save_lyrics()

# remove spaces from inputted artist string to locate json file
artistString = artist.replace(" ", "")

#print("Lyrics_" + str(artistString) + ".json")

# read JSON file back into python
with open('Lyrics_' + str(artistString) + '.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# extract songs data from JSON file
songExtract = obj['songs']

# loop through songs and extract lyrics
songLyrics = [i['lyrics'] for i in songExtract]

# replace occurences of \n with a whitespace
songLyrics = [i.replace("\n", " ") for i in songLyrics]

# replace instrumental song strings with an empty string so that the word count is 0
songLyrics = [i.replace("[Instrumental]", "") for i in songLyrics]

# count number of words per song and compile into list
wordCountList = [len(i.split()) for i in songLyrics]

# print lyrics
#print(songLyrics)

# print list with word count of each song
#print(wordCountList)

# print the outcome for the user
print("Average (mean) number of words in a " + artist + " song is: " + str((sum(wordCountList)/len(wordCountList))))

# print minimum length
print("Minimum number of words in a " + artist + " song is: " + str(min(wordCountList)))

# print maximum length
print("Maximum number of words in a " + artist + " song is: " + str(max(wordCountList)))

# print variance
print("Variance of words in " + artist + " songs is: " + str(np.var(wordCountList)))

# print standard deviation
print("Standard deviation of words in " + artist + " songs is: " + str(np.std(wordCountList)))

# plot all word counts into a histogram to see distribution of number of words
sns.set_style("white")
plt.figure(figsize=(10,5), dpi= 300)
sns.distplot(wordCountList, color="green", hist_kws=dict(edgecolor="k", linewidth=1), bins=10)
plt.xlabel('Number of Words')
plt.ylabel('Probability Density')
plt.title('Histogram to Show the Distribution of Number of Words in ' + artist + ' Songs')
plt.savefig(artist + ' Histogram.png')
print('Saved ' + artist + ' Histogram.png in the directory')

# plot all word counts into a boxplot to see distribution of number of words
sns.set_style("white")
plt.figure(figsize=(10,5), dpi= 300)
sns.boxplot(x=wordCountList, color="green")
plt.xlabel('Number of Words')
plt.title('Boxplot to Show the Distribution of Number of Words in ' + artist + ' Songs')
plt.savefig(artist + ' Boxplot.png')
print('Saved ' + artist + ' Boxplot.png in the directory')