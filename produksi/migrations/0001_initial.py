# Generated by Django 2.2 on 2019-05-27 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hasilore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(db_index=True, default=datetime.datetime.now)),
                ('hasilore', models.DecimalField(decimal_places=2, max_digits=15)),
                ('keterangan', models.CharField(blank=True, default=None, max_length=50)),
            ],
            options={
                'verbose_name': 'Hasil Ore',
                'verbose_name_plural': 'Hasil Ore',
                'ordering': ['-tanggal'],
            },
        ),
    ]
