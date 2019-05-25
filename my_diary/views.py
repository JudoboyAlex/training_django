from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from my_diary.models import Diary
from datetime import date

def root_page(request):
    return HttpResponseRedirect('home/')

def home_page(request):
    current_date = date.today()
    context = {
        'diaries': Diary.objects.all(),
        'today': current_date
    }
    response = render(request, 'index.html', context)
    return HttpResponse(response)