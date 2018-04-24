from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
from sign.models import Event, Guest


def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html')

def login_action(request):
    u"""登录动作"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)   # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            # return HttpResponseRedirect('/event_manage/')
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)   # 添加浏览器cookie
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    u"""发布会管理"""
    # return render(request, "event_manage.html")
    # username = request.COOKIES.get('user', '')   # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    event_list = Event.objects.all()
    return render(request, "event_manage.html", {"user": username, "events": event_list})

@login_required
def search_name(request):
    u'''发布会搜索'''
    username = request.session.get('user', '')
    name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})

@login_required
def guest_manage(request):
    u'''嘉宾管理'''
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})

@login_required
def search_phone(request):
    u'''嘉宾搜索'''
    username = request.session.get('user', '')
    phone = request.GET.get("phone", "")
    print (phone)
    guest_list = Guest.objects.filter(phone__contains=phone)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})
