# Generated by Django 2.1.7 on 2019-04-24 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=15, verbose_name='Calve del Grupo')),
                ('cantAlumnos', models.PositiveIntegerField()),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profesores.Profesores')),
            ],
        ),
    ]