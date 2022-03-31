# Generated by Django 4.0.3 on 2022-03-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_aso_funcao_alter_aso_realizacao_exame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='epi',
            name='pasta_plastica',
        ),
        migrations.AddField(
            model_name='epi',
            name='camisa',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='Luvas',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='abafadores',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='botas',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='capacetes',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='capas_de_chuva_refletores',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='colete_refletor',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='galochas',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='jugulares',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='lanterna',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='oculos_claros',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='oculos_escuros',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='perneiras',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]