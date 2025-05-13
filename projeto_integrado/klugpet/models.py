from django.db import models
from django.db.models import Sum 
from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal

class Usuario(AbstractUser):
    NIVEL_CHOICES = (
        ('admin', 'Administrador'),
        ('funcionario', 'Funcionário'),
    )
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='funcionario')

    def __str__(self):
        return self.username

class Tutor(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    conheceu = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_completo

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100, blank=True, null=True)
    idade = models.CharField(blank=True, null=True)
    sexo = models.CharField(max_length=100, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    observacoes_medicas = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='pets/', blank=True, null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome_servico = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Altere para DecimalField

    def __str__(self):
        return self.nome_servico

class Agendamento(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    data_agendamento = models.DateField()
    status = models.CharField(max_length=20, choices=[(
        'Sim', 'Sim'),
        ('Não', 'Não')
    ])
    observacoes = models.TextField(blank=True, null=True)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    valor_total_bruto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Definindo o método dentro da classe Agendamento
    def calcular_valor_total(self):
        total = self.servicos.all().aggregate(total=Sum('preco'))['total'] or Decimal('0.00')

    # Garante que o desconto percentual seja Decimal, mesmo se vier de outro tipo
        desconto_percentual = Decimal(self.desconto_percentual)

    # Calcular o desconto com todos os tipos sendo Decimal
        desconto = total * (desconto_percentual / Decimal('100.00'))

        valor_total = total - desconto

        return valor_total

    def __str__(self):
        return f"Agendamento {self.id} - {self.pet.nome}"

class Nota(models.Model):
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)
    numero_nota = models.AutoField(primary_key=True)
    data_emissao = models.DateTimeField(auto_now_add=True)