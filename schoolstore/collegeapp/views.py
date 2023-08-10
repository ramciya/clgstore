from django.contrib import messages, auth
from django.contrib.auth.models import User,HttpResponse
from django.shortcuts import render, redirect,get_object_or_404



def home(request):
    return render(request,"navbar.html")


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            user = User.objects.create_user(username=username,password=password, cpassword=cpassword)
            user.save();
            print("user is created")
            return redirect("login.html")

        else:
            print("password not matching")
    return render(request, "register.html")

def login(request):

     if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenicate(username=username, password=password)


            return render(request,"newpage.html")

     else:
        return render(request,"login.html")

def newpage(request):

    if request.method == 'POST':

        name = request.POST['name']
        dob = request.POST['DOB']
        age = request.POST['AGE']
        gender = request.POST['gender']
        phonenumber= request.POST['phonenumber']
        mailid = request.POST['mailid']
        address = request.POST['Address']
        Courses= request.POST['Courses']
        Departments= request.POST['Departments']
        purpose = request.POST['purpose']
        material = request.POST['username']

    return render(request,"newpage.html")