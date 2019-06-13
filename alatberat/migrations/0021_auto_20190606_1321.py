# Generated by Django 2.2 on 2019-06-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alatberat', '0020_auto_20190527_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alatberat',
            name='bbmperjam',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Pemakaian BBM Per Jam'),
        ),
        migrations.AlterField(
            model_name='alatberat',
            name='hargahm',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Harga Hour Meter'),
        ),
        migrations.AlterField(
            model_name='alatberat',
            name='hargaot',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Harga Overtime'),
        ),
        migrations.AlterField(
            model_name='alatberat',
            name='hargasewa',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Harga Sewa'),
        ),
        migrations.AlterField(
            model_name='alatberat',
            name='jadwalhmservice',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Jadwal HM Service alat', max_digits=15, verbose_name='Jadwal HM Service berkala kendaraan'),
        ),
        migrations.AlterField(
            model_name='alatberat',
            name='namaalat',
            field=models.CharField(max_length=30, verbose_name='Nama Alat'),
        ),
        migrations.AlterField(
            model_name='bbmab',
            name='hmbefore',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='HM Sebelumnya'),
        ),
        migrations.AlterField(
            model_name='bbmab',
            name='hmnow',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='HM Saat ini'),
        ),
        migrations.AlterField(
            model_name='bbmab',
            name='ltrmasuk',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Liter yg masuk'),
        ),
        migrations.AlterField(
            model_name='hourmeter',
            name='hmawal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='HM Awal'),
        ),
        migrations.AlterField(
            model_name='hourmeter',
            name='hmdunia',
            field=models.DecimalField(decimal_places=0, default=9, max_digits=10, verbose_name='HM Dunia'),
        ),
        migrations.AlterField(
            model_name='hourmeter',
            name='ot',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Overtime'),
        ),
        migrations.AlterField(
            model_name='operatorab',
            name='basicsalary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Basic Salary'),
        ),
        migrations.AlterField(
            model_name='operatorab',
            name='namaoperator',
            field=models.CharField(max_length=30, verbose_name='Nama Operator'),
        ),
    ]