import mysql.connector
import billboard
import lyricsgenius





def delete_and_add():
    clear_database = ("DELETE FROM lyric_search_song")
    cursor.execute(clear_database)
    cnx.commit()

    for i in range(100):
        sql = "INSERT INTO lyric_search_song VALUES (%s, %s, %s, %s, %s)"
        val = (i + 1, i + 1, chart[i].title, chart[i].artist, "hi")


def update():
    for i in range(100):
        song = genius.search_song(chart[i].title, chart[i].artist)
        sql = ("UPDATE lyric_search_song SET title = %s, artist = %s, lyrics = %sWHERE id = %s")
        val = (chart[i].title, chart[i].artist, song.lyrics, i + 1)

        cursor.execute(sql, val)
        cnx.commit()

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LyricChart"
)

cursor = cnx.cursor()

chart = billboard.ChartData('hot-100')
genius = lyricsgenius.Genius('vN3XWRhSbaH74LFf2HpCDfdQou-1YSfIdAAHp_sL8q6xQOLTEpi4TXDI5LWdWM0i')


#delete_and_add()
update()

cursor.close()
cnx.close()