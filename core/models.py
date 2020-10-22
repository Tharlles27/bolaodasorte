from django.db import models
from django.db.models import Count, Max
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    pagamento = models.BooleanField(default=True)
    repeticao = models.BooleanField(default=False)
    quantidade = models.IntegerField(default=0, null=True, blank=True)

    def acertos(self):
        return self.escolha_set.filter(sorteado=True).count()

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):

        super(Pessoa, self).save(*args, **kwargs)

class Escolha(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numeros = models.IntegerField()
    sorteado = models.BooleanField(default=False)
    acertos = models.IntegerField(default=0, null=True, blank=True)
    
    class Meta:
        ordering = ['numeros']
        unique_together = [('pessoa', 'numeros')]
        verbose_name_plural = "Escolhas"
        verbose_name     = "Escolha"
        
    def __str__(self):
        return str(self.numeros)

    def refresh(sender, instance, **kwargs):   
        Escolha.objects.all().update(sorteado=False)

    def save(self, *args, **kwargs):
        super(Escolha, self).save(*args, **kwargs)

class Rodadas(models.Model):
   
    RODADA_CHOICES = ( 
    ("1° Rodada", "1° Rodada"), 
    ("2° Rodada", "2° Rodada"), 
    ("3° Rodada", "3° Rodada"), 
    ("4° Rodada", "4° Rodada"), 
    ("5° Rodada", "5° Rodada"),
    ("6° Rodada", "6° Rodada"),
    ("7° Rodada", "7° Rodada"),
    ("8° Rodada", "8° Rodada"),
    ("9° Rodada", "9° Rodada"),
    ("10° Rodada", "10° Rodada"),
    ("11° Rodada", "11° Rodada"),) 

    data = models.DateTimeField(auto_now_add=True)
    num_rodada = models.CharField(max_length=11, choices=RODADA_CHOICES, verbose_name='Numero da rodada')

    def _calculo(sender, instance, **kwargs):
        super(Rodadas, self).save(*args, **kwargs)

    def __str__(self):
        return self.num_rodada

class Dezenas(models.Model):
    rodada = models.ForeignKey(Rodadas, on_delete=models.CASCADE)
    dezena = models.IntegerField()

    class Meta:
        ordering = ['dezena']
        unique_together =[('rodada', 'dezena')]

    
    def save(self, *args, **kwargs):
        escolha = Escolha.objects.all() 
        for vv in escolha:
            if vv.numeros == self.dezena:
                vv.sorteado = True
                vv.save()
        super(Dezenas, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.dezena}'
#comando signals
post_delete.connect(Escolha.refresh, sender=Dezenas)

class Acertos(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    acertos = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)

class Config(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    v_max_ponto = models.IntegerField(verbose_name='Porcentagem para maior pontuador. ex(30) para 30%', null=True, blank=True)
    v_min_ponto = models.IntegerField(verbose_name='Porcentagem para menor pontuador. ex(10) para 10%', null=True, blank=True)
    valor_jogada = models.IntegerField(verbose_name='Valor padrão de cada rodada, ex: 10, para 10,00R$', null=True, blank=True)

    def __str__(self):
        return f'Maior pontuação:{self.v_max_ponto} --- Menor pontuação: {self.v_min_ponto} ---Valor da jogada: {self.valor_jogada}'

    
   
 
    
