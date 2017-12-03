from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from gymkhanawebsite import settings
from .models import Chat,Chatroom
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView


def Login(request):
    next = request.GET.get('next', '/home/')
    return HttpResponseRedirect(str('/home/login/?next='+next))


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/home/logout/")


def Home(request,label):
    room = get_object_or_404(Chatroom,label=label)
    c=Chat.objects.filter(room=room)
    if request.user.is_authenticated:
        return render(request, "chat_app/home.html", {'home': 'active', 'chat': c,'label':label})
    else:
        return render(request,"chat_app/home.html",{'home':'active','chat':c,'error_message':"Please LogIn",'label':label})

@login_required
def Post(request,label):
    room=get_object_or_404(Chatroom,label=label)
    if request.method == "POST":
        msg = request.POST.get('chat-msg', None)
        c = Chat(user=request.user, message=msg,room=room)
        if msg != '':
            c.save()
        #JsonResponse({'msg': msg, 'user': c.user.username})
        return HttpResponseRedirect(str('/chatpage/'+label +'/home/'))
    else:
        return HttpResponse('Request must be POST.')

@login_required
def Messages(request,label):
    room = get_object_or_404(Chatroom,label=label)
    c=Chat.objects.filter(room=room)
    return render(request, 'chat_app/messages.html', {'chat': c})

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        chat_rooms = Chatroom.objects.order_by('name')[:5]
        context = {
        'chat_list': chat_rooms,
        }
        return render(request,'chat_app/index.html', context)
    else:
        return HttpResponseRedirect('/home/login/?next=/chatpage/')

def chat_room(request, label):
  return HttpResponseRedirect(str('/chatpage/'+label+'/home/'))

class ChatroomCreate(CreateView):
    model=Chatroom
    fields=['name','label']
