# Generated by Django 4.0.3 on 2022-03-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_epi_botas_alter_epi_capas_de_chuva_refletores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aso',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
