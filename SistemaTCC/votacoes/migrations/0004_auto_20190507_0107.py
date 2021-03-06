# Generated by Django 2.1.7 on 2019-05-07 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votacoes', '0003_auto_20190426_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTurma', models.CharField(max_length=1)),
                ('anoTurma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacoes.Ano')),
                ('cursoTurma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacoes.Curso')),
            ],
        ),
        migrations.AlterModelOptions(
            name='votacao',
            options={'verbose_name_plural': 'votações'},
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='cursoAluno',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='serieAluno',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turmaAluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacoes.Turma'),
        ),
        migrations.AlterField(
            model_name='votacao',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Em Andamento'), (2, 'Pausada'), (3, 'Finalizada')], default=2),
        ),
        migrations.AlterField(
            model_name='voto',
            name='voto',
            field=models.IntegerField(choices=[(1, 'Sim'), (2, 'Não'), (3, 'Abstenção')], default=3),
        ),
        migrations.AddField(
            model_name='ano',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacoes.Curso'),
        ),
    ]
