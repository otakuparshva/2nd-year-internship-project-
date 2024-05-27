from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def game(request):
    return render(request, 'game/game.html')