from django.db import models
from treatment.models import Treatment


class Reception(models.Model):
    class Meta:
        verbose_name = u'Рецепт'
        verbose_name_plural = u'Рецепти'
    complains = models.CharField(max_length=100)
    survey_type = models.CharField(max_length=100)
    scheduled = models.CharField(max_length=100)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)


class Inspection(models.Model):
    class Meta:
        verbose_name = u'Рецепт повний'
        verbose_name_plural = u'Рецепти повні'
    survey = models.CharField(max_length=100)
    includes = models.CharField(max_length=100)
    reception = models.ForeignKey(Reception, on_delete=models.CASCADE)
