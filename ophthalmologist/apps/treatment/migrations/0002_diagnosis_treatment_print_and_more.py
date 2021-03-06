# Generated by Django 4.0.3 on 2022-06-04 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_alter_print_options'),
        ('treatment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='treatment',
            name='print',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.print'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='appointment_procedures',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='procedures_perform',
            field=models.IntegerField(),
        ),
    ]
