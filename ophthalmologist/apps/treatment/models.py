from django.db import models
from patient.models import Patient_analysis
from analysis.models import Print


class AssignTreat(models.Model):
    class Meta:
        verbose_name = u'Тип лікування'
        verbose_name_plural = u'Тип лікування'

    def __str__(self):
        return f'#{self.id} {self.name}'

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=1000)


class Diagnosis(models.Model):
    class Meta:
        verbose_name = u'Діагноз'
        verbose_name_plural = u'Діагноз'

    def __str__(self):
        return f'#{self.id} {self.name}'

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=1000)


class Treatment(models.Model):
    class Meta:
        verbose_name = u'Лікування'
        verbose_name_plural = u'Лікування'

    def __str__(self):
        return f'#{self.id} {self.patient_analysis.patient.fio()}'

    patient_analysis = models.ForeignKey(Patient_analysis, on_delete=models.CASCADE, null=True)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, null=True)
    appointment_procedures = models.IntegerField(null=True)
    procedures_perform = models.IntegerField(null=True)
    assign_treat = models.ForeignKey(AssignTreat, on_delete=models.CASCADE, null=True)
    print = models.ForeignKey(Print, on_delete=models.CASCADE, null=True)
