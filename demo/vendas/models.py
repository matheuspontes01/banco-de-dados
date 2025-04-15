from django.db import models

# Create your models here.
#METODO PARA SALVAR UM CLIENTE NO BANCO DE DADOS
class Cliente(models.Model):
    '''
    GERANDO A CHAVE AUTOMATICAMENTE'''
    id_cliente = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)  # Formato: 000.000.000-00
    telefone = models.CharField(max_length=20)

    class Meta:
        managed = False  # Django NÃO vai tentar criar ou alterar essa tabela
        db_table = 'cliente'  # nome EXATO da tabela no banco PostgreSQL

    def __str__(self):
        return self.nome
