# Generated by Django 2.1.3 on 2019-04-03 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190403_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='begda',
            field=models.DateField(default=datetime.date(2019, 1, 1), verbose_name='Designacion'),
        ),
    ]