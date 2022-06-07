from django.db import models

class Print(models.Model):
    class Meta:
        verbose_name = u'Печать'
        verbose_name_plural = u'Печати'

    def __str__(self):
        return f'#{self.id}'
    visus_no_cor=models.CharField(max_length=100,null=True)
    sph = models.IntegerField(null=True)
    cyt = models.IntegerField(null=True)
    ax = models.IntegerField(null=True)
    visus_in_cor = models.CharField(max_length=100,null=True)
    bot = models.CharField(max_length=100,null=True)
    eyelids = models.CharField(max_length=100,null=True)
    eye_pos = models.CharField(max_length=100,null=True)
    conjunctival = models.CharField(max_length=100,null=True)
    p_camera = models.CharField(max_length=100,null=True)
    pupil = models.CharField(max_length=100,null=True)
    iris = models.CharField(max_length=100,null=True)
    crystalline_glass = models.CharField(max_length=100,null=True)
    dzn = models.CharField(max_length=100,null=True)
    vessels = models.CharField(max_length=100,null=True)
    maculah = models.CharField(max_length=100,null=True)
    diagnose = models.CharField(max_length=100,null=True)
    recommend = models.CharField(max_length=100,null=True)




