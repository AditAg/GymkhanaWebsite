from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.views.generic.base import TemplateView
# from django.http import HttpResponseRedirect
# from django.core.mail import send_mail, BadHeaderError
# from .forms import EmailForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import smtplib
from .models import Emailmessage


@login_required
# def sendmail(request):
#    if request.method == 'POST':
#        form = EmailForm(request.POST)
#
#        if form.is_valid():
#           firstname = form.cleaned_data['firstname']
#           lastname = form.cleaned_data['lastname']
#           email = form.cleaned_data['email']
#           subject = form.cleaned_data['subject']
#           botcheck = form.cleaned_data['botcheck'].lower()
#           message = form.cleaned_data['message']
#          if botcheck == 'yes':
#               try:
#                  fullemail = firstname + " " + lastname + " " + "<" + email + ">"
#                  send_mail(subject, message, fullemail, ['aditagarwal1997@gmail.com','localhost'])
#                   return HttpResponseRedirect('/email/thankyou/')
#              except:
#                    return HttpResponseRedirect('/email/')
#        else:
#            return HttpResponseRedirect('/email/')
#   else:
#       return HttpResponseRedirect('/email/')
def emailform(request):
    if request.user.is_authenticated:
        return render(request, 'emailsmtp/formmail.html', {})
    else:
        return HttpResponseRedirect(str('/home/login/?next=' + request.path))


def select(request):
    return render(request,'emailsmtp/select.html',{})

def emailform2(request):
    if request.user.is_authenticated:
        return render(request, 'emailsmtp/formmail2.html', {})
    else:
        return HttpResponseRedirect(str('/home/login/?next=' + request.path))

def sendmail(request):


    string = request.POST['To']
    sender = request.POST['sender']
    try:
        To = [x.strip() for x in string.split(',')]
    except:
        To = string
    message = 'From:' + str(request.user.username) + '\n To:' + str(request.POST['To']) + '\n' + str(request.POST['message'])
    try:
        server = str(request.POST['server'])
    except:
        server = 'smtp.gmail.com'
    try:
        port = int(request.POST['port'])
    except:
        port = 587
    try:
        passwd = request.POST['password']
    except:
        passwd = 'abc@123'

    try:
        smtpobj = smtplib.SMTP(server, port)
        if server == 'smtp.gmail.com':
            smtpobj.ehlo()
            smtpobj.starttls()
            smtpobj.login(sender, passwd)
        else:
            try:
               user = authenticate(username=sender, password=passwd)
               if user is not None:
                   if user.is_active:
                       login(request, user)
            except:
                error_message="Please specify correct login details or register here"
                return render(request,'emailsmtp/formmail.html',{'error_message':error_message})
        message1="Successfully logged in"
    except:
        message1="Unable to login"
    try:
        smtpobj.sendmail(sender, To, message)
        c=Emailmessage()
        c.username=request.user
        c.To=To
        c.subject=str("A message from User"+str(request.user.username))
        c.From=request.user.username
        c.message=message
        c.save()
        message2="Successfully sent mail"
    except:
        message2="Unable to send mail"

    return render(request,'emailsmtp/thankyou.html',{'message1':message1,'message2':message2})

def sendmail2(request):


    subject = request.POST['To']
    sender = request.POST['sender']
    if subject:
        To='adit.agarwal.cse15@itbhu.ac.in'
    message = 'From:' + str(request.user.username) + '\n To:' + str(request.POST['To']) + '\n' + str(request.POST['message'])
    try:
        server = str(request.POST['server'])
    except:
        server = 'smtp.gmail.com'
    try:
        port = int(request.POST['port'])
    except:
        port = 587
    try:
        passwd = request.POST['password']
    except:
        passwd = '40201017'

    try:
        smtpobj = smtplib.SMTP(server, port)
        print('server')
        if server == 'smtp.gmail.com':
            smtpobj.ehlo()
            smtpobj.starttls()
            print('ping')
            smtpobj.login(sender, passwd)

        else:
            try:
               user = authenticate(username=sender, password=passwd)
               if user is not None:
                   if user.is_active:
                       login(request, user)
            except:
                error_message="Please specify correct login details or register here"
                return render(request,'emailsmtp/formmail.html',{'error_message':error_message})
        message1="Successfully logged in"
    except:
        message1="Unable to login"
    try:
        smtpobj.sendmail(sender, To, message)
        c=Emailmessage()
        c.username=request.user
        c.To=To
        c.subject=subject
        c.From=request.user.username
        c.message=message
        c.save()
        message2="Successfully sent mail"
    except:
        message2="Unable to send mail"

    return render(request,'emailsmtp/thankyou.html',{'message1':message1,'message2':message2})