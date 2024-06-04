# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from government.models import *
from datetime  import date
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


def workerhome(request):
    return render(request, 'workerhome.html')


# def govnotification(request):
#     ashaworker_id = request.session['userid']
#     get_panchayah = "select district,panchayath,phone_no from worker_reg where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(get_panchayah)
#     wrkr_details = c.fetchone()
#     view_projects = "select * from projects where district='" + \
#         str(wrkr_details[0])+"' and panchayath='"+str(wrkr_details[1])+"'"
#     c.execute(view_projects)
#     view_data = c.fetchall()
#     return render(request, 'gov_notif.html', {"data": view_data})


# def motherlink(request):
#     return render(request, 'mother_link.html')


def addmother(request):
    dates = date.today()
    wid=request.session["id"]
    w=Workers.objects.get(id=wid)
    if request.POST:
       
       
        mname = request.POST["mname"]
        mage = request.POST["mage"]
        maddress = request.POST["maddress"]
        mphone = request.POST["mphone"]
        # district = request.POST["mphone"]
        # panchayath = request.POST["mphone"]
        # ward_no = request.POST["mphone"]
        user=Mothers.objects.filter(name=mname,con=mphone).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            try:
                u=CustomUser.objects.create_user(username=mname,password=mphone,usertype="mother")
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                try:
                    s=Mothers.objects.create(wid=w,name=mname,age=mage,district=w.district,panchayat=w.panchayat,add=maddress,con=mphone,user=u)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Registered successfully")    
    return render(request, 'Add_mother.html', {'dates': dates})


def viewmother(request):
    data=Mothers.objects.all()
    return render(request, 'view_mother.html', {"data": data})


def alertlink(request):
    return render(request, 'alert_link.html')


# def addvaccination(request):
#     if request.POST:
#         ashaworker_id = request.session['userid']
#         get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#             str(ashaworker_id)+"'"
#         c.execute(get_panchayah)
#         wrkr_details = c.fetchone()

#         vacname = request.POST.get("vacname")
#         vdetails = request.POST.get("vdetails")
#         vactime = request.POST.get("vactime")
#         vacdate = request.POST.get("vacdate")
#         vacloc = request.POST.get("vacloc")
#         posteddat = date.today()

#         vacc_exists = "select count(*) from vaccination where wrkr_id='"+str(ashaworker_id)+"' and vac_name='"+str(
#             vacname)+"' and time='"+str(vactime)+"' and posted_date='"+str(posteddat)+"' and vaccination_date='"+str(vacdate)+"' "
#         print("-------"+vacc_exists+"-------")
#         c.execute(vacc_exists)
#         exisist_data = c.fetchone()
#         # try:
#         if exisist_data[0] > 0:
#             message = "Such details already exisist"
#             return render(request, "Add_vaccination.html", {"message": message})
#         else:
#             vac_insert = "insert into vaccination(`wrkr_id`,`vac_name`,`details`,`time`,`posted_date`,`vaccination_date`,`location`,`status`)values('"+str(
#                 ashaworker_id)+"','"+str(vacname)+"','"+str(vdetails)+"','"+str(vactime)+"','"+str(posteddat)+"','"+str(vacdate)+"','"+str(vacloc)+"','1')"
#             c.execute(vac_insert)
#             conn.commit()
#             msg = "The ashaworker added something new vaccination details please check it on, don't be late posted on " + \
#                 str(posteddat)
#             vacc_sms = "select phone_number from mother_reg where wrker_id='" + \
#                 str(ashaworker_id)+"'"
#             c.execute(vacc_sms)
#             phone_data = c.fetchall()
#            # for p in phone_data:
#             #sendsms(p[0], msg)

#             message = "Added Successfully"
#             return render(request, "Add_vaccination.html", {"message": message})
#         # except:
#         #     message="Such details already exisist"
#         #     return render(request,"Add_mother.html",{"message":message})
#     return render(request, 'Add_vaccination.html')


# def viewvaccination(request):
#     ashaworker_id = request.session['userid']
#     get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(get_panchayah)
#     wrkr_details = c.fetchone()

#     view_pan = "select * from vaccination where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(view_pan)
#     view_data = c.fetchall()
#     return render(request, 'view_vaccination_worker.html', {"data": view_data})


