# Generated by Django 5.1 on 2024-08-30 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogProf', '0007_pessoal_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoal',
            name='portfolio',
            field=models.URLField(blank=True),
        ),
    ]
