from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['phone_number']
        email = request.POST['email']
        #print(first_name,last_name,username)
        # user = auth.authenticate(username = email,password = password)
        if User.objects.filter(username = username).exists():
            messages.info(request,'An Account with this phone number already exist _')
            return render(request,'account/signup.html')
        if len(username)==0 or len(username)<10:
            messages.info(request,'Invalid Phone number _')
            return render(request,'account/signup.html')
        
        
        password = request.POST['pass']
        
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)    
        
        messages.info(request,'Account created Successfully!')    
        user.save()
       # send_mail(
        #    'Welcome to Shrishti Abhushan!!!',
         #   'Thanks for giving your time!',
          #  'Shristisarvagya@gmail.com',
           # [email],
            #fail_silently=False,
       # )
            
        return render(request,'account/login.html')
    else:
        return render(request,'account/signup.html')

def login(request):
    
    if request.method == 'POST':
        email = request.POST['phone_number']
        password = request.POST['password']
        
        user = auth.authenticate(username = email,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials _')
            return redirect('login')
    else:
        return render(request,'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

