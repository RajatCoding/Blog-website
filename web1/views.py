from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, SignUp,AuthPost,Profile_Change
from .models import Post
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.


#Home
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'post':posts})





#About Us
def about_us(request):
    return render(request, 'about_us.html',)

#Contact Us
def contact_us(request):
    return render(request, 'contact_us.html')





#Sign Up
def user_signup(request):
    fm = SignUp()
    if request.method == 'POST':
        fm = SignUp(request.POST)
        if fm.is_valid():
            messages.success(request,'You are registered successfully')
            fm.save()
            # return HttpResponseRedirect('/')
    return render(request, 'signup.html', {'form': fm})
    







def user_login(request):
        if not request.user.is_authenticated:
            if request.method == 'POST':
                fm = LoginForm(request=request, data=request.POST)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    upass = fm.cleaned_data['password']
                    chaplin = authenticate(password=upass, username=uname)
                    if chaplin is not None:
                        login(request, chaplin)
                        messages.success(request,'Logged in successfully')
                        return HttpResponseRedirect('/dashboard/')
            else:
                fm = LoginForm()
            return render(request, 'login.html', {'form': fm})
        else:
            return HttpResponseRedirect('/dashboard/')
        

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def dashboard(request):
        if request.user.is_authenticated:
            post = Post.objects.all()

            return render(request, 'dashboard.html',{'name': request.user.first_name, 'post':post})
        else:
            return HttpResponseRedirect('login')
    

#addpost
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthPost(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                form = AuthPost()
        else:
            form = AuthPost()
        
        return render(request,'add.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = Post.objects.get(pk=id)
            form = AuthPost(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                form = AuthPost()
        else:
            pi = Post.objects.get(pk=id)
            form = AuthPost(instance=pi)
        return render(request,'update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request,id):
    if request.user.is_authenticated:
        pi = Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def changeprofile(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                fm = Profile_Change(request.POST,instance = request.user )
                if fm.is_valid():
                    messages.success(request, 'profile updated successfully!!')
                    fm.save()
                    # ')return HttpResponseRedirect('/profile/
                
            else:
                fm = Profile_Change(instance = request.user)
            return render(request, 'edit_profile.html', {'form':fm})

        else:
            return HttpResponseRedirect('/')

#change password
def chanfge_use_password(request):
    return render(request, "add.html")
