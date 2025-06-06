from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User 
from war_risk.models import *
import re
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from .trackingenemyloc import track_enemy_movements
import os


# Create your views here.
def home(request):
    return render(request,'home.html')

def home(request):
    map_obj = track_enemy_movements()
    return render(request,'home.html',{'map_obj': map_obj})

def signup(request):
    return render(request,'signup.html')

def signuplogic(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    password_pattern = r'[a-zA-Z0-9_]{8,16}[\W]$'
    if not email or not password:
        return JsonResponse({'success':False,'error':"All fields are required!"},status=400)
    if not re.match(password_pattern,password):
        return JsonResponse({'success':False,'error':'Password must be atleast 8 characters long containing one special character'},status=400)
    if User.objects.filter(email=email).exists():
        return JsonResponse({'success':False,'error':"Username already exists"})
    if User.objects.filter(password=password).exists():
        return JsonResponse({'success':False,'error':"Password already exists"})
    
    website_user = User.objects.create_user(
        username=email,
        email=email,
        password=password
    )

    website_user.set_password(password)
    website_user.save()

    if website_user is not None:

        messages.info(request, "Account created Successfully!")
        return redirect('../login1',foo="bar")

    return render(request,'signup.html')

def login1(request):
    return render(request,'login1.html')

def login_page(request):
    return render(request,'login.html')

def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        #if email entered is not found in the database
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request,username=user_obj.username,password=password)

            #display an error message if authentication fails (invalid password)
            '''if user is None: 
                return JsonResponse({'message':'authentication failed'})
                messages.error(request,'Invalid username')
                return redirect('../login')
            else:    
                #login the user
                login(request,user_obj)
                return redirect('../home')'''
            if user is not None: 
                #login the user
                login(request,user)
                return redirect('../home')
            else:   
                messages.error(request,'Invalid password')
                return redirect('../login')
            
        except User.DoesNotExist:
            messages.error(request,'Invalid username')
            return redirect('../login')

    return render(request,'login.html')

def upload(request):
    return render(request,'upload.html')

def upload_files(request):
    if request.method == 'POST' and request.FILES["th_img"]:
        file = request.FILES["th_img"]
        fs = FileSystemStorage()
        filename = fs.save(file.name,file)
        GunImage.objects.create(file=filename)
        #return JsonResponse({"message":"File uploaded succesfully",filename: "filename"})
        return redirect('/tracking_dashboard')

def tracking_dashboard(request):
    return render(request,'tracking.html')

def tracking_dashboard(request):
    #retrieve from model
    files = GunImage.objects.all()
    if not files:
        print("Not found")
    '''if obj and obj.file:
        file_path = obj.file.path
        if os.path.exists(file_path):
            with open(file_path,encoding='utf-8') as f:
                file_content = f.read()'''
    return render(request,'tracking.html',{'files':files})
    '''track = Tracking(request)
    fs = FileSystemStorage()
    root_location = fs.location
    print(root_location)
    return render(request,'tracking.html',{'data':fs.files})
    return render(request, 'tracking.html', {'content': 'No file found'})'''

        

