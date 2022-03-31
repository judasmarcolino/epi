# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Colaborador(models.Model):
    
    TIPO_TRABALHADOR=(
        ("Interno","Interno"),
        ("Externo","Externo"),
        ("Contratado","Contratado"),
    )
    id = models.BigAutoField(primary_key=True, )
    nome  = models.CharField(max_length=100, unique=True)
    cargo = models.CharField(max_length=100, null=True)
    nib = models.CharField(max_length=100 , null=True)
    categoria =models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.CharField(max_length=100,choices=TIPO_TRABALHADOR)
    nr_bi = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=100, null=True)
    nuit = models.CharField(max_length=100, null=True)
    inss =models.CharField(max_length=100, null=True)
    data_nascimeto = models.DateField(auto_now_add=False, null=True)
    def __str__(self):
        return self.nome
    


class Epi(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=True,blank=True)   
    botas = models.IntegerField(null=True,blank=True)
    camisa =models.IntegerField(null=True,blank=True)
    perneiras = models.IntegerField(null=True,blank=True)
    capacetes = models.IntegerField(null=True,blank=True)
    jugulares = models.IntegerField(null=True,blank=True)
    abafadores = models.IntegerField(null=True,blank=True)
    colete_refletor= models.IntegerField(null=True,blank=True)
    oculos_de_protecao = models.IntegerField(null=True,blank=True)
    Luvas = models.IntegerField(null=True,blank=True)
    galochas = models.IntegerField(null=True,blank=True)
    capas_de_chuva_refletores = models.IntegerField(null=True,blank=True)
    lanterna = models.IntegerField(null=True,blank=True)
    data_recepcao = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    observacao = models.CharField(max_length=100, null=True,blank=True)
    
   

class Aso(models.Model):
    ESTADO =(
        ('Liberado','Liberado'),
        ('Pendente','Pendente'),
    )
    CLINICA =(
        ("Clinica Sorriso","Clinica Sorriso"),
        ("SEPRI","SEPRI"),   
    )
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100,null=True,blank=True)
    base =models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(choices=ESTADO, max_length=100,null=True,blank=True)
    clinica = models.CharField(choices=CLINICA,max_length=100,blank=True,null=True)
    realizacao_exame =models.DateField(max_length=100,null=True,blank=True)
    validade = models.DateField(null=True,blank=True)
    local_entrega = models.CharField(max_length=100, null=True,blank=True)
    observacao = models.CharField(max_length=200, null=True,blank=True)
  
        

class Rac(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.ForeignKey(Colaborador,on_delete=models.CASCADE,null=True,blank=True)
    validade = models.ForeignKey(Aso,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.id

class Cracha(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.ForeignKey(Colaborador,on_delete=models.CASCADE)
    Codigo = models.CharField(max_length=100)
    validade= models.ForeignKey(Aso,null=True,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.id