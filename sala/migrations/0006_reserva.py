# Generated by Django 4.2.7 on 2023-11-10 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0005_salas_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.CharField(max_length=100)),
                ('data_hora_reserva', models.DateTimeField()),
                ('data_hora_devolucao', models.DateTimeField(blank=True, null=True)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala.salas')),
            ],
            options={
                'verbose_name': 'Reserva',
            },
        ),
    ]