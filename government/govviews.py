# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import *
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


# def sendsms(ph, msg):
#     sendToPhoneNumber = "+91"+ph
#     userid = "2000022557"
#     passwd = "54321@lcc"
#     url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + \
#         "&msg=" + msg + "&userid=" + userid + "&password=" + \
#         passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
#     # contents = urllib.request.urlopen(url)
#     webbrowser.open(url)


def adminhome(request):
    return render(request, 'Adminhome.html')


# def panchayathlink(request):
#     return render(request, 'Panchayathlink.html')


def panchayathreg(request):
    if request.POST:
        pname = request.POST["pname"]
        district = request.POST["district"]
        wno = request.POST["wno"]
        hno = request.POST["hno"]
        president = request.POST["president"]        
        address = request.POST["address"]
        email = request.POST["email"]
        phn = request.POST["phn"]

        user=Panchayat.objects.filter(email=email,con=phn).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            try:
                u=CustomUser.objects.create_user(username=email,email=email,password=phn,usertype="panchayat")
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
           
                try:
                    s=Panchayat.objects.create(name=pname,con=phn,email=email,add=address,president=president,district=district,wno=wno,hno=hno)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Registered successfully")
    return render(request, 'PanchayathReg.html')


def viewpanchayath(request):
    data=Panchayat.objects.all()
    return render(request, 'viewpanchayath.html', {"data":data})


# def workerlink(request):
#     return render(request, 'Workerlink.html')


def workerreg(request):
    data=Panchayat.objects.all()
    if request.POST:
        district = request.POST["district"]
        panchayath = request.POST["panchayathlist"]
        pan=Panchayat.objects.get(id=panchayath)
        wnamee = request.POST["wnamee"]
        wphnu = request.POST["wphnu"]
        wan = request.POST["wan"]
        waddress = request.POST["waddress"]
        wmail = request.POST["wmail"]
        qul = request.POST["qul"]

        user=Workers.objects.filter(email=wmail,con=wphnu).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            try:
                u=CustomUser.objects.create_user(username=wmail,email=wmail,password=wphnu,usertype="worker")
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                try:
                    s=Workers.objects.create(name=wnamee,con=wphnu,email=wmail,add=waddress,user=u,panchayat=pan,district=district,wan=wan,qul=qul)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Registered successfully")
    return render(request, 'workerreg.html',{"data":data})


# def panchayathlistview(request):
#     pan_list = []
#     did = request.GET.get("d_id")
#     c.execute(
#         "select panchayath_id,name from panchayath_reg where district ='" + str(did)+"'")
#     data2 = c.fetchall()
#     for d in data2:
#         pan_list.append(d[1])
#     return HttpResponse(json.dumps(pan_list), content_type="application/json")


def viewworker(request):
    data=Workers.objects.all()
    return render(request, 'viewworker.html', {"data": data})


def projectlink(request):
    return render(request, 'Project_link.html')


def addproject(request):
    data=Panchayat.objects.all()
    if request.POST:
        district = request.POST["district"]
        panchayath = request.POST["panchayathlist"]
        p=Panchayat.objects.get(id=panchayath)
        ptitle = request.POST["ptitle"]
        pdescription = request.POST["pdescription"]
        valiupto = request.POST["valiupto"]
        posteddate = datetime.today()

        user=Projects.objects.filter(title=ptitle).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            
                try:
                    s=Projects.objects.create(valid=valiupto,details=pdescription,date=posteddate,district=district,panchayat=p,title=ptitle,status="Active")
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Added successfully")

    return render(request, 'Add_project.html',{"data":data})


def viewprojects(request):
    # view_projects = "select * from projects"
    
    # c.execute(view_projects)
    view_data = Projects.objects.all()

    return render(request, 'viewprojects.html', {"data": view_data})


# def doctorlink(request):
#     return render(request, 'Doctor_link.html')


def adddoctor(request):
    data=Panchayat.objects.all()
    if request.POST:
        district = request.POST["district"]
        panchayath = request.POST["panchayathlist"]
        dname = request.POST["dname"]
        dqual = request.POST["dqual"]
        daddress = request.POST["daddress"]
        dphnu = request.POST["dphnu"]
        dopt = request.POST["dopt"]
        pan=Panchayat.objects.get(id=panchayath)

        user=Doctors.objects.filter(name=dname,dphnu=dphnu).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            try:
                u=CustomUser.objects.create_user(username=dname,password=dphnu,usertype="doctor")
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                try:
                    s=Doctors.objects.create(name=dname,dphnu=dphnu,add=daddress,user=u,panchayat=pan,district=district,opt=dopt,qual=dqual)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Registered successfully")
    return render(request, 'Add_Doctor.html',{"data":data})


def viewdoctor(request):
    data=Doctors.objects.all()
    return render(request, 'viewdoctor.html', {"data":data})




def allviews(request):
    return render(request, 'All_Views.html')


def view_vacc(request):
    view_data=Vaccine.objects.all()
    return render(request, 'View_Vaccination.html', {"data": view_data})


def view_food(request):
    view_data=Foods.objects.all()
    return render(request, 'View_food.html', {"data": view_data})


def view_worker(request):
    view_data=Workers.objects.all()
    return render(request, 'View_Disease.html', {"data": view_data})


def view_panchayat(request):
    view_data=Panchayat.objects.all()
    return render(request, 'View_Health.html', {"data": view_data})


# def deletepanchayath(request):
#     pid = request.GET.get("pid")
#     del_pan = "delete from panchayath_reg where panchayath_id='"+str(pid)+"'"
#     c.execute(del_pan)
#     return HttpResponseRedirect("/viewpanchayath")


# def deleteworker(request):
#     wid = request.GET.get("wid")
#     del_wrkr = "delete from worker_reg where wrkr_id='"+str(wid)+"'"
#     del_login = "delete from login where userid='" + \
#         str(wid)+"' and usertype='worker'"
#     c.execute(del_wrkr)
#     c.execute(del_login)
#     return HttpResponseRedirect("/viewworker")


def deleteproject(request):
    pr_id = request.GET.get("id")
    data=Projects.objects.get(id=pr_id).delete()
    return redirect("/viewprojects")


# def deletedoctor(request):
#     dr_id = request.GET.get("dr_id")
#     del_dr = "delete from doctor where doctor_id='"+str(dr_id)+"'"
#     del_login = "delete from login where userid='" + \
#         str(dr_id)+"' and usertype='doctor'"
#     c.execute(del_login)
#     c.execute(del_dr)
#     return HttpResponseRedirect("/viewdoctor")
