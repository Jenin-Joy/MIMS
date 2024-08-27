from django.db import models
from Admin.models import tbl_department,tbl_designation,tbl_place,tbl_admin,tbl_worktype
import json

# Create your models here.

class tbl_officer(models.Model):
    officer_name = models.CharField(max_length=30)
    officer_contact = models.CharField(max_length=30)
    officer_email = models.EmailField(max_length=30)
    officer_address = models.CharField(max_length=30)
    officer_dob = models.DateField()
    officer_photo = models.FileField(upload_to='Assets/Officer/Photo/')
    officer_proof = models.FileField(upload_to='Assets/Officer/Proof/')
    officer_gender = models.CharField(max_length=5)
    officer_status = models.IntegerField(default=0)
    officer_password = models.CharField(max_length=30)
    department = models.ForeignKey(tbl_department, on_delete=models.CASCADE)
    designation = models.ForeignKey(tbl_designation, on_delete=models.CASCADE)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)

class tbl_keys(models.Model):
    key_name = models.TextField()
    admin = models.ForeignKey(tbl_admin, on_delete=models.CASCADE)
    officer = models.ForeignKey(tbl_officer, on_delete=models.CASCADE)

class tbl_chat(models.Model):
    chat_content = models.BinaryField(max_length=10000)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='Assets/ChatFiles/')
    admin_from = models.ForeignKey(tbl_admin,on_delete=models.CASCADE,related_name="admin_from", null=True)
    admin_to = models.ForeignKey(tbl_admin,on_delete=models.CASCADE,related_name="admin_to", null=True)
    officer_from = models.ForeignKey(tbl_officer,on_delete=models.CASCADE,related_name="officer_from", null=True)
    officer_to = models.ForeignKey(tbl_officer,on_delete=models.CASCADE,related_name="officer_to", null=True)

class tbl_assign(models.Model):
    assign_description = models.CharField(max_length=100)
    officer = models.ForeignKey(tbl_officer, on_delete=models.CASCADE)
    worktype = models.ForeignKey(tbl_worktype, on_delete=models.CASCADE)
    assign_date = models.DateField(auto_now_add=True)
    assign_status = models.IntegerField(default=0)
    StartDate = models.DateTimeField(null=True)
    EndDate = models.DateTimeField(null=True)