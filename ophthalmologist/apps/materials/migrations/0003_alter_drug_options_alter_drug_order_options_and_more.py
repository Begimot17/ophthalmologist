# Generated by Django 4.0.3 on 2022-05-29 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_drug_remove_place_number_of_deliveries_drug_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drug',
            options={'verbose_name': 'Ліки', 'verbose_name_plural': 'Ліки'},
        ),
        migrations.AlterModelOptions(
            name='drug_order',
            options={'verbose_name': 'Замовлення ліків', 'verbose_name_plural': 'Замовлення ліків'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Матеріали', 'verbose_name_plural': 'Матеріали'},
        ),
        migrations.AlterField(
            model_name='drug',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Назва ліків'),
        ),
        migrations.AlterField(
            model_name='drug',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Тип ліків'),
        ),
        migrations.AlterField(
            model_name='drug_order',
            name='drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.drug', verbose_name='Ліки'),
        ),
        migrations.AlterField(
            model_name='drug_order',
            name='quantity',
            field=models.IntegerField(verbose_name='Кол-во'),
        ),
        migrations.AlterField(
            model_name='place',
            name='date_of_delivery',
            field=models.DateField(blank=True, null=True, verbose_name='Дата постачання'),
        ),
        migrations.AlterField(
            model_name='place',
            name='drugs',
            field=models.ManyToManyField(to='materials.drug_order', verbose_name='Назви препаратів'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Назва матеріалу'),
        ),
        migrations.AlterField(
            model_name='place',
            name='open',
            field=models.IntegerField(verbose_name='Відкрито'),
        ),
        migrations.AlterField(
            model_name='place',
            name='remainder',
            field=models.IntegerField(verbose_name='Залишок'),
        ),
        migrations.AlterField(
            model_name='place',
            name='total',
            field=models.IntegerField(verbose_name='Загальна кількість'),
        ),
    ]