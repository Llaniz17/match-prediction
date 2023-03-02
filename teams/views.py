from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Team, Player
import numpy

# Canada  centros PB colocao Cr asistir Sen Gol USa centros Mechico colacao Jap asist Y



def index(request):
    latest_team_list = Team.objects.order_by('id')
    context = {'latest_team_list': latest_team_list}
    return render(request, 'teams/index.html', context)


def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    over = 0
    for player in team.player_set.all():
        over = over + player.ovr
    over = round(over / len(team.player_set.all()))
    team.ovr = over
    team.save()

    return render(request, 'teams/detail.html', {'team': team})


def match(request):
    latest_team_list = Team.objects.order_by('id')
    context = {'latest_team_list': latest_team_list}
    return render(request, 'teams/match.html', context)

def playMatch(request):
    t1 = request.POST['team1']
    t2 = request.POST['team2']
    team1 = Team.objects.get(name=t1)
    team2 = Team.objects.get(name=t2)
    if(team1.ovr>team2.ovr):
        p1 = 33.33 + abs(team1.ovr-team2.ovr)
        p2 = 33.33 - abs(team1.ovr-team2.ovr)/2
        empate = 100 - p1 - p2
    elif(team2.ovr>team1.ovr):
        p2 = 33.33 + abs(team1.ovr-team2.ovr)
        p1 = 33.33 - abs(team1.ovr-team2.ovr)/2
        empate = 100 - p1 - p2
    else:
        p1 = 33.33
        p2 = 33.33
        empate = 100 - p1 - p2
    
    prob = numpy.random.choice([team1.name,"Draw",team2.name],size=1, p=[(p1/100),(empate/100),(p2/100)] )

    for p in prob:
        if(p==team1.name):
            result = numpy.random.choice([team1.name+" :1 - "+team2.name+" :0",
            team1.name+" :2 - "+team2.name+" :0",
            team1.name+" :2 - "+team2.name+" :1",
            team1.name+" :3 - "+team2.name+" :0",
            team1.name+" :3 - "+team2.name+" :1"],size=1,p=[0.2,0.2,0.2,0.2,0.2])
        elif(p==team2.name):
            result = numpy.random.choice([team2.name+" :1 - "+team1.name+" :0",
            team2.name+" :2 - "+team1.name+" :0",
            team2.name+" :2 - "+team1.name+" :1",
            team2.name+" :3 - "+team1.name+" :0",
            team2.name+" :3 - "+team1.name+" :1"],size=1,p=[0.2,0.2,0.2,0.2,0.2])
        elif(p=="Draw"):
            result = numpy.random.choice([team1.name+" :0 - "+team2.name+" :0",
            team1.name+" :1 - "+team2.name+" :1",
            team1.name+" :2 - "+team2.name+" :2",
            team1.name+" :3 - "+team2.name+" :3",],size=1,p=[0.25,0.25,0.25,0.25])


    context = {
        'p1':round(p1),
        'empate':round(empate),
        'p2':round(p2),
        'result':result
        }

    return render(request,'teams/playMatch.html',{
        'team1':team1,
        'team2':team2,
        'context':context
    })


def detail_player(request, team_id, player_id):
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id, team=team_id)
    return render(request, 'teams/detail_player.html', {'player': player})


#Sim match functions

