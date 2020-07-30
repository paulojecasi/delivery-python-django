from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Cidade(models.Model):
    CIDADE_CHOICES = (
        ('TERESINA', 'TERESINA'),
        ('TIMOM', 'TIMOM')
    )
    ESTADO_CHOICES = (
        ('PI', 'PIAUI'),
        ('MA', 'MARANHAO')
    )

    cidade = models.CharField(max_length=30, blank=True, null=True, verbose_name='Cidade',
                              choices=CIDADE_CHOICES)
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name='U F',
                              choices=ESTADO_CHOICES)

    def __str__(self):
        return self.cidade + " " + self.estado

    class Meta:
        verbose_name = '3  Cadastro de Cidade'
        verbose_name_plural = '3  Cadastro de Cidades'


class Bairro(models.Model):
    COBERTURA_CHOICES = (
        ('S', 'SIM'),
        ('N', 'NAO')
    )

    ZONA_CHOICES = (
        ('RC', 'REGIAO CENTRAL'),
        ('ZN', 'ZONA NORTE'),
        ('ZS', 'ZONA SUL'),
        ('ZL', 'ZONA LESTE'),
        ('ZD', 'ZONA SUDESTE')

    )
    cidade = models.ForeignKey(Cidade, related_name='bairro_cidade',
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Cidade')
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    zona = models.CharField(max_length=2, blank=True, null=True, verbose_name='Zona',
                            choices=ZONA_CHOICES,default="ZD")
    cobertura = models.CharField(max_length=1, blank=True, null=True,
                                 verbose_name='Entregar neste Bairro?',
                                choices=COBERTURA_CHOICES, default="N")

    def __str__(self):
        return self.bairro

    class Meta:
        verbose_name = '4  Cadastro de Bairro'
        verbose_name_plural = '4  Cadastro de Bairros'
        ordering = ["bairro"]


class Cliente(models.Model):
    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )
    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    primeiro_nome = models.CharField(max_length=20, verbose_name='Primeiro Nome', blank=True, null=True)
    sobre_nome = models.CharField(max_length=20, verbose_name='Sobre Nome', blank=True, null=True)
    cnpj = models.CharField(unique=True, max_length=14, blank=True, null=True, verbose_name='C N P J')
    cpf = models.CharField(unique=True, max_length=11, blank=True, null=True, verbose_name='C P F')
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento', auto_now=False)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
    endereco = models.CharField(max_length=300, blank=True, null=True, verbose_name='Endereço')
    numero = models.CharField(max_length=6, blank=True, null=True, verbose_name='Numero')
    complemento = models.CharField(max_length=300, blank=True, null=True, verbose_name='Complemento')
    cep = models.CharField(max_length=10, verbose_name='Cep')
    bairro = models.ForeignKey(Bairro, related_name='cliente_bairro',
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='Bairro')
    cidade = models.ForeignKey(Cidade, related_name='cliente_cidade',
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='Cidade')
    telcelular = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº telefone celular')
    telfixo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº telefone fixo')
    email = models.EmailField(blank=True, null=True,verbose_name='E-Mail')
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº Whatsapp')
    facebook = models.CharField(max_length=80, blank=True, null=True, verbose_name='Facebook')
    instagram = models.CharField(max_length=80, blank=True, null=True, verbose_name='Instagram')
    twitter = models.CharField(max_length=80, blank=True, null=True, verbose_name='twitter')
    dt_cadastro = models.DateField('Data cadastro', blank=True, null=True, auto_now=True)
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')

    class Meta:
        verbose_name = 'Cliente Cadastrado'
        verbose_name_plural = 'Clientes Cadastrados'

