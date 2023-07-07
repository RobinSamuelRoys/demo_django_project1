from django.shortcuts import render,redirect
from django.contrib.auth import login
# Create your views here.

# def login_vw(request):
#     return render(request,'login_sucess.html')


# def login_user(request):
#     if request.method=='post':
#         username=request.post['username']   
#         password=request,post['password']
#         user=authenticate(username,password=password)
#         if user is not none:
#             login(request,user)
#             return redirect('/member/lg_su/') 
#     return render(request,'/login.html')    


# def success(request):
#     return render(request,'success.html')


def lg_ss(request):
    return render(request,'login_success.html')