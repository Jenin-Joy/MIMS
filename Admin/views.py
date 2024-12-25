from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import tbl_officer,tbl_chat,tbl_keys,tbl_assign
from django.db.models import Q
from datetime import datetime
import random
from cryptography.fernet import Fernet
# Create your views here.

def homepage(request):
    if 'aid' in request.session:
        return render(request, 'Admin/homepage.html')
    else:
        return redirect("Guest:login")

def logout(request):
    del request.session["aid"]
    return redirect("Guest:login")

def adminreg(request):
    if 'aid' in request.session:
        admin = tbl_admin.objects.all()
        if request.method == "POST":
            tbl_admin.objects.create(admin_name=request.POST.get('txt_name'), admin_email=request.POST.get('txt_email'), admin_password=request.POST.get('txt_password'))
            return render(request,"Admin/Admin_Reg.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Admin_Reg.html",{"admin":admin})
    else:
        return redirect("Guest:login")

def deleteadmin(request,id):
    tbl_admin.objects.get(id=id).delete()
    return render(request,"Admin/Admin_Reg.html",{"msg":"Data Deleted"})

def department(request):
    if 'aid' in request.session:
        department = tbl_department.objects.all()
        if request.method == "POST":
            tbl_department.objects.create(department_name=request.POST.get('txt_name'))
            return render(request,"Admin/Department.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Department.html",{"department":department})
    else:
        return redirect("Guest:login")

def deletedepartment(request,id):
    tbl_department.objects.get(id=id).delete()
    return render(request,"Admin/Department.html",{"msg":"Data Deleted"})

def editdepartment(request,id):
    department = tbl_department.objects.get(id=id)
    if request.method == "POST":
        department.department_name = request.POST.get('txt_name')
        department.save()
        return render(request,"Admin/Department.html",{"msg":"Data Updated"})
    else:
        return render(request,"Admin/Department.html",{"editdepartment":department})

def designation(request):
    if 'aid' in request.session:
        designation = tbl_designation.objects.all()
        if request.method == "POST":
            tbl_designation.objects.create(designation_name=request.POST.get('txt_name'))
            return render(request,"Admin/Designation.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Designation.html",{"designation":designation})
    else:
        return redirect("Guest:login")

def deletedesignation(request,id):
    tbl_designation.objects.get(id=id).delete()
    return render(request,"Admin/Designation.html",{"msg":"Data Deleted"})

def editdesignation(request,id):
    designation = tbl_designation.objects.get(id=id)
    if request.method == "POST":
        designation.designation_name = request.POST.get('txt_name')
        designation.save()
        return render(request,"Admin/Designation.html",{"msg":"Data Updated"})
    else:
        return render(request,"Admin/Designation.html",{"editdesignation":designation})

def state(request):
    if 'aid' in request.session:
        state = tbl_state.objects.all()
        if request.method == "POST":
            tbl_state.objects.create(state_name=request.POST.get('txt_name'))
            return render(request,"Admin/State.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/State.html",{"state":state})
    else:
        return redirect("Guest:login")

def deletestate(request,id):
    tbl_state.objects.get(id=id).delete()
    return render(request,"Admin/State.html",{"msg":"Data Deleted"})

def editstate(request,id):
    state = tbl_state.objects.get(id=id)
    if request.method == "POST":
        state.state_name = request.POST.get('txt_name')
        state.save()
        return render(request,"Admin/State.html",{"msg":"Data Updated"})
    else:
        return render(request,"Admin/State.html",{"editstate":state})

def worktype(request):
    if 'aid' in request.session:
        worktype = tbl_worktype.objects.all()
        if request.method == "POST":
            tbl_worktype.objects.create(worktype_name=request.POST.get('txt_name'))
            return render(request,"Admin/Work_Type.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Work_Type.html",{"worktype":worktype})
    else:
        return redirect("Guest:login")

def deleteworktype(request,id):
    tbl_worktype.objects.get(id=id).delete()
    return render(request,"Admin/Work_Type.html",{"msg":"Data Deleted"})

def editworktype(request,id):
    worktype = tbl_worktype.objects.get(id=id)
    if request.method == "POST":
        worktype.worktype_name = request.POST.get('txt_name')
        worktype.save()
        return render(request,"Admin/Work_Type.html",{"msg":"Data Updated"})
    else:
        return render(request,"Admin/Work_Type.html",{"editworktype":worktype})

def district(request):
    if 'aid' in request.session:
        state = tbl_state.objects.all()
        district = tbl_district.objects.all()
        if request.method == "POST":
            tbl_district.objects.create(district_name=request.POST.get('txt_name'), state=tbl_state.objects.get(id=request.POST.get('sel_state')))
            return render(request,"Admin/District.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/District.html",{"district":district,"state":state})
    else:
        return redirect("Guest:login")

def deletedistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return render(request,"Admin/District.html",{"msg":"Data Deleted"})

