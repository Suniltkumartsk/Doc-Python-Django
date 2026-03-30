from django.db import models


class Userdata(models.Model):
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=255)  # will store hashed password

    def __str__(self):
        return self.email


class Doctorinfo(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_image = models.ImageField(upload_to='doctor/')
    specialist = models.CharField(max_length=100)

    def __str__(self):
        return self.doctor_name


class Registerinfo(models.Model):
    user = models.ForeignKey(Userdata, on_delete=models.SET_NULL, null=True, blank=True)
    doc_name = models.CharField(max_length=100)
    p_name = models.CharField(max_length=100)
    p_age = models.IntegerField()
    p_date = models.DateTimeField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)   # CharField to preserve leading zeros
    problem = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.p_name} -> Dr. {self.doc_name}"
