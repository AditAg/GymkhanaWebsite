from django.contrib.auth import authenticate, login, logout
# authenticate is used to verify their identity and login is to maintain a session-id
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import LatestNews, Events, Contacts, Userevents
from time import *
from django.contrib.auth.models import User
import smtplib
import base64
from urllib import parse

# Create your views here.
all_news = LatestNews.objects.all()
all_events = Events.objects.all()

urgent = []
unverifiedusers = []
encstring="THISISAUNIQUEMARKER-"

def index(request):
    template = loader.get_template('mainpage/home.html')
    if request.user.is_authenticated:
        user_events = Userevents.objects.filter(user=request.user)
        for event in user_events:
            global urgent
            event_date = event.event_date
            l = list(event_date.split('-'))
            t = strptime(ctime())
            l2 = strftime('%Y %m %d', t).split(' ')
            if (l2 == l):
                urgent.append(event)

        context = {
            'all_news': all_news,
            'all_events': user_events,
            'urgent': urgent,

        }
    else:
        context = {
            'all_news': all_news,
            'all_events': all_events,
            'urgent': urgent,

        }
    return HttpResponse(template.render(context, request))

def contact(request):
    # put content in database
    return render(request,"mainpage/thankyou.html",{'message':"Thank You for submitting your info.We will contact you soon"})


def ContactsCreate(request):
    if request.method == 'POST':
        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_phone = request.POST['contact_phone']
        contact_message = request.POST['contact_message']
        c = Contacts()
        c.contact_name = contact_name
        c.contact_email = contact_email
        c.contact_phone = contact_phone
        c.contact_message= contact_message
        c.save()
        return HttpResponseRedirect('/home/contact/')
    else:
        return HttpResponse('Sorry method should be post')



class UserFormView(View):
    form_class = UserForm
    template_name = 'mainpage/registration_form.html'

    # Rem: The same url can handle two different requests because we may specify different methods(Post or Get) and so
    # for the two methods different requests can be made on url
    # So, we can use if method==POST and if method==GET for the two different requests on same url
    # E.g.-GET to get the form page and POST to submit the form but then the code is large

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form,})

    # submit the form and process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned(normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            unverifiedusers.append(user)

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)

                server.ehlo()

                server.starttls()

                server.login('smtplibproject@gmail.com','45201017')

                enc=base64.b64encode(bytes(encstring+str(user.pk),'utf-8')).decode('utf-8')
                print('dvdss')
                message = """From: From Gymkhana <smtplibproject@gmail.com>
To: To %s <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: User Verification

<h3>Username=%s<br>Password=%s<br>Copy and paste the following link in your url box to verify<br>'127.0.0.1:8000/home/%s/verify'<br></h3>
""" % (username, email, username, password, enc)
                print(message)
                v=[]
                v.append(email)
                server.sendmail('smtplibproject@gmail.com',v, message)
                print('sent')
            except:
                u=User.objects.get(pk=user.pk)
                u.delete()
                return HttpResponse("Couldn't connect to gmail")


            # returns User objects if credentials are correct.
            if user in unverifiedusers:
                return render(request,"mainpage/visit.html",{})
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('mainpage:index')
                    else:
                        return HttpResponse("Inactive User")
                else:
                    return HttpResponseRedirect('/home/register/')

        return render(request, self.template_name, {'form': form})


def Login(request):

    next = request.GET.get('next', str('/home/'))
    if next =='/home/':
        error=""
    else:
        error="Please LogIn First"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            if request.user not in unverifiedusers:
                user = authenticate(username=username, password=password)
            else:
                return HttpResponse('Please verify first<a href="www.gmail.com">Gmail</a>')
        except:
            return render(request, "mainpage/login.html",
                          {'redirect_to': "mainpage:index", 'error_message': 'Sorry provide correct details','error':error})

        if user is not None:
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive User")
        else:
            return render(request, "mainpage/login.html",
                          {'redirect_to': "mainpage:index", 'error_message': 'Sorry provide correct details'})

    return render(request, "mainpage/login.html", {'redirect_to': next})


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/home/")


def UsereventsCreate(request):
    return render(request, 'mainpage/userevents_form.html', {})


def Eventadd(request):
    if request.method == 'POST':
        event_date = request.POST['event_date']
        event_detail = request.POST['event_details']
        event_title = request.POST['event_title']
        event_url = request.POST['event_url']
        c = Userevents()
        c.user = request.user
        c.event_date = event_date
        c.event_detail = event_detail
        c.event_title = event_title
        c.event_url = event_url
        c.save()
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponse('Sorry method should be post')


def UserVerify(request, string):
    global unverifiedusers
    string=base64.b64decode(string).decode('utf-8')
    parse.unquote(string)
    string=list(string.split('-'))[1]
    user_id=int(string)
    user = User.objects.filter(pk=user_id)
    print("dfdfd")
    if user in unverifiedusers:
        unverifiedusers.remove(user)
        print ('dfdfd')
        login(request,user)

        return HttpResponseRedirect('/home/')
    else:

        return HttpResponseRedirect('/home/')

@login_required
def chat(request):
    return render(request,'mainpage/chat.html',{})