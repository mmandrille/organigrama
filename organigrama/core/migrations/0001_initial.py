# Generated by Django 2.0.5 on 2018-05-15 13:12

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.IntegerField(choices=[(0, 'Gobernador'), (10, 'Secretario'), (11, 'Secretaria'), (12, 'Subsecretario'), (13, 'SubScretaria'), (21, 'Director'), (22, 'Directora'), (31, 'Coordinador'), (32, 'Coordinadora'), (99, 'Administrativo')], default=99)),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=100, verbose_name='DNI')),
                ('titulo', models.CharField(max_length=20, verbose_name='Titulo Profesional')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Personal')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Titulo')),
                ('descripcion', tinymce.models.HTMLField()),
                ('icono', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='archivos/'), upload_to='')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
                ('cuit', models.CharField(blank=True, max_length=13, null=True, verbose_name='CUIT')),
                ('telefonos', models.CharField(max_length=100, verbose_name='Telefonos')),
                ('web', models.URLField(verbose_name='Web')),
                ('activo', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
                ('padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos', to='core.Organismo')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='organismo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Organismo'),
        ),
    ]