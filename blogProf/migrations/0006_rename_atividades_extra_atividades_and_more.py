# Generated by Django 5.1 on 2024-08-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogProf', '0005_atividades_extra_habilidades_tecnicas_pessoal_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Atividades_extra',
            new_name='Atividades',
        ),
        migrations.RenameModel(
            old_name='Habilidades_tecnicas',
            new_name='Habilidades',
        ),
        migrations.RemoveField(
            model_name='pessoal',
            name='imagem',
        ),
        migrations.AddField(
            model_name='pessoal',
            name='imagemBg',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='pessoal',
            name='imagemIntro',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
