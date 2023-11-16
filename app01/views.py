from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    # 默认去app01目录下面寻找templates寻找user_list
    # 优先寻找app01目录下的，不回去根目录
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def tql(request):
    name = '李嘉骏'
    roles = ['管理员','CEO','保安' ]
    salary_info = {'name':'李嘉骏', 'selary':'10000'}


    return render(request,"tql.html",{'n1':name,'n2':roles,'n3':salary_info})

def news(request):
    import requests
    from bs4 import BeautifulSoup
    url = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2023/02/news"
    headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 Edg/119.0.0.0"}
    res = requests.get(url, headers=headers)
    data_list = res.json()

    return render(request,"news.html",{"news_list":data_list})

def something(request):
    

    # return render(request,"something.html")

    # 浏览器重定向
    return redirect("https://www.baidu.com")



def login(request):
    if request.method == "GET":
        return render(request,login.html)
    else:
        # 如果是post请求，则获得用户提交的数据
        print(request.POST)
        return HttpResponse("登录成功！")








