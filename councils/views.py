from django.shortcuts import render, get_object_or_404
from .models import Councils,Clubs,Achievements,Clubevents,Clubgallery
from django.template import loader


# Create your views here.
def index(request, council_id):
    council = get_object_or_404(Councils, pk=council_id)
    achievements=Achievements.objects.filter(council=council)
    club_list=council.clubs_set.all()
    context = {
        'council': council,
        'club_list':club_list,
        'achievements':achievements,
        'council_id':council_id,
    }
    return render(request,'councils/council.html',context)

def clubpage(request,council_id,club_id):
    council=get_object_or_404(Councils,pk=council_id)
    club=get_object_or_404(Clubs,council=council,pk=club_id)
    clubevents=Clubevents.objects.filter(club=club)
    clubgallery=Clubgallery.objects.filter(club=club)
    context={
        'council': council,
        'club':club,

    }
    return render(request,'councils/index.html',context)

def gallery(request,council_id,club_id):
    council=get_object_or_404(Councils,pk=council_id)
    club=get_object_or_404(Clubs,council=council,pk=club_id)
    clubgallery=Clubgallery.objects.filter(club=club)
    context={
        'club':club,
        'council': council,
        'clubgallery':clubgallery,
    }
    return render(request,'councils/gallery.html',context)


def events(request,council_id,club_id):
    council=get_object_or_404(Councils,pk=council_id)
    club=get_object_or_404(Clubs,council=council,pk=club_id)
    clubevents=Clubevents.objects.filter(club=club)
    context={
        'club':club,
        'council': council,
        'clubevents':clubevents,
    }
    return render(request,'councils/events.html',context)

def contacts(request,council_id,club_id):
    council=get_object_or_404(Councils,pk=council_id)
    club=get_object_or_404(Clubs,council=council,pk=club_id)
    clubevents=Clubevents.objects.filter(club=club)
    context={
        'club':club,
        'council': council,

    }
    return render(request,'councils/contact.html',context)
