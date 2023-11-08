from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    # 默认去app01目录下面寻找templates寻找user_list
    # 优先寻找app01目录下的，不回去根目录
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")