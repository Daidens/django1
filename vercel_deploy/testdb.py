# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from vercel_deploy.models import Test
 
# 数据库操作
def testdb(request):
    res = ""
    test1 = Test(name='huyi')
    test1.save()
    listTest = Test.objects.all()
    response2 = Test.objects.get(id=1)
    # response2.name = "Google"
    # response2.save()
    # Test.objects.filter(id=4).update(name='Google')
    # response2.delete()
    for var in listTest:
        res += var.name + " "
    response = res
    return HttpResponse(res)