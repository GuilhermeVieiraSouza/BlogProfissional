# Generated by Django 5.1 on 2024-08-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
