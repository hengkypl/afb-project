# Generated by Django 2.2 on 2019-05-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alatberat', '0010_auto_20190521_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorab',
            name='bpjs',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='operatorab',
            name='basicsalary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='operatorab',
            name='hadirmalam',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='operatorab',
            name='hadirpagi',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='operatorab',
            name='mingguraya',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]