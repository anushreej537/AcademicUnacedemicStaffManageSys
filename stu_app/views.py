from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# from django.contrib.auth import authenticate
from django.contrib import auth
from django.urls import reverse
# from django.conf import settings
# curl=settings.CURRENT_URL
# Create your views here.

# def registration(request):
#     if request.method == 'POST':
#         name = request.POST['uname']
#         email = request.POST['email']
#         pas
# sword = request.POST['password']
#         usertype = request.POST['usercheck']
#         if usertype=='academic':
#             return render(request,'academic.html')
#         elif usertype=='nonacademic':
#             return render(request,'nonacademic.html')
#         elif usertype=='student':
#             return render(request,'student.html')
#         User_registration.objects.filter(name=name,email=email,password=password,usertype=usertype).exists()
#         return redirect('/login/')
#     else:
#         return redirect('/registration/')
    

# def login(request):
#     if request.method == 'POST':
#         return redirect('/dash/')
#     else:
#         return render(request,'main/login.html')
    

def signup(request):
    if request.method == 'POST':
        names = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        usertype = request.POST['usercheck']
        # if usertype=='academic':
        #     return render(request,'main/academic.html')
        # elif usertype=='nonacademic':
        #     return render(request,'main/nonacademic.html')
        # elif usertype=='student':
        #     return render(request,'main/student.html')
        User_registration.objects.create(names=names,email=email,password=password,usertype=usertype)
        messages.success(request,'user registered successfully')
        return render(request,'main/login.html')  
    else:
        return render(request,'main/signup.html')  

def login(request):
    return render(request,'main/login.html')

def login_user(request):
    print(request.method)
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        if User_registration.objects.filter(email=email).exists():
            obj=User_registration.objects.filter(email=email).first()
            if User_registration.objects.filter(password=password).exists():
                if obj.usertype=='academic':
                    request.session['user_id']=obj.id
                    user_id = request.session['user_id']
                    url = reverse('home',args=[ user_id ])
                    return redirect(url)

                    # return redirect('/home/')
                elif obj.usertype=='nonacademic':
                    return redirect('/nonacademic/')
                else:
                    return redirect('/student/')
            else:
                messages.error(request,'password incorrect')   
                return redirect('/login/')
        else:
            messages.error(request,'email not registered')
            return redirect('/login/')
    else:
        return redirect('/home/')

def base(request):
    return render(request,'main/base.html')

def academic_dashboard(request):
    return render(request,'main/academic_dashboard.html')

def nonacademic(request):
    return render(request,'main/nonacademic.html')


def student(request):
    return render(request,'main/student.html')

def home(request,user_id):
    try:
        if user_id:
            print(dict(request.session))
            return render(request,'main/home.html',{'user_id':user_id})
        else:
            return redirect('/logout/')
    except:
        return redirect('/logout/')
def logout(request):
    if User_registration is not None:
        request.session.pop('user_id', None)
        # return redirect('logout_success_url')
        return redirect('/')
    else:
        # request.session.pop('user_id', None)
        return redirect('/logout/')
        # return redirect(str(curl)+'mpeb_login')

# def logout(request):
#     if user_