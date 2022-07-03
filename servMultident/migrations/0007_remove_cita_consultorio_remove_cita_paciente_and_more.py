# Generated by Django 4.0.5 on 2022-06-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servMultident', '0006_alter_personal_cat_per_alter_personal_especialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='consultorio',
        ),
        migrations.RemoveField(
            model_name='cita',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='cita',
            name='personal',
        ),
        migrations.AddField(
            model_name='cita',
            name='apellido_c',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cita',
            name='correo',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cita',
            name='nombre_c',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
