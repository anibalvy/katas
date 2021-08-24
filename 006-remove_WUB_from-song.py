import re
def song_decoder(song):
    #return song.replace("WUBWUB","").replace("WUB"," ").strip()
    return re.sub("(WUB)+", " ", song).strip()

# return " ".join(song.replace('WUB', ' ').split())
# return ' '.join([a for a in song.split('WUB') if a])


test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")
