# Generated by Django 4.0.3 on 2022-05-29 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=100)),
                ('appointment_procedures', models.CharField(max_length=100)),
                ('procedures_perform', models.CharField(max_length=100)),
                ('patient_analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient_analysis')),
            ],
        ),
    ]
