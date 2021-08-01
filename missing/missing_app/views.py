from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import User_form,UserProfileInfo_form, Items_lost_form,Contact_us_form
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm


from .models import UserProfileInfo,Items_lost

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

email = 'abc@gmail.com'

def Test_page(request):
    return render(request,'test.html')



def index(request):
    return HttpResponseRedirect('missing_app/home')


def Home_page(request):
    context={}
    return render(request,'home.html',context)


def Sign_up_page(request):
    registered = False
    if request.method == 'POST':
        User_form_obj=User_form(request.POST)
        UserProfileInfo_form_obj=UserProfileInfo_form(request.POST,request.FILES)
        if User_form_obj.is_valid() and UserProfileInfo_form_obj.is_valid() :
            userr = User_form_obj.save()
            userr.set_password(userr.password)
            userr.save()
            profile = UserProfileInfo_form_obj.save(commit=False)
            profile.user = userr
            profile.save()
            registered = True
        else:
            print(User_form_obj.errors,UserProfileInfo_form_obj.errors)
    else:
        User_form_obj = User_form()
        UserProfileInfo_form_obj = UserProfileInfo_form()
    context={'User_form_obj':User_form_obj ,"UserProfileInfo_form_obj":UserProfileInfo_form_obj,"registered":registered   }
    return render(request,'sign_up.html',context)


def Login_page(request):
    if request.method == "POST":
        global email
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        try:
            x=User.objects.get(email = email)
            global username
            username = x.username
            user = authenticate(username = username, password = password)
        except:
            context = {}
            return render(request,'error.html',context)
        if user :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Home_Page'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Some one tried to login and failed!")
            return HttpResponse("Invaid Email or Password!")
    else:
        context={}
        return render(request,'login.html',context)


@login_required
def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home_Page'))


@login_required
def Found_page(request):
    complaints_obj = Items_lost.objects.all().order_by("-timestamp")
    context={"complaints_obj":complaints_obj,}
    return render(request,'found.html',context)


@login_required
def Lost_page(request):
    if request.method == 'POST':
        Items_lost_form_obj = Items_lost_form(request.POST,request.FILES)
        if Items_lost_form_obj.is_valid():
            require_user_profile  = User.objects.get(email = email)
            yy=UserProfileInfo.objects.get(user = require_user_profile.id)
            if yy.status == "Verified":
                abc = Items_lost_form_obj.save(commit = False)
                abc.usernamee = request.user
                abc.emaill = email
                abc.save()
                return HttpResponseRedirect(reverse('Profile_Page'))
            else:
                text = "User Status not yet verified!"
                Items_lost_form_obj = Items_lost_form()
                context={"Items_lost_form_obj":Items_lost_form_obj,"text":text}
                return render(request,'lost.html',context)
        else:
            print(Items_lost_form_obj.errors)
    else:
        Items_lost_form_obj = Items_lost_form()
        context={"Items_lost_form_obj":Items_lost_form_obj}
        return render(request,'lost.html',context)


@login_required
def Profile_page(request):
    require_user_profile  = User.objects.get(email = email)
    require_user_profile_info = UserProfileInfo.objects.get(user = require_user_profile.id)
    user_complaints_obj = Items_lost.objects.filter(usernamee = require_user_profile.id).order_by("-timestamp")
    context={"require_user_profile":require_user_profile,
        'require_user_profile_info':require_user_profile_info,
        "user_complaints_obj":user_complaints_obj,
        }
    return render(request,'profile.html',context)


@login_required
def Contact_page(request):
    if request.method =="POST":
        contact_obj = Contact_us_form(request.POST)
        if contact_obj.is_valid():
            cde = contact_obj.save(commit =False)
            cde.name = request.user
            cde.save()
            textt = "Thank You for messaging us. We will get back to you via mail"
            context={"textt" :textt}
            return render(request,'contact.html',context)

    contact_obj = Contact_us_form()
    context={"contact_obj" :contact_obj}
    return render(request,'contact.html',context)


@login_required
def Found1_page(request):
    context={}
    return render(request,'found1.html',context)
