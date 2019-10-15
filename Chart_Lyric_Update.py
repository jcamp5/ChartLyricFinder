import lyricsgenius


genius = lyricsgenius.Genius('vN3XWRhSbaH74LFf2HpCDfdQou-1YSfIdAAHp_sL8q6xQOLTEpi4TXDI5LWdWM0i')
song = genius.search_song('Truth Hurts', 'Lizzo')
test = song.lyrics

print(test)