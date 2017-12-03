from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def userspecific(request):
    user=request.user
    return HttpResponseRedirect('/home/')
