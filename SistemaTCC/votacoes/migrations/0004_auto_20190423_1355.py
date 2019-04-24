# Generated by Django 2.1.7 on 2019-04-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacoes', '0003_auto_20190422_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voto', models.IntegerField(default=0)),
                ('user', models.CharField(default='Vazio', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='votacao',
            name='votosN',
        ),
        migrations.RemoveField(
            model_name='votacao',
            name='votosP',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='serieAluno',
            field=models.IntegerField(),
        ),
    ]
