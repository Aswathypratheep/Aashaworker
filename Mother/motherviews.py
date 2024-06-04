# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import redirect, render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from government.models import *
# import MySQLdb
# from flask import request_tearing_down
# # import pymysql
# import simplejson as json
# import random
# import urllib.request
# import webbrowser
# from datetime import date

# conn = MySQLdb.connect("localhost", "root", "", "babycare")
# c = conn.cursor()


def motherhome(request):
    return render(request, 'Mother_home.html')


def vaccination_alerts(request):
    id=request.session["id"]
    mom=Mothers.objects.get(id=id)
    view_data=Vaccine.objects.filter(panchayat=mom.panchayat)

    return render(request, 'Vacc_Alerts.html', {"data": view_data})


def food_details(request):
  
    id=request.session["id"]
    mom=Mothers.objects.get(id=id)
    view_data=Foods.objects.filter(panchayat=mom.panchayat)



    return render(request, 'Food_Details.html', {"data": view_data})


# def health_tips(request):
#     mother_id = request.session['userid']
#     get_panchayah = f"select district,panchayath,phone_number,wrker_id from mother_reg where mother_id='{mother_id}'"
#     c.execute(get_panchayah)
#     mthr_details = c.fetchone()
#     view_food = "select * from health_tips where wrkr_id='" + \
#         str(mthr_details[3])+"'"
#     c.execute(view_food)
#     view_data = c.fetchall()
#     return render(request, 'Health_Tips.html', {"data": view_data})


# def disease_details(request):
#     mother_id = request.session['userid']
#     get_panchayah = "select district,panchayath,phone_number,wrker_id from mother_reg where mother_id='" + \
#         str(mother_id)+"'"
#     c.execute(get_panchayah)
#     mthr_details = c.fetchone()
#     view_disease = "select d.disease_id,d.details,doc.dname,doc.qualification,doc.address,doc.phone_no,doc.optime, doc.doctor_id from disease d,doctor doc where d.wrkr_id='" + \
#         str(mthr_details[3])+"' and doc.doctor_id=d.doc_id"
#     c.execute(view_disease)
#     view_data = c.fetchall()
#     return render(request, 'Disease_Details.html', {"data": view_data})


# def bookDoc(request):
#     mothid = request.session['userid']
#     docid = request.GET['docid']
#     if request.method == "POST":
#         date = request.POST['date']
#         desc = request.POST['desc']
#         qry = f"INSERT INTO `booking` (`doctor_id`,`mother_id`,`booking_date`,`desc`) VALUES ('{docid}','{mothid}','{date}','{desc}')"
#         c.execute(qry)
#         conn.commit()
#         return redirect("/motherBookings")
#     return render(request, "bookDoc.html")


# def motherBookings(request):
#     mothid = request.session['userid']
#     qry = f"SELECT * FROM `booking`b, `doctor`d WHERE b.`mother_id`='{mothid}' AND b.`doctor_id`=d.`doctor_id` ORDER BY b.`bkid` DESC"
#     c.execute(qry)
#     data = c.fetchall()
#     return render(request, "motherBookings.html", {"data": data})
