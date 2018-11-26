# Describe the relationship between string.join(string.split(song)) and song.
# Are they same for all strings?
# When would they be different? (Song is a string)
import string
song='Good Time'

print(song.split())
song[0].join(song[1])
print(song)

# METHOD II
newSong=''
for i in song:
    newSong+=i
print(newSong)