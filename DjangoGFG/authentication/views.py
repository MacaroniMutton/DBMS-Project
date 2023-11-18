import random
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Player, PlayerProfile
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        if "register" in request.POST:
            name = request.POST['username']
            plemail = request.POST['email']
            plpassword = request.POST['password']

            try:
                myuser = Player(username=name, email=plemail, password=plpassword)
                myuser.save()

                playerprofile = PlayerProfile(username=myuser)
                playerprofile.save()

                messages.success(request, "Your Account has been successfully created! You may login now")
            except IntegrityError as e:
                # Handle the case where a duplicate entry is detected
                messages.error(request, "A user with the same username or email already exists.")
        elif "login" in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Player.objects.get(email=email, password=password)
            except Player.DoesNotExist:
                user = None
            if user is not None:
                request.session['user_id'] = user.id
                messages.success(request, "You have successfully logged in!")
                return redirect('suclog')
            else:
                messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')

def get_player_from_session(request):
    user_id = request.session.get('user_id')
    if user_id:
        return get_object_or_404(Player, id=user_id)
    return None


def suclog(request):
    return render(request, 'successlogin.html')

# def gamepage(request):
    
#     if request.method == "POST":
#         if "delete" in request.POST:
#             name=request.POST['username']
#         try:
#             user = Player.objects.get(username=name)
#         except Player.DoesNotExist:
#             user = None
#         if user is not None:
#             user.delete()
#         else:
#             messages.error(request, "Invalid login credentials")
#     return render(request, 'game.html')


def gamepage(request):
    return render(request, 'game.html')

def deleteProfile(request):
    player = get_player_from_session(request)

    if request.method == "POST" and player:
        if "delete" in request.POST:
            try:
                # Delete the PlayerProfile associated with the user
                playerprofile = PlayerProfile.objects.get(username=player)
                playerprofile.delete()

                # Delete the Player
                player.delete()

                # Clear the user_id from the session
                del request.session['user_id']

                messages.success(request, "Your profile has been deleted.")
                return redirect('home')
            except PlayerProfile.DoesNotExist:
                messages.error(request, "Player profile not found.")
        # Add other conditions or actions as needed

    # Rest of the function
    return render(request, 'deleteprof.html')  


def playerProfile(request):
    player = get_player_from_session(request)

    if player:
        try:
            # Assuming 'PlayerProfile' has a OneToOne relationship with 'Player'
            playerprofile = PlayerProfile.objects.get(username=player)
            context = {'player_profile': playerprofile}
        except PlayerProfile.DoesNotExist:
            context = {'player_profile': None}
    else:
        context = {'player_profile': None}

    return render(request, 'plprof.html', context)

def playresults(request):
    player = get_player_from_session(request)

    if player:
        # Simulate match results
        match_won = random.choice([True, False])
        if match_won:
            rounds_won = 13
            rounds_lost = random.randint(1, 11)
        else:
            rounds_won = random.randint(1, 11)
            rounds_lost = 13
        avg_combat_score = random.randint(1, 1000)
        first_blood = random.randint(1, 3)
        plants = random.randint(1, 3)
        defuses = random.randint(1, 3)

        # Update player profile based on match results
        player_profile = PlayerProfile.objects.get(username=player)
        player_profile.games_played += 1

        if match_won:
            player_profile.matches_won += 1
            player_profile.matches_won_curr_lvl += 1
            player_profile.level_up()  # Implement level_up method in PlayerProfile model

            # Update rank based on level
            if player_profile.level >= 1 and player_profile.level <= 5:
                player_profile.rank = 'Iron'
            elif player_profile.level >= 6 and player_profile.level <= 12:
                player_profile.rank = 'Bronze'
            elif player_profile.level >= 13 and player_profile.level <= 20:
                player_profile.rank = 'Silver'
            elif player_profile.level >= 21 and player_profile.level <= 30:
                player_profile.rank = 'Gold'
            elif player_profile.level >= 31 and player_profile.level <= 42:
                player_profile.rank = 'Platinum'
            elif player_profile.level >= 43 and player_profile.level <= 60:
                player_profile.rank = 'Diamond'
            elif player_profile.level >= 61 and player_profile.level <= 79:
                player_profile.rank = 'Ascendant'
            elif player_profile.level >= 80 and player_profile.level <= 100:
                player_profile.rank = 'Immortal'
            else:
                player_profile.rank = 'Radiant'

        else:
            player_profile.matches_lost += 1

        player_profile.save()

        # Pass match results as context to the template
        context = {
            'match_won': match_won,
            'rounds_won': rounds_won,
            'rounds_lost': rounds_lost,
            'avg_combat_score': avg_combat_score,
            'first_blood': first_blood,
            'plants': plants,
            'defuses': defuses,
        }

        return render(request, 'plres.html', context)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
