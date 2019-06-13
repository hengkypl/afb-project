# Generated by Django 2.2 on 2019-06-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kendaraanlain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('keterangan', models.CharField(blank=True, max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Kendaraan / Peralatan lainnya',
                'verbose_name_plural': 'Kendaraan / Peralatan lainnya',
                'ordering': ['nama'],
            },
        ),
    ]