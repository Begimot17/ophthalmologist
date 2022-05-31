from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    class Meta:
        verbose_name = u'Пацієнт'
        verbose_name_plural = u'Пацієнти'
    def fio(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    date_of_birth= models.DateField(null=True, blank=True)
    date_of_receipt = models.DateField(null=True, blank=True)
    phone= models.CharField(max_length=100)
    first_name= models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Patient_analysis(models.Model):
    class Meta:
        verbose_name = u'Лечение пацієнта'
        verbose_name_plural = u'Лечение пацієнтов'
    def __str__(self):
        return f'{self.patient.last_name} {self.patient.first_name} {self.patient.middle_name}'
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_treatment = models.CharField(max_length=100) # назначенное лечение
    examination_after_treatment = models.CharField(max_length=100)# обследование после лечения
    new_treatment = models.CharField(max_length=100)# новое лечение