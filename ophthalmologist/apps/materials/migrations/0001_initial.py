# Generated by Django 4.0.3 on 2022-05-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
                ('remainder', models.IntegerField()),
                ('open', models.IntegerField()),
                ('date_of_delivery', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('number_of_deliveries', models.IntegerField()),
            ],
        ),
    ]
