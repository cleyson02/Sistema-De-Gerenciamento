# Generated by Django 4.2.7 on 2023-11-10 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0003_remove_salas_data_devolucao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salas',
            old_name='sala',
            new_name='nome',
        ),
    ]