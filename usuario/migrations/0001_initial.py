# Generated by Django 4.0.2 on 2022-02-09 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=10)),
                ('permissão', models.IntegerField()),
                ('ativado', models.BooleanField(default=True)),
                ('data_cadastro', models.DateField(auto_now=True)),
            ],
        ),
    ]
