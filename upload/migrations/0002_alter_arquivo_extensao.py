# Generated by Django 4.0.2 on 2022-02-08 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='extensao',
            field=models.TextField(max_length=10),
        ),
    ]