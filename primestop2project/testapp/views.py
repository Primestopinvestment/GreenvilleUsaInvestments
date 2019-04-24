from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import  SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.

def home_page(request):
    return render(request,'testapp/home.html')
@login_required
def check_cashing(request):
    return render(request,'testapp/check_cashing.html')

def beer_page(request):
    return render(request,'testapp/beer.html')

def cigarates_page(request):
    return render(request,'testapp/cigarates.html')

def log_out_view(request):
    return render(request,'testapp/logout.html')

def sign_up_view(request):
    form= SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/sign_up.html',{'form':form})


