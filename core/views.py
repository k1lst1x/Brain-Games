from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
import json

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
    try:
        data = json.loads(request.body)
        points = int(data.get('points', 0))  # безопасное извлечение
        if points > 0:
            request.user.score += points
            request.user.save()
            return JsonResponse({'status': 'success', 'new_score': request.user.score})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid points'}, status=400)
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def leaderboard_view(request):
    users = CustomUser.objects.filter(is_active=True).order_by('-score')[:50]  # топ-50
    return render(request, 'leaderboard.html', {'users': users})

@login_required
def profile_view(request):
    all_users = CustomUser.objects.filter(is_active=True).order_by('-score')
    user = request.user
    rank = list(all_users).index(user) + 1  # +1 потому что index начинается с 0
    total = all_users.count()
    return render(request, 'profile.html', {
        'user': user,
        'rank': rank,
        'total': total,
    })