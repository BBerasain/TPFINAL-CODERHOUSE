# Generated by Django 5.0 on 2024-01-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_remove_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('nacionalidad', models.CharField(max_length=40)),
                ('ultimo_equipo', models.CharField(max_length=40)),
                ('nuevo_equipo', models.CharField(max_length=40)),
                ('valor_de_traspaso', models.IntegerField(max_length=40)),
            ],
        ),
    ]