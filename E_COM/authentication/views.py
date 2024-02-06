from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponsePermanentRedirect
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generateToken
import hashlib

# Create your views here.

def login_home(request):
    return render(request, "authentication/loginIndex.html")

def signup(request):

    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists, Try some Other Username")
            return redirect("auth_Index/")
            
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered !")
            return redirect("auth_Index/")

        if len(username)>15:
            messages.error(request, "Username must be under 15 characters.")
            return redirect("auth_Index/")
        
        if pass1!=pass2:
            messages.error(request, "Passwords did not match !")
            return redirect("auth_Index/")

        if not username.isalnum():
            messages.error("Username must Alpha-numeric no speacial characters allowed.")
            return redirect("auth_Index/")
        
        #encrypting the password
        pass1=hashlib.sha1(pass1.encode())
        pass1=pass1.hexdigest()

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.is_active=False

        myuser.save()
        messages.success(request, "Your account has been created Successfully. We have sent you an email, please confirm your email to activate your account. ")

        #Welcome Email
        subject="Welcome to 3D-Bazar - Login authentication!!"
        message="Hello "+ myuser.first_name +"!! \n"+"Welcome to 3D-Bazar an new emerging 3D-model marketplace. \nThank you for visiting out website. \nWe have also sent you the confirmation email, please confirm your email address in order to activate your account.\n If confirmation email doesn't shows please check in the spam of your email.[Its not a spam !] \n Thanking you from the team of 3D-Bazar."
        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]

        send_mail(subject,message,from_email,to_list, fail_silently=True)

        #Email Address Confirmation email
        current_site=get_current_site(request)
        email_subject="Confirm your email @ 3D-Bazar!!"
        message2=render_to_string('email_confirmation.html',{'name':myuser.first_name,
                                                             'domain':current_site.domain,
                                                             'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
                                                             'token':generateToken.make_token(myuser)
                                                             })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )

        email.fail_silently=True
        email.send()

        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signin(request):

    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')

        pass1=hashlib.sha1(pass1.encode())
        pass1=pass1.hexdigest()
        
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            
            fname = user.first_name
            url='/product_index/?username={}'.format(fname)
            return HttpResponsePermanentRedirect(url)
            
            #in order to connect web pages you need to save all pages in one app
            #return render(request, "authentication/loginIndex.html",{'fname':fname})

        else:
            messages.error(request, "Bad Credentials !")
            return redirect('auth_Index')

    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "logged Out Successfully.")
    return redirect('auth_Index')

def activate(request, uidb64, token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        myuser=User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser=None

    if myuser is not None and generateToken.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request,myuser)
        return redirect('/auth_Index/')
    else:
        return render(request, "activation_failed.html")
    

def products(request):
    return render(request, 'index.html')