# Generated by Django 2.0.3 on 2018-05-08 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180508_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organismo',
            name='padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Organismo'),
        ),
    ]