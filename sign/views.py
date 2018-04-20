from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html')

def login_action(request):
    u"""登录动作"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin':
            # return HttpResponseRedirect('/event_manage/')
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)   # 添加浏览器cookie
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

def event_manage(request):
    u"""发布会管理"""
    # return render(request, "event_manage.html")
    # username = request.COOKIES.get('user', '')   # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "event_manage.html", {"user": username})
