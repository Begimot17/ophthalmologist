# Generated by Django 4.0.3 on 2022-06-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0004_alter_diagnosis_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignTreat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=1000)),
            ],
        ),
    ]
