# Generated by Django 2.2 on 2019-05-27 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0002_auto_20190527_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hasilore',
            name='keterangan',
        ),
    ]
