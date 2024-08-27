from django.shortcuts import render
from Guest.models import tbl_officer
from Admin.models import *
from Guest.models import tbl_chat,tbl_keys,tbl_assign
from datetime import datetime
from django.db.models import Q
import random
from cryptography.fernet import Fernet
# Create your views here.

def homepage(request):
    return render(request, 'Officer/Homepage.html')

def profile(request):
    officer = tbl_officer.objects.get(id=request.session["ofid"])
    return render(request, 'Officer/Profile.html',{'officer':officer})

def editprofile(request):
    officer = tbl_officer.objects.get(id=request.session["ofid"])
    designation = tbl_designation.objects.all()
    department = tbl_department.objects.all()
    if request.method == "POST":
        officer.officer_name = request.POST.get('txt_name')
        officer.officer_contact = request.POST.get('txt_contact')
        officer.officer_email = request.POST.get('txt_email')
        officer.department = tbl_department.objects.get(id=request.POST.get('sel_department'))
        officer.designation = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        officer.save()
        return render(request, 'Officer/Profile.html',{'msg':'Data Updated'})
    else:
        return render(request, 'Officer/EditProfile.html',{'officer':officer,"designation":designation,'department':department})

def changepassword(request):
    officer = tbl_officer.objects.get(id=request.session["ofid"])
    if request.method == "POST":
        if officer.officer_password == request.POST.get("txt_old_password"):
            if request.POST.get("txt_new_password") == request.POST.get("txt_con_password"):
                officer.officer_password = request.POST.get("txt_new_password")
                officer.save()
                return render(request, 'Officer/Profile.html',{'msg':'Password Changed'})
            else:
                return render(request, 'Officer/ChangePassword.html',{'msg':'Confirm Passwords do not match'})
        else:
            return render(request, 'Officer/ChangePassword.html',{'msg':'Old Password is incorrect'})
    else:
        return render(request, 'Officer/ChangePassword.html')

def viewadmin(request):
    admin = tbl_admin.objects.all()
    return render(request, 'Officer/View_Admin.html',{'admin':admin})

def chatpage(request,id):
    admin  = tbl_admin.objects.get(id=id)
    connection = tbl_keys.objects.filter(admin=admin,officer=request.session["ofid"]).count()
    if connection == 0:
        key = random.randint(111111,999999)
        tbl_keys.objects.create(key_name=key,admin=tbl_admin.objects.get(id=admin.id),officer=tbl_officer.objects.get(id=request.session["ofid"]))
        return render(request,"Admin/Chat.html",{"user":admin})
    else:
        return render(request,"Officer/Chat.html",{"user":admin})

def ajaxchat(request):
    from_officer = tbl_officer.objects.get(id=request.session["ofid"])
    to_admin = tbl_admin.objects.get(id=request.POST.get("tid"))
    key = tbl_keys.objects.get(admin=to_admin,officer=request.session["ofid"])
    # print(key.key_name.encode())
    fernet = Fernet(key.key_name.encode())
    # print("fernet" , fernet)
    encryptedtext = fernet.encrypt(request.POST.get("msg").encode())
    # print("encryptedtext" , encryptedtext)
    tbl_chat.objects.create(chat_content=encryptedtext,chat_time=datetime.now(),officer_from=from_officer,admin_to=to_admin,chat_file=request.FILES.get("file"))
    return render(request,"Officer/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    officer = tbl_officer.objects.get(id=request.session["ofid"])
    key = tbl_keys.objects.get(admin=request.session["aid"],officer=tid)
    fernet = Fernet(key.key_name.encode())
    chat_data = tbl_chat.objects.filter((Q(officer_from=officer) | Q(officer_to=officer)) & (Q(admin_from=tid) | Q(admin_to=tid))).order_by('chat_time')
    for i in chat_data:
        # print(i.chat_content)   
        decryptedtext = fernet.decrypt(i.chat_content).decode()
        # print(decryptedtext)
        i.chat_content = decryptedtext
    return render(request,"Officer/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(officer_from=request.session["ofid"]) & Q(admin_to=request.GET.get("tid")) | (Q(admin_from=request.GET.get("tid")) & Q(officer_to=request.session["ofid"]))).delete()
    return render(request,"Officer/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def viewworks(request):
    assign = tbl_assign.objects.filter(officer=request.session["ofid"])
    return render(request,"Officer/View_Works.html",{"assign":assign})

def updatework(request, id, status):
    assign = tbl_assign.objects.get(id=id)
    msg = ""
    if status == 1:
        msg = "Work Started successfully"
        assign.assign_status = status
        assign.StartDate = datetime.now()
    elif status == 2:
        msg = "Work Completed successfully"
        assign.assign_status = status
        assign.EndDate = datetime.now()
    else:
        msg = "Error"
    assign.save()
    return render(request,"Officer/View_Works.html",{"msg":msg})
    