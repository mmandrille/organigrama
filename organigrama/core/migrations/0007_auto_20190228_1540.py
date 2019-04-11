# Generated by Django 2.1.3 on 2019-02-28 18:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190226_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='funcion_unica',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.IntegerField(choices=[(0, 'Gobernador'), (1, 'Vice Gobernador'), (10, 'Ministro'), (20, 'Secretario'), (21, 'Secretaria'), (22, 'Subsecretario'), (23, 'SubScretaria'), (31, 'Director'), (32, 'Directora'), (33, 'SubDirector'), (34, 'SubDirectora'), (41, 'Coordinador'), (42, 'Coordinadora'), (51, 'Consejal'), (52, 'Diputado'), (53, 'Senador'), (61, 'Juez'), (62, 'Fiscal'), (63, 'Vocal'), (71, 'Intendente'), (72, 'Comisionado'), (81, 'Escribano'), (82, 'Presidente'), (83, 'Vice Presidente'), (91, 'Administrativo'), (92, 'Jefe'), (93, 'Obispo'), (94, 'Sacerdote'), (95, 'Consul'), (96, 'Asesor')], default=99),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='endda',
            field=models.DateField(default=datetime.date(9999, 12, 31), verbose_name='Cese de Funciones'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='organismo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='core.Organismo'),
        ),
    ]
