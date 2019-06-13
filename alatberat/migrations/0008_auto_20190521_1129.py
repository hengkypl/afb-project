# Generated by Django 2.2 on 2019-05-21 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alatberat', '0007_hourmeter_keterangan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operatorab',
            old_name='gajipokok',
            new_name='basicsalary',
        ),
        migrations.RenameField(
            model_name='operatorab',
            old_name='transport',
            new_name='mingguraya',
        ),
        migrations.RenameField(
            model_name='operatorab',
            old_name='tunjangan',
            new_name='uanghadir',
        ),
        migrations.RemoveField(
            model_name='operatorab',
            name='email',
        ),
        migrations.AddField(
            model_name='alatberat',
            name='hargahm',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='alatberat',
            name='hargaot',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='alatberat',
            name='jenissewa',
            field=models.CharField(choices=[('PAGI', 'PAGI'), ('SIANG', 'SIANG'), ('MALAM', 'MALAM')], max_length=5),
        ),
        migrations.AlterField(
            model_name='hourmeter',
            name='shift',
            field=models.CharField(choices=[('PAGI', 'PAGI'), ('SIANG', 'SIANG'), ('MALAM', 'MALAM')], max_length=5),
        ),
    ]