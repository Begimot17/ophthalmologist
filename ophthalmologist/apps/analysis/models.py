from django.db import models

class Print(models.Model):
    class Meta:
        verbose_name = u'Печать'
        verbose_name_plural = u'Печати'
    visus_no_cor=models.CharField(max_length=100)
    sph = models.IntegerField()
    cyt = models.IntegerField()
    ax = models.IntegerField()
    visus_in_cor = models.CharField(max_length=100)
    bot = models.CharField(max_length=100)
    eyelids = models.CharField(max_length=100)
    eye_pos = models.CharField(max_length=100)
    conjunctival = models.CharField(max_length=100)
    p_camera = models.CharField(max_length=100)
    pupil = models.CharField(max_length=100)
    iris = models.CharField(max_length=100)
    crystalline_glass = models.CharField(max_length=100)
    dzn = models.CharField(max_length=100)
    vessels = models.CharField(max_length=100)
    maculah = models.CharField(max_length=100)
    diagnose = models.CharField(max_length=100)
    recommend = models.CharField(max_length=100)




