from django.db import models
from patient.models import Patient_analysis
from analysis.models import Print


class Treatment(models.Model):
    patient_analysis=models.ForeignKey(Patient_analysis, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=100)
    appointment_procedures = models.IntegerField()
    procedures_perform = models.IntegerField()
    print = models.ForeignKey(Print, on_delete=models.CASCADE, null=True)