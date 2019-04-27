# Generated by Django 2.1.7 on 2019-04-27 00:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagemAluno', models.ImageField(upload_to='images/')),
                ('nomeAluno', models.CharField(max_length=255)),
                ('cursoAluno', models.CharField(max_length=50)),
                ('turmaAluno', models.CharField(max_length=1)),
                ('cpfAluno', models.CharField(max_length=14)),
                ('serieAluno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('concluida', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacoes.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voto', models.CharField(default='Branco', max_length=6)),
                ('professor', models.CharField(default='Vazio', max_length=255)),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacoes.Votacao')),
            ],
        ),
    ]
