from django.db import models
from patient.models import Patient_analysis


class Treatment(models.Model):
    patient_analysis=models.ForeignKey(Patient_analysis, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=100)
    appointment_procedures = models.CharField(max_length=100)
    procedures_perform = models.CharField(max_length=100)