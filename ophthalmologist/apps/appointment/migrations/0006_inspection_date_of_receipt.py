# Generated by Django 4.0.3 on 2022-06-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_inspection_includes_alter_inspection_reception_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='date_of_receipt',
            field=models.DateField(blank=True, null=True),
        ),
    ]
