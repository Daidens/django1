from django.urls import path,re_path
from . import views,testdb,search,search2

urlpatterns = [
    
    path('index/', views.index,name='index'),
    path('viewsdemo/', views.viewsdemo),
    path('testdb/', testdb.testdb),
    path('searfo/', search.search_form),
    path('search/', search.search),
    path('Message-Board/', search2.search_post,name="message"),
    re_path("^index/([0-9]{4})/([0-9]{2})/$", views.index2),

    


    
    
]