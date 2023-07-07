from django.shortcuts import render
from django.http import HttpResponse
from.models import Teacher
# from.forms import TeacherForms





# Create your views here.

# def te_forms(request):
#     form=TeacherForms()
#     return render(request,'std_frm.html',{'form':form})

    


def reg (request):
   if request.method=='post':
    a1=request.post['a']
    b2=request.post['b']
    c3=request,post['c']
    data=Teacher.object.create(name=a1,age=b2,address=c2)
    data.save() 
    return render(request,registration.html)









def displayvw(request):
    obj=Student.object.all()
    return render(render,'display1.html',{'data':obj})





















def msg(request):
    return HttpResponse('....hi robin...')

def index(request):
     return render(request,'index.html')

def display(request):
    x="hello"
    return render(request,'display.html',{"data":x})

def add(request):
    a=5
    b=3
    c=a+b
    return render(request,'display.html',{'data1':a,'data2':b,'data3':c})



def sub(request):
    x=5
    y=3
    z=x-y
    return render(request,'display.html',{'data1':x,'data2':y,'data3':z})


def reverse(request):
    a="hi"
    rev=""
    for i in a:
        rev = i+rev
    return render(request,'display.html',{'data':rev})    