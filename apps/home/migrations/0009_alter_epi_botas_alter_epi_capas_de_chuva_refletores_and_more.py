# Generated by Django 4.0.3 on 2022-03-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_capas_refletores_epi_capas_de_chuva_refletores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epi',
            name='botas',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='capas_de_chuva_refletores',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='galochas',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='epi',
            name='oculos_claros',
            field=models.BooleanField(default=True),
        ),
    ]