# def addfood(request):
#     if request.POST:
#         ashaworker_id = request.session['userid']
#         get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#             str(ashaworker_id)+"'"
#         c.execute(get_panchayah)
#         wrkr_details = c.fetchone()

#         ftitle = request.POST.get("ftitle")
#         fdetails = request.POST.get("fdetails")
#         posted_date = date.today()

#         food_exists = "select count(*) from food where wrkr_id='"+str(ashaworker_id)+"' and title='"+str(
#             ftitle)+"' and posted_date='"+str(posted_date)+"' and status='1' "
#         print("-------"+food_exists+"-------")
#         c.execute(food_exists)
#         exisist_data = c.fetchone()
#         # try:
#         if exisist_data[0] > 0:
#             message = "Such details already exisist"
#             return render(request, "Add_food.html", {"message": message})
#         else:
#             food_insert = "insert into food(`wrkr_id`,`title`,`details`,`posted_date`,`status`)values('"+str(
#                 ashaworker_id)+"','"+str(ftitle)+"','"+str(fdetails)+"','"+str(posted_date)+"','1')"
#             c.execute(food_insert)
#             conn.commit()
#             msg = "The ashaworker added something new food details please check it on, don't be late posted on " + \
#                 str(posted_date)
#             food_sms = "select phone_number from mother_reg where wrker_id='" + \
#                 str(ashaworker_id)+"'"
#             c.execute(food_sms)
#             phone_data = c.fetchall()
#             # for p in phone_data:
#             # sendsms(p[0], msg)

#             message = "Added Successfully"
#             return render(request, "Add_food.html", {"message": message})
#         # except:
#         #     message="Such details already exisist"
#         #     return render(request,"Add_mother.html",{"message":message})
#     return render(request, 'Add_food.html')


# def viewfood(request):
#     ashaworker_id = request.session['userid']
#     get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(get_panchayah)
#     wrkr_details = c.fetchone()

#     view_food = "select * from food where wrkr_id='"+str(ashaworker_id)+"'"
#     c.execute(view_food)
#     view_data = c.fetchall()
#     return render(request, 'viewfood.html', {"data": view_data})


# def healthlink(request):
#     return render(request, 'health_link.html')


# def addhealthtips(request):
#     if request.POST:
#         ashaworker_id = request.session['userid']
#         get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#             str(ashaworker_id)+"'"
#         c.execute(get_panchayah)
#         wrkr_details = c.fetchone()

#         agegrp = request.POST.get("agegrp")
#         tips = request.POST.get("tips")
#         posted_date = date.today()

#         tips_exists = "select count(*) from health_tips where wrkr_id='"+str(ashaworker_id)+"' and age_grp='"+str(
#             agegrp)+"' and posted_date='"+str(posted_date)+"' and tips='"+str(tips)+"' and status='1' "
#         print("-------"+tips_exists+"-------")
#         c.execute(tips_exists)
#         exisist_data = c.fetchone()
#         # try:
#         if exisist_data[0] > 0:
#             message = "Such details already exisist"
#             return render(request, "Add_healhtips.html", {"message": message})
#         else:
#             tips_insert = "insert into health_tips(`wrkr_id`,`age_grp`,`tips`,`posted_date`,`status`)values('"+str(
#                 ashaworker_id)+"','"+str(agegrp)+"','"+str(tips)+"','"+str(posted_date)+"','1')"
#             c.execute(tips_insert)
#             conn.commit()
#             msg = "The ashaworker added something new health tips details please check it on, don't be late posted on " + \
#                 str(posted_date)
#             tips_sms = "select phone_number from mother_reg where wrker_id='" + \
#                 str(ashaworker_id)+"'"
#             c.execute(tips_sms)
#             phone_data = c.fetchall()
#             # for p in phone_data:
#             # sendsms(p[0], msg)

#             message = "Added Successfully"
#             return render(request, "Add_healhtips.html", {"message": message})
#         # except:
#         #     message="Such details already exisist"
#         #     return render(request,"Add_mother.html",{"message":message})
#     return render(request, 'Add_healhtips.html')


# def viewhealthtips(request):
#     ashaworker_id = request.session['userid']
#     get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(get_panchayah)
#     wrkr_details = c.fetchone()

