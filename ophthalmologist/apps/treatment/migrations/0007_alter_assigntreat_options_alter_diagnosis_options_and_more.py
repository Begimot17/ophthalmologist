# Generated by Django 4.0.3 on 2022-06-06 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0006_treatment_assign_treat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assigntreat',
            options={'verbose_name': 'Тип лікування', 'verbose_name_plural': 'Тип лікування'},
        ),
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name': 'Діагноз', 'verbose_name_plural': 'Діагноз'},
        ),
        migrations.AlterModelOptions(
            name='treatment',
            options={'verbose_name': 'Лікування', 'verbose_name_plural': 'Лікування'},
        ),
    ]
