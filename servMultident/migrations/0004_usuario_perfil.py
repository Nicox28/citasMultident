# Generated by Django 4.0.5 on 2022-06-08 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servMultident', '0003_rename_cel_pac_personal_cel_per_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
