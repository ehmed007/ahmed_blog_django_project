from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import contact_form, signup_form, login_form, blogs_form
from .models import contact, blogs
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.cache import cache
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    data = blogs.objects.all().order_by('id')   
    page_data = Paginator(data, 3, orphans=1)
    pg_number = request.GET.get('page')
    page_obj = page_data.get_page(pg_number)
    return render(request, 'app1/home.html',{'data':page_obj})
    
def about(request): 
    return render(request, 'app1/about.html')
    
def contact(request):
    if request.method == 'POST':
        fm = contact_form(request.POST)
        if fm.is_valid():
            messages.error(request, 'Your form is submitted successfully!', extra_tags='signup')
            fm.save()
            fm = contact_form()
            return render(request, 'app1/contact.html',{'form':fm})
        return render(request, 'app1/contact.html',{'form':fm})
    fm = contact_form()
    return render(request, 'app1/contact.html',{'form':fm})
    
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_user_name()

        ip = request.session.get('ip',0)
        ct = cache.get('count', version=user.pk)
        # if ct >= 4:
            # do_logout(request)
            # return HttpResponseRedirect('/login/')

        if user_name != 'admin':
            data = blogs.objects.filter(usernamee=user_name)
        else:
            data = blogs.objects.all()
        if request.method == 'POST':
            fm = blogs_form(request.POST)
            fm.save()
        
        # data = blogs.objects.all().order_by('id')
        page_data = Paginator(data, 3)
        pg_number = request.GET.get('page')
        page_obj = page_data.get_page(pg_number)

        fm = blogs_form()
        return render(request, 'app1/dashboard.html',{'form':fm,'data':page_obj,'username':user_name,'ip':ip,'ct':ct})
    else:
        return HttpResponseRedirect('/login/')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = signup_form(request.POST)
            if fm.is_valid():
                user = fm.save()
                group = Group.objects.get(name='simple_user')
                user.groups.add(group)
                messages.error(request, 'Your Account has been Created!', extra_tags='signup')
                fm = signup_form()
                return render(request, 'app1/signup.html',{'form':fm})

            return render(request, 'app1/signup.html',{'form':fm})
        fm = signup_form()
        return render(request, 'app1/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
    
    
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = login_form(request=request, data=request.POST)
            uname = request.POST['username']
            passw = request.POST['password']
            if fm.is_valid():
                usr = authenticate(username=uname,password=passw)
                if usr is not None:
                    do_login(request, usr)
                    return HttpResponseRedirect('/dashboard/')  

            messages.error(request, 'Incorrect username or password', extra_tags='login')
            return render(request, 'app1/login.html',{'form':fm})        
        fm = login_form()
        return render(request, 'app1/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
     
def logout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            do_logout(request)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse('<h1>404 page not found!</h1>')
    else:
        return HttpResponseRedirect('/login/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            user_name = user.get_user_name()
            obj = blogs(title=request.POST['title'],description=request.POST['description'], usernamee=user_name)
            obj.save()

        fm = blogs_form()
        return render(request, 'app1/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = blogs.objects.get(pk=id)
            obj.title = request.POST['title']
            obj.description = request.POST['description']
            obj.save()
            return HttpResponseRedirect('/dashboard/')
        obj = blogs.objects.get(pk=id)
        fm = blogs_form(instance=obj)        
        return render(request, 'app1/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = blogs.objects.get(pk=id)
            obj.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')