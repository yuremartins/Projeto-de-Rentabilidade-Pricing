from django.db import models

class Veiculo(models.Model):
    codigoTabelaReferencia = models.IntegerField()
    codigoTipoVeiculo = models.IntegerField()
    codigoMarca = models.IntegerField()
    codigoModelo = models.IntegerField()
    ano = models.CharField(max_length=8)  # Pode ser também um DateField ou IntegerField dependendo do uso
    codigoTipoCombustivel = models.IntegerField()
    anoModelo = models.IntegerField()
    tipoConsulta = models.CharField(max_length=20)

