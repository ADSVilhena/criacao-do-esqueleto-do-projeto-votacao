# Generated by Django 2.1.7 on 2019-04-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacoes', '0002_auto_20190426_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votacao',
            name='concluida',
        ),
        migrations.AddField(
            model_name='votacao',
            name='estado',
            field=models.IntegerField(default=2, verbose_name=((1, 'Em Andamento'), (2, 'Pausada'), (3, 'Finalizada'))),
        ),
        migrations.AlterField(
            model_name='voto',
            name='voto',
            field=models.CharField(default='Abstenção', max_length=16),
        ),
    ]
