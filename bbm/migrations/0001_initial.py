# Generated by Django 2.2 on 2019-05-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiltangki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=20)),
            ],
            options={
                'verbose_name': 'Mobil Tangki',
                'verbose_name_plural': 'Mobil Tangki',
            },
        ),
        migrations.CreateModel(
            name='Tangkiinduk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=20)),
            ],
            options={
                'verbose_name': 'Tangki Induk',
                'verbose_name_plural': 'Tangki Induk',
            },
        ),
    ]