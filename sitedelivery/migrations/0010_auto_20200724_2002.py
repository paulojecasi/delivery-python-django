# Generated by Django 3.0.8 on 2020-07-24 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitedelivery', '0009_auto_20200724_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='estado',
        ),
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente_bairro', to='sitedelivery.Bairro', verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='bairro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrega_bairro', to='sitedelivery.Bairro', verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente_cidade', to='sitedelivery.Cidade', verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrega_cidade', to='sitedelivery.Cidade', verbose_name='Cidade'),
        ),
    ]