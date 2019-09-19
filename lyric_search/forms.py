from django import forms


class SongForm(forms.Form):
    rank = forms.IntegerField()
    title = forms.CharField(max_length=75)
    artist = forms.CharField(max_length=75)
    lyrics = forms.CharField(max_length=10000)