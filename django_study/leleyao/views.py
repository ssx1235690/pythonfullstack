from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from leleyao import models

# Create your views here.
def sxsong(request):
    print('xxxxx')
    return HttpResponse('sxsong is my father')
def leleyao(request):
    print('xxxxx')
    xxx=models.Author()
    xxx.name='leleyao'
    xxx.save()
    return HttpResponse('qing is my mother')
