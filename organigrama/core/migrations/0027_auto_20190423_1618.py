# Generated by Django 2.2 on 2019-04-23 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20190423_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='organismo',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funcionarios', to='core.Organismo'),
        ),
    ]
