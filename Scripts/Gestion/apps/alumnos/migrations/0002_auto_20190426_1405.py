# Generated by Django 2.1.7 on 2019-04-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]