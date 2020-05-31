import re

def song_decoder(song):
    song = song.replace("WUB"," ")
    song = song.rstrip()
    song = song.lstrip()
    song = re.sub(" +"," ",song)
    return song
print song_decoder("WUBAWUBWUBBWUBCWUB")