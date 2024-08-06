# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from .models import TimeTest
from datetime import datetime

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        name = request.POST['n']
        cons = request.POST['q']
        if len(name) and len(cons)>0:
            test1 = TimeTest(name=name,cons=cons)
            #Test.objects.all().delete()
            test1.save()
        
    listTest = TimeTest.objects.all()
    res = ""
    li=[]
    dic={}
    for var in listTest:
        li.append({"name":var.name,
                   "cons":var.cons,
                   "time":var.updated_at
                   })
    dic={
       
        "list":li
    }
    
    return render(request, 'post.html',context=dic)