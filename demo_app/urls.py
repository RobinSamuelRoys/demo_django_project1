from django.urls import path
from .import views

urlpatterns=[
    path('reverse/',views.reverse),
    path('add/',views.add),
    path('sub/',views.sub),
    path('display/',views.display),
    path('index/',views.index),
    path('ms/',views.msg),
    path('reg/',views.reg),
    
    # path('te_frm/',views.te_form)
    

]