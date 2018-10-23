from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from .models import users
# Create your views here.
import json


import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_platform.settings")
django.setup()

# 文件列表路径

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media')


def index(request):
    return  render(request,'index.html')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pws = request.POST.get('pws')
        u = users.objects.filter(username=user)
        print(u,user,pws)
        if u and user and pws:
            print(user,pws,u[0].username)
            rsp = {'status': 1, 'data': {'username':u[0].username},'message':''}
            return HttpResponse(json.dumps(rsp))
        else:
            rsp = {'status':0,'data':{},'message':'用户名错误'}
            return HttpResponse(json.dumps(rsp))
    else:
        return render(request,'login.html')


def wiki(request):
    files = os.listdir(file_path)
    return render(request,'wiki.html',{'files':files})


def upload_file(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        f = open(os.path.join(file_path, file_obj.name), 'wb')
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('OK')