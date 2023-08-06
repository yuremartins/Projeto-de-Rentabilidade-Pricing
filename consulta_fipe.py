from fipe_api import fipe_json

def consultar_valor_veiculo(data):
    url = "ConsultarValorComTodosParametros"
    return fipe_json(url, data)

data = {
    "codigoTabelaReferencia": 231,
    "codigoTipoVeiculo": 1,
    "codigoMarca": 26,
    "codigoModelo": 4925,
    "ano": "2010-1",
    "codigoTipoCombustivel": 1,
    "anoModelo": 2011,
    "tipoConsulta": "tradicional"
}

valor_veiculo = consultar_valor_veiculo(data)
print(valor_veiculo)

