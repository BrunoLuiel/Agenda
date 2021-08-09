from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) #Pode ficar em branco ou possuir valor null
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação',auto_now=True) #Inserir a hora atual da criação
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #item já do Django, criação de usuários

    class Meta:
        db_table = 'evento'# Ao criar a tabela automaticamente o sistema a nomeou de core_evento, mas para eu alterar o nome será usado essa class

    def __str__(self):
        return self.titulo # Para melhorar pois no site quando vai ver o evento salvo fica um nome estranho e com essa configuração fica o mesmo nome do título 


