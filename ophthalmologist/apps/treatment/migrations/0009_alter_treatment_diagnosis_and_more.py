# Generated by Django 4.0.3 on 2022-06-06 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_options_alter_patient_analysis_options'),
        ('treatment', '0008_alter_treatment_appointment_procedures_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='diagnosis',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='treatment.diagnosis'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient_analysis',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient_analysis'),
        ),
    ]
