from django.http import HttpResponse
from django.shortcuts import render
from vercel_deploy.models import Test
# 表单
def search_form(request):
    return render(request, 'search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你的留言内容为：' + request.GET['q']
        submit = request.GET['q']
        name = Test(name=str(submit))
        name.save()

    else:
        message = '你提交了空表单'

    listTest = Test.objects.all()
    res = ""
    li=[]
    dic={}
    for var in listTest:
        li.append(var.name)
    dic={
        "message":message,
        "list":li
    }
    context={"data":dic}
    return render(request, 'search.html',context=context)