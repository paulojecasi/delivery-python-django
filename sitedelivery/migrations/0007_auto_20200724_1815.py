# Generated by Django 3.0.8 on 2020-07-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedelivery', '0006_auto_20200723_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagina', models.CharField(blank=True, max_length=1, null=True, verbose_name='Pagina ')),
                ('libera', models.CharField(blank=True, choices=[('S', 'SIM'), ('N', 'NAO')], max_length=1, null=True, verbose_name='Liberada para uso? ')),
            ],
        ),
        migrations.AlterModelOptions(
            name='bairro',
            options={'verbose_name': '3 - Cadastro de Bairro', 'verbose_name_plural': '3 - Cadastro de Bairros'},
        ),
        migrations.AlterModelOptions(
            name='cidade',
            options={'verbose_name': '2 - Cadastro de Cidade', 'verbose_name_plural': '2 - Cadastro de Cidades'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente Cadastrado', 'verbose_name_plural': 'Clientes Cadastrados'},
        ),
        migrations.AlterModelOptions(
            name='entrega',
            options={'verbose_name': 'Endereço de Entrega Cadastrado', 'verbose_name_plural': 'Endereços de Entregas Cadastrados'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name': 'Pedido Realizado', 'verbose_name_plural': 'Pedidos Realizados'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['bebida'], 'verbose_name': '1 - Cadastro e manutenção de Produto', 'verbose_name_plural': '1 - Cadastro e manutenção de Produtos'},
        ),
        migrations.AlterField(
            model_name='produto',
            name='bebida',
            field=models.CharField(choices=[('ANTARCTICA', 'ANTARCTICA'), ('BADER', 'BADER'), ('BAVARIA', 'BAVARIA'), ('BOHEMIA', 'BOHEMIA'), ('BRAHMA', 'BRAHMA'), ('BUDWEISER', 'BUDWEISER'), ('CARACU', 'CARACU'), ('CORONA', 'CORONA'), ('CRYSTAL', 'CRYSTAL'), ('DEVASSA', 'DEVASSA'), ('EISENBAHN', 'EISENBAHN'), ('GLACIAL', 'GLACIAL'), ('GUARANA ANTARCTICA', 'GUARANA ANTARCTICA'), ('GUARANA FANTA', 'GUARANA FANTA'), ('GUARANA KUAT', 'GUARANA KUAT'), ('GUARANA SCHIN', 'GUARANA SCHIN'), ('HEINEKEN', 'HEINEKEN'), ('ITAIPAVA', 'ITAIPAVA'), ('KAISER', 'KAISER'), ('PETRA', 'PETRA'), ('REFRI COCACOLA', 'REFRI COCA COLA'), ('REFRI FANTA LARANJA', 'REFRI FANTA LARANJA'), ('REFRI FANTA UVA', 'REFRI FANTA UVA'), ('SCHIN', 'SCHIN'), ('SKOL', 'SKOL'), ('STELLA', 'STELLA'), ('TERESOPOLIS', 'TERESOPOLIS'), ('TIJUCA', 'TIJUCA')], help_text='Selecione o produto', max_length=100, verbose_name='Bebida'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(choices=[('GARRAFA 1 LT RETORNAVEL', 'GARRAFA 1 LT RETORNAVEL'), ('KS RETORNAVEL', 'KS RETORNAVEL'), ('LATA 350 ML', 'LATA 350 ML'), ('LATAO 550 ML', 'LATA 550 ML'), ('LATAO 473 ML', 'LATAO 473 ML'), ('LATINHA 269 ML', 'LATINHA 269 ML'), ('LITRAO 1000 ML', 'LITRAO 1000 ML'), ('LITRAO 990 ML', 'LITRAO 990 ML'), ('LITRO 600 ML', 'LITRO 600 ML'), ('LONG NECK 250 ML', 'LONG NECK 250 ML'), ('LONG NECK 275 ML', 'LONG NECK 275 ML'), ('LONG NECK 330 ML', 'LONG NECK 330 ML'), ('LONG NECK 350 ML', 'LONG NECK 350 ML'), ('LONG NECK 355 ML', 'LONG NECK 355 ML'), ('PERIGUETE 300 ML', 'PERIGUETE 300 ML'), ('PET 1 LTS', 'PET 1 LTS'), ('PET 1 LTS RETORNAVEL', 'PET 1 LTS RETORNAVEL'), ('PET 1.5 LTS', 'PET 1.5 LTS'), ('PET 1.5 LTS RETORNAVEL', 'PET 1.5 LTS RETORNAVEL'), ('PET 2 LITROS RETORNAVEL', 'PET 2  LTS RETORNAVEL'), ('PET 2 LTS', 'PET 2 LTS'), ('PET 2 LITROS', 'PET 2 LTS'), ('PET 2 LTS RETORNAVEL', 'PET 2 LTS RETORNAVEL')], help_text='Selecione a quantidade/tamanho', max_length=100, verbose_name='Tamanho'),
        ),
    ]
