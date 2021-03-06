# Generated by Django 4.0.3 on 2022-06-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_alter_print_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='ax',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='bot',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='conjunctival',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='crystalline_glass',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='cyt',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='diagnose',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='dzn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='eye_pos',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='eyelids',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='iris',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='maculah',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='p_camera',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='pupil',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='recommend',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='sph',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='vessels',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='visus_in_cor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='visus_no_cor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
