from django.db import models
# Create your models here.

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_email = models.EmailField(max_length=30)
    admin_password = models.CharField(max_length=30)

class tbl_department(models.Model):
    department_name = models.CharField(max_length=30)

class tbl_designation(models.Model):
    designation_name = models.CharField(max_length=30)

class tbl_state(models.Model):
    state_name = models.CharField(max_length=30)

class tbl_worktype(models.Model):
    worktype_name = models.CharField(max_length=30)

class tbl_district(models.Model):
    state = models.ForeignKey(tbl_state, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=50)

class tbl_place(models.Model):
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50)