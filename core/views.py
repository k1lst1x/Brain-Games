from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'index.html')

@login_required
def game_2048(request):
    return render(request, '2048.html')

@login_required
def marsmoney(request):
    return render(request, 'marsmoney.html')

@login_required
def mastercards(request):
    return render(request, 'mastercards.html')

@login_required
def masterpieces(request):
    return render(request, 'masterpieces.html')

@login_required
def genius_memory(request):
    return render(request, 'genius_memory.html')

@login_required
@require_POST
def add_score(request):
    user = request.user
    user.score += 10  # Например, 10 очков за правильный ответ
    user.save()
    return JsonResponse({'status': 'success', 'new_score': user.score})