from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def game_2048(request):
    return render(request, '2048.html')

def marsmoney(request):
    return render(request, 'marsmoney.html')