class Entrega(models.Model):

    cliente = models.ForeignKey(Cliente, related_name='entrega_cliente',
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Cliente')

    endereco = models.CharField(max_length=300, blank=True, null=True, verbose_name='Endereço')
    numero = models.CharField(max_length=6, blank=True, null=True, verbose_name='Numero')
    complemento = models.CharField(max_length=300, blank=True, null=True, verbose_name='Complemento')
    cep = models.CharField(max_length=10, verbose_name='Cep')
    bairro = models.ForeignKey(Bairro, related_name='entrega_bairro',
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='Bairro')
    cidade = models.ForeignKey(Cidade, related_name='entrega_cidade',
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='Cidade')
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')

    class Meta:
        verbose_name = 'Endereço de Entrega Cadastrado'
        verbose_name_plural = 'Endereços de Entregas Cadastrados'



class Produto(models.Model):
    BEBIDAS_CHOICES = (
        ('KAISER', 'CERVEJA KAISER'),
        ('BRAHMA', 'CERVEJA BRAHMA'),
        ('BRAHMA DUPLO MALTE', 'CERVEJA BRAHMA DUPLO MALTE'),
        ('SKOL', 'CERVEJA SKOL'),
        ('ANTARCTICA', 'CERVEJA ANTARCTICA'),
        ('ANTARCTICA ORIGINAL', 'CERVEJA ANTARCTICA ORIGINAL'),
        ('ANTARCTICA SUB-ZERO', 'CERVEJA ANTARCTICA SUB-ZERO'),
        ('BOHEMIA', 'CERVEJA BOHEMIA'),
        ('HEINEKEN', 'CERVEJA HEINEKEN'),
        ('STELLA', 'CERVEJA STELLA'),
        ('BAVARIA', 'CERVEJA BAVARIA'),
        ('GLACIAL', 'CERVEJA GLACIAL'),
        ('TIJUCA','CERVEJA TIJUCA'),
        ('PETRA','CERVEJA PETRA'),
        ('SCHIN', 'CERVEJA SCHIN'),
        ('ITAIPAVA', 'CERVEJA ITAIPAVA'),
        ('CRYSTAL', 'CERVEJA CRYSTAL'),
        ('DEVASSA', 'CERVEJA DEVASSA'),
        ('EISENBAHN', 'CERVEJA EISENBAHN'),
        ('CORONA', 'CERVEJA CORONA'),
        ('BUDWEISER', 'CERVEJA BUDWEISER'),
        ('CARACU', 'CERVEJA CARACU'),
        ('BADER','CERVEJA BADER'),
        ('TERESOPOLIS','CERVEJA TERESOPOLIS'),
        ('COCACOLA', 'REFRIGERANTE COCA COLA'),
        ('GUARANA ANTARCTICA','GUARANA ANTARCTICA'),
        ('GUARANA SCHIN','GUARANA SCHIN'),
        ('GUARANA FANTA', 'GUARANA FANTA'),
        ('GUARANA KUAT', 'GUARANA KUAT'),
        ('FANTA LARANJA','REFRIGERANTE FANTA LARANJA'),
        ('FANTA UVA', 'REFRIGERANTE FANTA UVA'),
        ('CAJUINA NODESTINA','CAJUINA NODESTINA'),
        ('CACHAÇA MAGUEIRA OURO','CACHAÇA MAGUEIRA OURO'),
        ('CACHAÇA MAGUEIRA', 'CACHAÇA MAGUEIRA'),
        ('VODKA SLOVA','VODKA SLOVA'),
        ('VINHO PADRE CICERO', 'VINHO PADRE CICERO'),
        ('VINHO QUINTO DO MORGADO', 'VINHO QUINTO DO MORGADO'),
        ('VINHO GAUCHO', 'VINHO GAUCHO'),
        ('GELO', 'GELO'),
        ("CARVAO","CARVAO")


    )
    ordena_choices = sorted(BEBIDAS_CHOICES, key=lambda x: x[1])
    BEBIDAS_CHOICES = ordena_choices

    DESC_CHOICES = (
        ('Cerveja Pilsen', 'Cerveja Pilsen'),
        ('Cerveja Lager', 'Cerveja Lager'),
        ('Cerveja Puro Malte', 'Cerveja Puro Malte'),
        ('Cerveja Duplo Malte', 'Cerveja Duplo Malte'),
        ('Cerveja Premium', 'Cerveja Premium'),
        ('Cerveja Heles', 'Cerveja Heles'),
        ('Cerveja Dortmunder Export', 'Cerveja Dortmunder Export'),
        ('Cerveja Dry Beer', 'Cerveja Dry Beer'),
        ('Refrigerante Cola', 'Refrigerante Cola'),
        ('Guarana', 'Guarana'),
        ('Refrigerante', 'Refrigerante'),
        ('Cajuina','Cajuina'),
        ('Cachaça','Cachaça'),
        ('Vodka', 'Vodka'),
        ('Vinho', 'Vinho'),
        ('Gelo em cubos', 'Gelo em cubos'),
        ('Carvao Vegetal','Carvao Vegetal')

    )
    ordena_choices = sorted(DESC_CHOICES, key=lambda x: x[1])
    DESC_CHOICES = ordena_choices

    TAMANHO_CHOICES = (
        ('GARRAFA 1 LT RETORNAVEL', 'GARRAFA 1 LT RETORNAVEL'),
        ('PET 2 LTS','PET 2 LTS'),
        ('PET 1 LTS', 'PET 1 LTS'),
        ('PET 1.5 LTS', 'PET 1.5 LTS'),
        ('PET 2 LITROS', 'PET 2 LTS'),
        ('KS RETORNAVEL', 'KS RETORNAVEL'),
        ('PET 2 LTS RETORNAVEL', 'PET 2 LTS RETORNAVEL'),
        ('PET 1 LTS RETORNAVEL', 'PET 1 LTS RETORNAVEL'),
        ('PET 1.5 LTS RETORNAVEL', 'PET 1.5 LTS RETORNAVEL'),
        ('PET 2 LITROS RETORNAVEL', 'PET 2  LTS RETORNAVEL'),
        ('LONG NECK 250 ML', 'LONG NECK 250 ML'),
        ('LONG NECK 275 ML', 'LONG NECK 275 ML'),
        ('LONG NECK 330 ML', 'LONG NECK 330 ML'),
        ('LONG NECK 350 ML', 'LONG NECK 350 ML'),
        ('LONG NECK 355 ML', 'LONG NECK 355 ML'),
        ('LITRO 600 ML', 'LITRO 600 ML'),
        ('LITRAO 990 ML', 'LITRAO 990 ML'),
        ('LITRAO 1000 ML', 'LITRAO 1000 ML'),
        ('LATINHA 269 ML', 'LATINHA 269 ML'),
        ('LATA 350 ML', 'LATA 350 ML'),
        ('LATAO 473 ML', 'LATAO 473 ML'),
        ('LATAO 550 ML', 'LATA 550 ML'),
        ('PERIGUETE 300 ML', 'PERIGUETE 300 ML'),
        ('GARRAFA 490 ML', 'GARRAFA 490 ML'),
        ('GARRAFA 960 ML', 'GARRAFA 960 ML'),
        ('GARRAFA 480 ML', 'GARRAFA 480 ML'),
        ('GARRAFA 970 ML', 'GARRAFA 970 ML'),
        ('GARRAFA 890 ML', 'GARRAFA 890 ML'),
        ('GARRAFA 750 ML', 'GARRAFA 750 ML'),
        ('GARRAFA 400 ML', 'GARRAFA 400 ML'),

    )

    ordena_choices = sorted(TAMANHO_CHOICES, key=lambda x: x[1])
    TAMANHO_CHOICES = ordena_choices

    PARAOSITE = (
        ('SIM', 'SIM'),
        ('NAO', 'NAO')
    )

    site = models.CharField(max_length=3, verbose_name='Para apresentação no site?',
                            default="SIM", choices=PARAOSITE,
                            help_text='Informe se o produto vai aparecer no site')
    bebida = models.CharField(max_length=100, verbose_name='Bebida', choices=BEBIDAS_CHOICES,
                              help_text='Selecione o produto')
    complemento = models.CharField(max_length=200, blank=True, null=True,
                                   verbose_name='Descrição Complementar',
                                   help_text='Complemento de informações do produto',
                                   choices=DESC_CHOICES)
    tamanho = models.CharField(max_length=100, verbose_name='Tamanho', choices=TAMANHO_CHOICES,
                               help_text='Selecione a quantidade/tamanho')
    valor = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Valor R$',
                                help_text='Informe o valor')
    url_imagem = models.CharField(max_length=600, blank=True, null=True,
                                  verbose_name='URL da Imagem do Produto',
                                  help_text='Digite a url de endereço da imagem')
    foto = models.FileField (upload_to='media/images/produtos', blank=True, null=True,
                             verbose_name='Foto do Produto',
                             help_text='Selecione a foto do produto')
    dt_inicio = models.DateField('Data inicio da apresentação', blank=True, null=True,
                                 auto_now=False)
    dt_final = models.DateField('Data final da apresentação',  blank=True, null=True,
                                 auto_now=False)

    def __str__(self):
        return self.bebida +  " " + self.tamanho + "  " + self.complemento + ",    Site: " + self.site

    class Meta:
        ordering = ['bebida']
        verbose_name = '1  Cadastro e manutenção de Produto'
        verbose_name_plural = '1  Cadastro e manutenção de Produtos'



