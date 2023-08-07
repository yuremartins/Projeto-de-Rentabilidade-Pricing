# Projeto de Rentabilidade (Pricing)
Este projeto em Python tem como objetivo calcular a rentabilidade de um veículo com base nos dados da Tabela FIPE e no valor de locação.

## Requisição da API da Tabela FIPE
```
import requests

def fipe_json(resource, data=None):
    url = "http://veiculos.fipe.org.br/api/veiculos"
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br"
    }

    response = requests.post(f"{url}/{resource}", json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
```

 > Este script contém a função `fipe_json`, responsável por realizar requisições HTTP POST à API da Tabela FIPE e retornar os dados em formato JSON.

## Consulta de Valor de Veículo na Tabela FIPE

````
from fipe_api import fipe_json

def consultar_valor_veiculo(data):
    url = "ConsultarValorComTodosParametros"
    return fipe_json(url, data)

# Exemplo de uso
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
````
> Este script contém a função `consultar_valor_veiculo`, que consulta os detalhes de um veículo específico na Tabela FIPE, incluindo o valor de compra.

## Calculadora de Rentabilidade

````
from consulta_fipe import consultar_valor_veiculo

def calcular_valor_locacao(valor_compra, taxa_depreciacao_desejada, taxa_lucro_desejada, prazo_locacao_desejado):

    # A cada semestre aumenta-se 0,5% de depreciação
    semestres_extras = prazo_locacao_desejado / 6

    # Aumentando a taxa de depreciação em meio porcento para cada semestre extra
    taxa_depreciacao_atualizada = taxa_depreciacao_desejada + (semestres_extras * 0.005)

    # Cálculo do valor de venda considerando a depreciação
    valor_venda = valor_compra - (valor_compra * taxa_depreciacao_atualizada)

    # Cálculo do valor de locação necessário para atingir a taxa de lucro desejada
    valor_locacao_necessario = ((valor_compra + (valor_compra * taxa_lucro_desejada)) + (valor_compra - valor_venda)) / prazo_locacao_desejado

    # Cálculo do rental rate (porcentagem do valor de locação em relação ao valor de compra)
    rental_rate = (valor_locacao_necessario / valor_compra) * 100

    return round(valor_locacao_necessario, 2), round(valor_venda, 2), round(rental_rate, 2)

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
valor_compra = float(valor_veiculo["Valor"].replace("R$", "").replace(".", "").replace(",", "."))

# Valores desejados para cálculo de rentabilidade
taxa_depreciacao = 0.25
taxa_lucro = 0.2
prazo_locacao = 24

valor_locacao, valor_venda, rental_rate = calcular_valor_locacao(valor_compra, taxa_depreciacao, taxa_lucro, prazo_locacao)

print("Valor de Locação: R$ {:.2f}".format(valor_locacao))
print("Valor de Venda: R$ {:.2f}".format(valor_venda))
print("Rental Rate: {:.2f}%".format(rental_rate))
````
> Este script contém a função `calcular_rentabilidade` é utilizada para calcular a rentabilidade do veículo com base nos dados obtidos na consulta.
