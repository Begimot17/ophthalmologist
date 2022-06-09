from django.db import models
from treatment.models import Treatment

class Survey(models.Model):
    class Meta:
        verbose_name = u'Вид обстеження	'
        verbose_name_plural = u'Вид обстеження	'

    def __str__(self):
        return f'#{self.id} {self.name}'
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=1000)

class Reception(models.Model):
    class Meta:
        verbose_name = u'Рецепт'
        verbose_name_plural = u'Рецепти'
    def __str__(self):
        return f'#{self.id} {self.complains}'
    complains = models.CharField(max_length=100, verbose_name = u'Жалоби')
    survey_type = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name = u'Тип опроса')
    scheduled = models.CharField(max_length=100, verbose_name = u'Назва ліків')
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, verbose_name = u'Назва ліків')


class Inspection(models.Model):
    class Meta:
        verbose_name = u'Рецепт повний'
        verbose_name_plural = u'Рецепти повні'
    def __str__(self):
        return f'#{self.id} {self.survey}'
    survey = models.CharField(max_length=100, verbose_name = u'Обследование')
    includes = models.CharField(max_length=100, verbose_name = u'Включения')
    date_of_receipt= models.DateField(null=True, blank=True)
    time_of_receipt = models.CharField(max_length=100,null=True, blank=True)
    reception = models.ForeignKey(Reception, on_delete=models.CASCADE, verbose_name = u'Прийом')
