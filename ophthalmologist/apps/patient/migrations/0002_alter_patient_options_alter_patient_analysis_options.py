# Generated by Django 4.0.3 on 2022-06-04 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Пацієнт', 'verbose_name_plural': 'Пацієнти'},
        ),
        migrations.AlterModelOptions(
            name='patient_analysis',
            options={'verbose_name': 'Лечение пацієнта', 'verbose_name_plural': 'Лечение пацієнтов'},
        ),
    ]