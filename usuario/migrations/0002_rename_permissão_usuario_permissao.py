# Generated by Django 4.0.2 on 2022-02-09 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='permissão',
            new_name='permissao',
        ),
    ]
