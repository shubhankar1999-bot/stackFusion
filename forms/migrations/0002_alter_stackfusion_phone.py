# Generated by Django 4.1.7 on 2023-03-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stackfusion',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
