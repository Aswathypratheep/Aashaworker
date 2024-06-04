# from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from government.models import *
from datetime import datetime
# import MySQLdb
# # import pymysql
# import simplejson as json
# import random
# import urllib.request
# import webbrowser
# from datetime import date

# conn = MySQLdb.connect("localhost", "root", "", "babycare")
# c = conn.cursor()


def doctorhome(request):
    return render(request, 'Doctor_home.html')


def viewmothers(request):
    id=request.session["id"]
    pan=Panchayat.objects.get(id=id)
    print(pan.id)

    data=Workers.objects.filter(panchayat=pan.id)
    print(data)
    return render(request, 'doctor_View_Mother.html', {"data": data})


def addfood(request):
    data=Panchayat.objects.all()
    pid=request.session["id"]

    foodneed=Foods.objects.filter(panchayat=pid)
    if request.POST:
        
        district = request.POST["district"]
        pan = request.POST["pan"]
        panch=Panchayat.objects.get(id=pan)
        wan = request.POST["wan"]
        need = request.POST["need"]        
        address = request.POST["address"]
        dte=datetime.today()
        phn = request.POST["phn"]

        user=Foods.objects.filter(con=phn).exists()
        if user:
            messages.info(request,"Request already exists")
        else:
           
                try:
                    s=Foods.objects.create(district=district,panchayat=panch,needs=need,con=phn,add=address,ward=wan,date=dte)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Request successfully")
    return render(request,"addfood.html",{"data":data,"Food":foodneed})


def addvaccination(request):
    data=Panchayat.objects.all()
    pid=request.session["id"]

    vaccine=Vaccine.objects.filter(panchayat=pid)
    if request.POST:
        
        district = request.POST["district"]
        pan = request.POST["pan"]
        panch=Panchayat.objects.get(id=pan)
        wan = request.POST["wan"]
        need = request.POST["title"]        
        address = request.POST["address"]
        dte=datetime.today()
        valid=request.POST["valid"]
        time=request.POST["time"]
        phn = request.POST["phn"]

        user=Vaccine.objects.filter(con=phn).exists()
        if user:
            messages.info(request,"Request already exists")
        else:
           
                try:
                    s=Vaccine.objects.create(district=district,panchayat=panch,title=need,con=phn,add=address,ward=wan,date=dte,valid=valid,time=time)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Request successfully")
    return render(request,"addvaccination.html",{"data":data,"Vaccine":vaccine})

# def docViewBookings(request):
#     doctor_id = request.session['userid']
#     qry = f"SELECT * FROM `booking` b, `mother_reg` m WHERE b.`doctor_id`='{doctor_id}' AND b.`mother_id`=m.`mother_id` ORDER BY b.`bkid` DESC"
#     c.execute(qry)
#     data = c.fetchall()
#     return render(request, "docViewBookings.html", {"data": data})
