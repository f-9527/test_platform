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


#_______________________首页_______________________________________________________________________________

def index(request):
    return  render(request,'index.html')

#_______________________登陆_______________________________________________________________________________

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

#_______________________wiki_______________________________________________________________________________

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

#_______________________接口测试_______________________________________________________________________________

pro_info = ['pro1','pro2','pro3','pro4']

ver_info = {
            'pro1':['v1.11','v1.1.12','v1.3.1'],
            'pro2':['v2.11','v2.1.12','v2.3.1'],
            'pro3':['v3.11','v3.1.12','v3.3.1'],
            'pro4':['v4.11','v4.1.12','v4.3.1'],
           }


pro = [{'p_name':'pro1','p_version':'v1.0', 'IF_count':10, 'IF_add':'http://192.168.50.244/index.html', 'ps':'',},
       {'p_name':'pro2','p_version':'v1.2', 'IF_count':30, 'IF_add':'https://xiaochongtestcube.hc.top/product', 'ps':'',}
       ]

IF = [{'name':'IF1','type':'get','url':'url1','parameter':['para1','para2','para3'],'example':'example1','script':1,'id':0,'ps':'',},
      {'name':'IF2','type':'post','url':'url2','parameter':['para4','para5','para6'],'example':'example2','script':1,'id':1,'ps':'',},
      {'name':'IF3','type':'get','url':'url3','parameter':['para7','para8','para9'],'example':'example3','script':0,'id':2,'ps':'',}]

def interface(request):

    return render(request, 'interface.html', {'product':pro})

def add_IF(request):
    import random
    if request.method == "POST":

        newData = {'p_name':request.POST.get('proName'),
                    'p_version':request.POST.get('version'),
                    'IF_count':request.POST.get('IF_count'),
                    'IF_add':request.POST.get('IF_add'),
                    'ps':request.POST.get('ps'),
                    'id': random.randint(3,100)
                   }
        print(newData)
        pro.append(newData)
        return HttpResponse('OK')


def IF_list(request,pro_id,ver_id):

    return render(request, 'IF_list.html', {'IF_info':IF})

def addsrp(request,IF_id):


    rsp = IF[int(IF_id)]

    print(rsp)
    return render(request, 'srp.html',{'i':rsp})







#_______________________产品_______________________________________________________________________________

def product(request):

    return render(request,'product.html')