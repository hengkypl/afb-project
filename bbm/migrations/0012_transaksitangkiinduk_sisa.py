# Generated by Django 2.0 on 2019-06-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbm', '0011_auto_20190610_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksitangkiinduk',
            name='sisa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
