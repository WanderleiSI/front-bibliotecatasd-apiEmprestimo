from django.db import models
from datetime import date

# Create your models here.
class Emprestimo(models.Model):
    titulo = models.CharField(verbose_name="titulo",max_length=100,null=False, blank=False)
    idCliente = models.IntegerField(verbose_name="idCliente",null=False, blank=False)
    idLivro = models.IntegerField(verbose_name="idLivro",null=False, blank=False)
    dataEmprestimo = models.DateTimeField(verbose_name="dataEmprestimo",auto_now_add=True, null=False, blank=False)
    dataDevolucao = models.DateField(verbose_name="dataDevolucao",null=False, blank=False)
    entregueEm = models.DateField(verbose_name="entregueEm",null=True)

    class Meta:
        ordering = ["dataDevolucao"]

    def entregue(self):
        if not self.entregueEm:
            self.entregueEm = date.today()
            self.save()