import json
# file names we will use
input_file_name = 'songs.json'
output_file_name = 'playlist.csv'
# open our input file for reading
input_file = open(input_file_name, 'r')

# load the file contents into a dictionary
# using the load function from the json module
song_collection = json.load(input_file)

# print the contents so that we can see
# what it looks like
print('\nThe song dictionary:')
print(song_collection)

# get the list and print
song_list = song_collection.get('songlist')
print('\nThe song list:')
print(song_list)

# the overall goal here is to create a playlist for the user
# to do this, ultimately we will create a list of lists
# the outer list will be the playlist
# therefore, go ahead and create that outer list now
# this will create a empty list that we will add to later
print('\nNow creating a playlist...')
playlist = list()

# outer loop to ask user for each song
while True:
    # display a menu of songs for user to choose from
    # first setup a counter for menu options
    count = 1
        # display menu options - the songs to pick from
        # we have to display each song, hence a loop
        # we are reading from the song_list variable,
    # which is a list of dictionaries from the json file
    print('\nHere are your song options:')
    # put each song read into a dictionary variable
    # that we will call single_song_dictionary
    for single_song_dictionary in song_list:
    # display option by getting the song and title
    # out of the dictionary. uses the get method
    # that we can call on a dictionary.
        print(str(count) + '.',
            single_song_dictionary.get('title'),
            'by', single_song_dictionary.get('artist'))
        count += 1
    # ask user to choose a song, ank them for the number
    print('\nChoose a song to add to your playlist!')
    song_num = int(input('Enter the song number: '))
    # now we need to create that inner list that we
    # will add to playlist.
    # the inner list will represent a single song
    # the first element of the inner list will be the title
    # the second element will be the artist
    # first, create an empty list
    inner_list = list()
      # next, append the first element, which is the title
      # get title from song_list, indexed by num from user
    inner_list.append(song_list[song_num-1].get('title'))
    # next, append the second element, which is the artist
    # get the title from the song list, indexed by num from user
    inner_list.append(song_list[song_num-1].get('artist'))
    # print back to the user what they have chosen
    # note we are reading the song & artist from the inner list
    print('You have chosen', inner_list[0], 'by', inner_list[1])
    # append the inner_list to the outer play list
    playlist.append(inner_list)
    # ask the user if they want to add another song?
    # if no, then quit the loop
    chose_again = input('Do you want to choose another song? Y or N: ')
    if chose_again.upper() == 'N':
        break


# finally, we have a play list created,
# which is a list of lists
# print it out for the user using a loop
print('\nExcellent! Your play list is:')
for s in playlist:
    print(s[0], '-', s[1])
# now print the playlist to a CSV file
# first, we must open the file for writing
# if the file does not exist, it will create it
# if the file already exists, it will overwrite it
output_file = open(output_file_name, 'w')

# first, write the first row, which is the headers
output_file.write('NUMBER,SONG,ARTIST\n')
# next, write each row
# each row will be each song
# setup a counter variable to keep a count
count = 1
# to write each row we need to loop through
# the play list and get each inner list
for inner_list_song in playlist:
    output_file.write(str(count) + ','
        + inner_list_song[0] + ','
        + inner_list_song[1] + '\n')
    count += 1
print('\nNow find your playlist file and open it in Excel!')
