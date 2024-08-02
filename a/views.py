from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def login(request):
    return render(request,'login.html')
def check(request):
    if request.POST:
        if request.POST['username'] == 'ass' and request.POST['password'] == '65671234567':
            return HttpResponseRedirect('/index/')
        else:
            q='密码错误'
            return render(request,'login.html',{'pa':q})

def index(request):
    return render(request,'index.html')
def star(request):
    return render(request,'star.html')