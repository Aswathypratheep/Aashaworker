
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# import MySQLdb
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from government.models import *
from datetime  import date

# conn = MySQLdb.connect("localhost", "root", "", "babycare")
# c = conn.cursor()


def index(request):
    return render(request, 'home.html')


def login(request):
    
        if request.POST:
            username = request.POST['username']
            password = request.POST['pass']
            user=authenticate(username=username,password=password)
        
           
            if user:
                userdata=CustomUser.objects.get(username=username)
                if userdata.is_superuser == 1:
                        return redirect("/adminhome/")
                # elif userdata.usertype == "doctor":
                #         request.session["email"]=username
                #         r = Doctors.objects.get(name=username)
                #         request.session["id"]=r.id
                #         request.session["name"]=r.name
                #         return redirect("/doctorhome/")
                elif userdata.usertype == "panchayat":
                        request.session["email"]=username
                        r = Panchayat.objects.get(email=username)
                        request.session["id"]=r.id
                        request.session["name"]=r.name
                        return redirect("/doctorhome")
                elif userdata.usertype == "worker":
                        request.session["email"]=username
                        r = Workers.objects.get(email=username)
                        request.session["id"]=r.id
                        request.session["name"]=r.name
                        return redirect("/workerhome")
                else:
                        request.session["email"]=username
                        r = Mothers.objects.get(name=username)
                        request.session["id"]=r.id
                        request.session["name"]=r.name
                        return redirect("/motherhome")
            else:
                messages.info(request,"User dosent exist")
        return render(request, 'login.html')
