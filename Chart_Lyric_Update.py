import lyricsgenius


genius = lyricsgenius.Genius('bFSy9jEEXEe758Kf82Tpe-pUPb5A9Gs8r4F_YKn6BehF4u6sphLMEaUprO4bOt__')
song = genius.search_song('Truth Hurts', 'Lizzo')
test = song.lyrics

print(test)