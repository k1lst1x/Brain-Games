from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from users.models import CustomUser

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
def number_hunt(request):
    return render(request, 'number_hunt.html')

@login_required
def color_pairs(request):
    return render(request, 'color_pairs.html')

@login_required
def chess(request):
    return render(request, 'chess.html')

@login_required
def match_the_feel(request):
    return render(request, 'match_the_feel.html')

@login_required
def still_awake(request):
    return render(request, 'still_awake.html')

@login_required
@require_POST
def add_score(request):
    user = request.user
    user.score += 10  # Например, 10 очков за правильный ответ
    user.save()
    return JsonResponse({'status': 'success', 'new_score': user.score})

def leaderboard_view(request):
    users = CustomUser.objects.filter(is_active=True).order_by('-score')[:50]  # топ-50
    return render(request, 'leaderboard.html', {'users': users})
