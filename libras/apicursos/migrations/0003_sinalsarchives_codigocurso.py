# Generated by Django 5.0.1 on 2024-02-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicursos', '0002_sinalsarchives_codigosinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinalsarchives',
            name='codigocurso',
            field=models.IntegerField(default=404),
        ),
    ]
