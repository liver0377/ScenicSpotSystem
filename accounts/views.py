from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from .forms import SignUpForm

# Create your views here.
def signup(request):
    """
    第一次调用该函数得到一个空表单
    填写表单有效则返回主页, 否则需要重新填写
    """
    if request.method == "POST":
        form = SignUpForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("home")
    else:
        form = SignUpForm()
    
    return render(request, "signup.html", { "form": form})

 