from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

def index(request):
   
    dic = {
        "name":"luuna",
        "grade":"2"
    }
    dic1 = {"num":dic}
    return render(request, 'app.html',context=dic1)

# def viewsdemo(request):
#     name = request.POST.get("name")
#     return HttpResponse('姓名：{}'.format(name))
def viewsdemo(request):

    return redirect("/index/")

def index2(request, year,month):
    print(year,month) # 一个形参代表路径中一个分组的内容，按顺序匹配
    return HttpResponse('按照路由打印年份月份')