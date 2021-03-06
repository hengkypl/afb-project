# Generated by Django 2.2 on 2019-05-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alatberat', '0015_bbmab_hasilore'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bbmab',
            options={'ordering': ['-tanggal'], 'verbose_name': 'Input Pengisian BBM', 'verbose_name_plural': 'Input Pengisian BBM'},
        ),
        migrations.AlterModelOptions(
            name='biayaab',
            options={'ordering': ['-tanggal'], 'verbose_name': 'Biaya', 'verbose_name_plural': 'Biaya'},
        ),
        migrations.AlterModelOptions(
            name='hasilore',
            options={'ordering': ['-tanggal'], 'verbose_name': 'Hasil Ore', 'verbose_name_plural': 'Hasil Ore'},
        ),
        migrations.AlterModelOptions(
            name='hourmeter',
            options={'ordering': ['-tanggal'], 'verbose_name': 'Hour Meter', 'verbose_name_plural': 'Hour Meter'},
        ),
        migrations.AddField(
            model_name='hasilore',
            name='keterangan',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='alatberat',
            name='keterangan',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='bbmab',
            name='keterangan',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='biayaab',
            name='keterangan',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='hourmeter',
            name='keterangan',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='operatorab',
            name='catatan',
            field=models.TextField(default=None),
        ),
    ]
