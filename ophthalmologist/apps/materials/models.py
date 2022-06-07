from django.db import models


class Drug(models.Model):
    class Meta:
        verbose_name = u'Ліки'
        verbose_name_plural = u'Ліки'
    def __str__(self):
        return f'#{self.name}'
    name = models.CharField(max_length=100, verbose_name = u'Назва ліків')
    type = models.CharField(max_length=100, verbose_name = u'Тип ліків')


class Drug_Order(models.Model):
    class Meta:
        verbose_name = u'Замовлення ліків'
        verbose_name_plural = u'Замовлення ліків'
    def __str__(self):
        return f'#{self.id} {self.drug.name}: {self.quantity}шт'
    quantity = models.IntegerField(verbose_name = u'Кол-во')
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, verbose_name = u'Ліки')


class Place(models.Model):
    class Meta:
        verbose_name = u'Матеріали'
        verbose_name_plural = u'Матеріали'
    def __str__(self):
        return f'#{self.id} {self.name}'
    name = models.CharField(max_length=100, verbose_name = u'Назва матеріалу')
    total = models.IntegerField(verbose_name = u'Загальна кількість')
    remainder = models.IntegerField(verbose_name = u'Залишок')
    open = models.IntegerField(verbose_name = u'Відкрито')
    date_of_delivery = models.DateField('Дата постачання', null=True, blank=True)
    drugs = models.ForeignKey(Drug_Order, on_delete=models.CASCADE, verbose_name = u'Назви препаратів')
