from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

# Create your views here.
def index(request):  
    return render(request,'index.html', {})

def registration_community(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('You have succesfully signed up in our systems. Congrats!!!'))
        return render(request,'index.html', {})
    else:
        return render(request,'registration_community.html', {})