# Generated by Django 3.0.8 on 2020-08-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedelivery', '0014_auto_20200811_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='classificacao',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')], help_text='Posição que o produto vai aparecer no site', max_length=3, verbose_name='Classificaçao no site?'),
        ),
    ]