class Carrinho(models.Model):
    SITUACAO_CARRINHO_BEB = (
        ('0', 'ABERTO'),
        ('1', 'FECHADO'),
        ('2', 'CANCELADO')
    )

    produto = models.ForeignKey(Produto, related_name='carrinho_bebidas',
        on_delete=models.CASCADE,
        null=True,
        verbose_name= 'Produto'
    )


    dt_inclusao = models.DateField('Data de inclusão no carrinho',
        blank=True,
        null=True,
        editable=True,
        auto_now=True
    )
    valor_unitario = models.DecimalField(
        max_digits=12, decimal_places=2,
        verbose_name='Valor unitario R$'
    )
    quantidade = models.DecimalField(
        max_digits=7, decimal_places=2,
        verbose_name='Quntidade de itens'
    )
    valor_total_item = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Valor Total R$'
    )
    situacao_carrinho = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Situação do carrinho',
        choices=SITUACAO_CARRINHO_BEB
    )

class Pedido(models.Model):
    TIPO_PEDIDO = (
        ('1', 'CONVENIENCIA'),
        ('2', 'ALUGUEIS'),
        ('3', 'OUTROS')
    )

    SITUACAO_PEDIDO = (
        ('0', 'ABERTO'),
        ('1', 'FECHADO'),
        ('2', 'CANCELADO')
    )

    carrinho = models.ForeignKey(Carrinho, related_name='pedido_carrinho',
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='Carrinho'
                               )

    tipo_pedido = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Tipo de Pedido',
        choices=TIPO_PEDIDO
    )
    dt_abertura = models.DateField('Data de abertura do pedido',
        blank=True,
        null=True,
        auto_now=True


    )
    dt_fechamento = models.DateField('Data fechamento do pedido',
        blank=True,
        null=True,
        auto_now = True

    )

    dt_cancelamento = models.DateField('Data cancelamento do pedido',
        blank=True,
        null=True,
        auto_now = True
    )

    situacao = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Situação do pedido',
        choices = SITUACAO_PEDIDO
    )

    valor = models.DecimalField(
        max_digits=12,
        blank=True,
        null=True,
        decimal_places=2,
        verbose_name='Valor do pedido R$')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Pedido Realizado'
        verbose_name_plural = 'Pedidos Realizados'



class Libera(models.Model):
    PAGINAS_CHOICES = (
        ('delivery','Delivery'),
        ('catalogo','Catalogo')
    )

    LIBERA_CHOICES = (
        ('S', 'SIM'),
        ('N', 'NAO'),
    )
    pagina = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        choices= PAGINAS_CHOICES,
        verbose_name='Pagina')

    libera = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        verbose_name='Liberada para uso? ',
        choices=LIBERA_CHOICES)

    link = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name= "Link da Pagina"
    )

    def __str__(self):
        return self.pagina + " Pagina liberada para uso?: " + self.libera

    class Meta:
        verbose_name = '2  Liberação de Página'
        verbose_name_plural = '2  Liberação de Páginas'
