# Generated by Django 5.0.1 on 2024-01-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('idCliente', models.IntegerField()),
                ('idLivro', models.IntegerField()),
                ('dataEmprestimo', models.DateTimeField(auto_now_add=True)),
                ('dataDevolucao', models.DateTimeField()),
                ('entregueEm', models.DateField(null=True)),
            ],
            options={
                'ordering': ['dataDevolucao'],
            },
        ),
    ]
