# Generated by Django 5.0.1 on 2024-02-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinalsarchives',
            name='codigosinal',
            field=models.IntegerField(default=404),
        ),
    ]
