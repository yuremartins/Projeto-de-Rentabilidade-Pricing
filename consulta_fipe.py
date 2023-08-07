from fipe_api import fipe_json

def consultar_valor_veiculo(data):
    url = "ConsultarValorComTodosParametros"
    return fipe_json(url, data)

data = {
    "codigoTabelaReferencia": 300,
    "codigoTipoVeiculo": 1,
    "codigoMarca": 56,
    "codigoModelo": 10172,
    "ano": "2023-3",
    "codigoTipoCombustivel": 3,
    "anoModelo": 2023,
    "tipoConsulta": "tradicional"
}

valor_veiculo = consultar_valor_veiculo(data)
print(valor_veiculo)

