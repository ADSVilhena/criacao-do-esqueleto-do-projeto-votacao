# Generated by Django 2.1.7 on 2019-05-07 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacoes', '0004_auto_20190507_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ano',
            name='curso',
        ),
    ]
