# Generated by Django 4.0.3 on 2022-06-04 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0002_diagnosis_treatment_print_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='diagnosis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='treatment.diagnosis'),
        ),
    ]