def editdistrict(request,id):
    district = tbl_district.objects.get(id=id)
    state = tbl_state.objects.all()
    if request.method == "POST":
        district.district_name = request.POST.get('txt_name')
        district.state = tbl_state.objects.get(id=request.POST.get('sel_state'))
        district.save()
        return render(request,"Admin/District.html",{"msg":"Data Updated"})
    else:
        return render(request,"Admin/District.html",{"editdistrict":district,"state":state})

def place(request):
    if 'aid' in request.session:
        state = tbl_state.objects.all()
        place = tbl_place.objects.all()
        if request.method == "POST":
            tbl_place.objects.create(place_name=request.POST.get('txt_place'), district=tbl_district.objects.get(id=request.POST.get('sel_district')))
            return render(request,"Admin/Place.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Place.html",{"place":place,"state":state})
    else:
        return redirect("Guest:login")

def deleteplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return render(request,"Admin/Place.html",{"msg":"Data Deleted"})

def ajaxdistrict(request):
    district = tbl_district.objects.filter(state=request.GET.get("did"))
    return render(request,"Admin/AjaxDistrict.html",{"district":district})

def newofficer(request):
    if 'aid' in request.session:
        officer = tbl_officer.objects.filter(officer_status=0)
        return render(request,"Admin/New_Officers.html",{"officer":officer})
    else:
        return redirect("Guest:login")

def verifyofficer(request,id,status):
    officer = tbl_officer.objects.get(id=id)
    officer.officer_status = status
    officer.save()
    msg=""
    if status == 1:
        msg = "Officer Approved successfully"
    else:
        msg = "Officer rejected successfully"
    return render(request,"Admin/homepage.html",{"msg":msg})

def approvedofficer(request):
    if 'aid' in request.session:
        officer = tbl_officer.objects.filter(officer_status=1)
        return render(request,"Admin/Approved_Officer.html",{"officer":officer})
    else:
        return redirect("Guest:login")

def rejectedofficer(request):
    if 'aid' in request.session:
        officer = tbl_officer.objects.filter(officer_status=2)
        return render(request,"Admin/Rejected_Officer.html",{"officer":officer})
    else:
        return redirect("Guest:login")

def chatpage(request,id):
    user  = tbl_officer.objects.get(id=id)
    connection = tbl_keys.objects.filter(admin=request.session["aid"],officer=user).count()
    if connection == 0:
        key = Fernet.generate_key()
        tbl_keys.objects.create(key_name=key.decode(),admin=tbl_admin.objects.get(id=request.session["aid"]),officer=tbl_officer.objects.get(id=user.id))
        return render(request,"Admin/Chat.html",{"user":user})
    else:
        return render(request,"Admin/Chat.html",{"user":user})

def ajaxchat(request):
    from_admin = tbl_admin.objects.get(id=request.session["aid"])
    to_officer = tbl_officer.objects.get(id=request.POST.get("tid"))
    key = tbl_keys.objects.get(admin=request.session["aid"],officer=to_officer)
    # print(key.key_name.encode())
    fernet = Fernet(key.key_name.encode())
    # print("fernet" , fernet)
    encryptedtext = fernet.encrypt(request.POST.get("msg").encode())
    # print("encryptedtext" , encryptedtext)
    tbl_chat.objects.create(chat_content=encryptedtext,chat_time=datetime.now(),admin_from=from_admin,officer_to=to_officer,chat_file=request.FILES.get("file"))
    return render(request,"Admin/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    admin = tbl_admin.objects.get(id=request.session["aid"])
    key = tbl_keys.objects.get(admin=request.session["aid"],officer=tid)
    fernet = Fernet(key.key_name.encode())
    chat_data = tbl_chat.objects.filter((Q(admin_from=admin) | Q(admin_to=admin)) & (Q(officer_from=tid) | Q(officer_to=tid))).order_by('chat_time')
    for i in chat_data:
        # print(i.chat_content)   
        decryptedtext = fernet.decrypt(i.chat_content).decode()
        # print(decryptedtext)
        i.chat_content = decryptedtext
    return render(request,"Admin/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(admin_from=request.session["aid"]) & Q(officer_to=request.GET.get("tid")) | (Q(officer_from=request.GET.get("tid")) & Q(admin_to=request.session["aid"]))).delete()
    return render(request,"Admin/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def assignwork(request, id):
    worktype = tbl_worktype.objects.all()
    assign = tbl_assign.objects.all()
    if request.method == "POST":
        tbl_assign.objects.create(worktype = tbl_worktype.objects.get(id=request.POST.get("sel_worktype")), officer=tbl_officer.objects.get(id=id), assign_description=request.POST.get("txt_description"))
        return render(request,"Admin/Approved_Officer.html",{"msg":"Work Assigned Successfully"})
    else:
        return render(request,"Admin/Assign_Work.html",{"worktype":worktype,"assign":assign})

def deleteassignwork(request,id):
    tbl_assign.objects.get(id=id).delete()
    return render(request,"Admin/Assign_Work.html",{"msg":"Data Deleted"})