#     view_tips = "select * from health_tips where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(view_tips)
#     view_data = c.fetchall()
#     return render(request, 'view_healthtips.html', {"data": view_data})


# def adddisease(request):
#     ashaworker_id = request.session['userid']
#     get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(get_panchayah)
#     wrkr_details = c.fetchone()

#     get_doctor = "select doctor_id,dname from doctor where district='" + \
#         str(wrkr_details[0])+"' and panchayath='"+str(wrkr_details[1])+"' "
#     c.execute(get_doctor)
#     doctror_details = c.fetchall()

#     if request.POST:

#         doctor = request.POST.get("doctorlist")
#         details = request.POST.get("ddetails")
#         posted_date = date.today()

#         disease_exists = "select count(*) from disease where wrkr_id='"+str(ashaworker_id)+"' and doc_id='"+str(
#             doctor)+"' and posted_date='"+str(posted_date)+"' and details='"+str(details)+"' "
#         print("-------"+disease_exists+"-------")
#         c.execute(disease_exists)
#         exisist_data = c.fetchone()
#         # try:
#         if exisist_data[0] > 0:
#             message = "Such details already exisist"
#             return render(request, "Add_Disease.html", {"message": message})
#         else:
#             disease_insert = "insert into disease(`wrkr_id`,`doc_id`,`details`,`posted_date`)values('"+str(
#                 ashaworker_id)+"','"+str(doctor)+"','"+str(details)+"','"+str(posted_date)+"')"
#             c.execute(disease_insert)
#             conn.commit()
#             msg = "The ashaworker added something new about disease details please check it on, don't be late posted on " + \
#                 str(posted_date)
#             disease_sms = "select phone_number from mother_reg where wrker_id='" + \
#                 str(ashaworker_id)+"'"
#             c.execute(disease_sms)
#             phone_data = c.fetchall()
#             # for p in phone_data:
#             # sendsms(p[0], msg)

#             message = "Added Successfully"
#             return render(request, "Add_Disease.html", {"message": message})
#         # except:
#         #     message="Such details already exisist"
#         #     return render(request,"Add_mother.html",{"message":message})

#     return render(request, 'Add_Disease.html', {"doctors": doctror_details})


# def viewdisease(request):
#     ashaworker_id = request.session['userid']
#     get_panchayah = "select district,panchayath,ward_no from worker_reg where wrkr_id='" + \
#         str(ashaworker_id)+"'"
#     c.execute(get_panchayah)
#     wrkr_details = c.fetchone()

#     view_disease = "select d.disease_id,d.details,doc.dname,doc.qualification,doc.address,doc.phone_no,doc.optime from disease d,doctor doc where d.wrkr_id='" + \
#         str(ashaworker_id)+"' and doc.doctor_id=d.doc_id"
#     c.execute(view_disease)
#     view_data = c.fetchall()
#     return render(request, 'view_disease_wrkr.html', {"data": view_data})


# def deletemother(request):
#     mr_id = request.GET.get("mr_id")
#     del_mr = "delete from mother_reg where mother_id='"+str(mr_id)+"'"
#     del_login = "delete from login where userid='" + \
#         str(mr_id)+"' and usertype='mother'"
#     c.execute(del_login)
#     c.execute(del_mr)
#     return HttpResponseRedirect("/viewmother")


# def delete_vacc(request):
#     vac_id = request.GET.get("vac_id")
#     del_mr = "delete from vaccination where vac_id='"+str(vac_id)+"'"
#     c.execute(del_mr)
#     return HttpResponseRedirect("/viewvaccination")


# def delete_food(request):
#     f_id = request.GET.get("f_id")
#     del_mr = "delete from food where food_id='"+str(f_id)+"'"
#     c.execute(del_mr)
#     return HttpResponseRedirect("/viewfood")


# def delete_tips(request):
#     t_id = request.GET.get("t_id")
#     del_mr = "delete from health_tips where tipid='"+str(t_id)+"'"
#     c.execute(del_mr)
#     return HttpResponseRedirect("/viewhealthtips")


# def delete_disease(request):
#     dis_id = request.GET.get("dis_id")
#     del_mr = "delete from disease where disease_id='"+str(dis_id)+"'"
#     c.execute(del_mr)
#     return HttpResponseRedirect("/viewdisease")
