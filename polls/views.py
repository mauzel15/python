from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO WORLD,YOU ARE AT THE POLLS INDEX")

def detail(request,question_id):
    return HttpResponse("you are looking at question %s." % question_id)

def results(request,question_id):
    response = "you are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." %question_id)