# Generated by Django 3.0.6 on 2020-06-19 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre de genero')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='nombre pelicula')),
                ('duracion', models.IntegerField()),
                ('fecha', models.DateField()),
                ('Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Genero')),
            ],
        ),
    ]