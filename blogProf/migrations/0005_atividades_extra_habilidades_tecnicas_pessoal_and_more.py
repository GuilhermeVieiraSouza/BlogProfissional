# Generated by Django 5.1 on 2024-08-29 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogProf', '0004_guilherme_delete_eu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividades_extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidades_tecnicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='images/')),
                ('video', models.FileField(blank=True, upload_to='videos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='guilherme',
            name='cursos',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Guilherme',
        ),
    ]
