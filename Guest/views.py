from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def officer(request):
    designation = tbl_designation.objects.all()
    department = tbl_department.objects.all()
    state = tbl_state.objects.all()
    if request.method == "POST":
        tbl_officer.objects.create(
            officer_name=request.POST.get('txt_name'),
            officer_contact=request.POST.get('txt_contact'),
            officer_email=request.POST.get('txt_email'),
            officer_address=request.POST.get('txt_address'),
            officer_dob=request.POST.get('txt_dob'),
            officer_photo=request.FILES.get('txt_photo'),
            officer_proof=request.FILES.get('txt_proof'),
            officer_gender=request.POST.get('txt_gender'),
            officer_password=request.POST.get('txt_password'),
            department=tbl_department.objects.get(id=request.POST.get('sel_department')),
            designation=tbl_designation.objects.get(id=request.POST.get('sel_designation')),
            place=tbl_place.objects.get(id=request.POST.get('sel_place')),
        )
        return render(request, 'Guest/Officer.html', {"msg":"Registred Successfully"})
    else:
        return render(request, 'Guest/Officer.html',{"designation":designation, "state":state, "department":department})

def ajaxplace(request): 
    place = tbl_place.objects.filter(district=request.GET.get('did'))
    return render(request, 'Guest/AjaxPlace.html', {'place': place})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('txt_email')
        password = request.POST.get('txt_password')
        officercount = tbl_officer.objects.filter(officer_email=email, officer_password=password).count()
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        if officercount > 0:
            officer = tbl_officer.objects.get(officer_email=email, officer_password=password)
            if officer.officer_status == 0:
                return render(request, 'Guest/Login.html', {'msg':'Aoocunt Verifcation is pending'})
            elif officer.officer_status == 2:
                return render(request, 'Guest/Login.html', {'msg':'Account is Suspended'})
            else:
                request.session["ofid"] = officer.id
                return redirect("Officer:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email, admin_password=password)
            request.session["aid"] = admin.id
            return redirect("Admin:homepage")
        else:
            return render(request, 'Guest/Login.html', {'msg':'Invalid Email or Password'})
    else:
        return render(request, 'Guest/Login.html')