from django.db import models

class Userdata(models.Model):
    email=models.CharField(max_length=70)
    password=models.CharField(max_length=70)
    def __str__(self):
        return self.email
    
class Doctorinfo(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_image=models.ImageField(upload_to='doctor/')
    specialist=models.CharField(max_length=100)
    def __str__(self):
        return self.doctor_name
    
class Registerinfo(models.Model):
    doc_name=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    p_age=models.IntegerField()
    p_date=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    contact=models.IntegerField()
    problem=models.CharField(max_length=100)
    def __str__(self):
        return self.doc_name
# Create your models here.
