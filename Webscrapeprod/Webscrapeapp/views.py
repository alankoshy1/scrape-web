from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from . models import Scrap

# Create your views here.
def home(request):
    if request.method== "POST":
        new_scrap=request.POST.get('page','')
        urls=requests.get(new_scrap)
        Beaut=BeautifulSoup(urls.text,'html.parser')
        for link in Beaut.find_all('a'):
            s_address=link.get('href')
            s_name=link.string
            Scrap.objects.create(address=s_address,sitename=s_name)
        return HttpResponseRedirect('/')
    else:
        values=Scrap.objects.all()

    return render(request,'home.html',{'values':values})