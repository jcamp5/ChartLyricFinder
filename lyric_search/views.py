from django.shortcuts import render
#from django.http import HttpResponse
from django.views import View
from .models import Song
from .forms import SongForm
# Create your views here.


class index(View):

    def get(self, request):
        songs = Song.objects.order_by('rank')
        context = {'songs' : songs}
        return render(request, 'lyric_search/index.html', context)

class About(View):

    def get(self, request):
        return render(request, 'lyric_search/about.html')

class Contact(View):

    def get(self, request):
        return render(request, 'lyric_search/contact.html')


class Lyrics(View):
    
    def get(self, request, id=1):
        song = Song.objects.get(pk=id)
        context = {'song' : song}
        return render(request, 'lyric_search/lyrics.html', context)

#class AddSongView(View):
#    form = SongForm
#    context = {'form' : form}
#    template_name = 'lyric_search/add_song.html'

#    def get(self, request):
#        form = self.form()
#        return render(request, self.template_name, self.context)

#    def post(self, request):
#        form = self.form(request.POST)

#        if form.is_valid():
#            new_song = Song(rank=request.POST['rank'], title=request.POST['title'], artist=request.POST['artist'])
#            new_song.save()
        
#        return render(request, self.template_name, self.context)