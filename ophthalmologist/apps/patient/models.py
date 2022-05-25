from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    date_of_birth= models.DateField()
    phone= models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE)


class Patient_analysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_treatment = models.CharField(max_length=100)
    examination_after_treatment = models.CharField(max_length=100)
    new_treatment = models.CharField(max_length=100)