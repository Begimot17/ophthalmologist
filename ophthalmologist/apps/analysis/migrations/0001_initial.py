# Generated by Django 4.0.3 on 2022-05-29 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('treatment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visus_no_cor', models.CharField(max_length=100)),
                ('sph', models.IntegerField()),
                ('cyt', models.IntegerField()),
                ('ax', models.IntegerField()),
                ('visus_in_cor', models.CharField(max_length=100)),
                ('bot', models.CharField(max_length=100)),
                ('eyelids', models.CharField(max_length=100)),
                ('eye_pos', models.CharField(max_length=100)),
                ('conjunctival', models.CharField(max_length=100)),
                ('p_camera', models.CharField(max_length=100)),
                ('pupil', models.CharField(max_length=100)),
                ('iris', models.CharField(max_length=100)),
                ('crystalline_glass', models.CharField(max_length=100)),
                ('dzn', models.CharField(max_length=100)),
                ('vessels', models.CharField(max_length=100)),
                ('maculah', models.CharField(max_length=100)),
                ('diagnose', models.CharField(max_length=100)),
                ('recommend', models.CharField(max_length=100)),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.treatment')),
            ],
        ),
    ]
