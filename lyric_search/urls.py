from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('lyrics/', views.Lyrics.as_view(), name='lyrics'),
    path('lyrics/<int:id>/', views.Lyrics.as_view(), name='lyrics'),
    #path('add_song/', views.AddSongView.as_view(), name='add_song'),
]