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

def calcular_rentabilidade(valor_compra, taxa_depreciacao, taxa_lucro, prazo_locacao, valor_locacao):
    valor_venda = valor_compra * (1 - taxa_depreciacao)
    valor_lucro = valor_compra * taxa_lucro
    
    valor_faturamento_periodo = (valor_venda - valor_compra) / prazo_locacao + valor_lucro
    valor_faturamento_total = valor_faturamento_periodo * prazo_locacao
    
    rental_rate = (valor_locacao / valor_compra) * 100
    
    return {
        'valor_compra': valor_compra,
        'valor_venda': valor_venda,
        'valor_lucro': valor_lucro,
        'valor_faturamento_periodo': valor_faturamento_periodo,
        'valor_faturamento_total': valor_faturamento_total,
        'rental_rate': round(rental_rate, 2)
    }

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
valor_compra = float(valor_veiculo["Valor"].replace("R$", "").replace(".", "").replace(",", "."))
valor_locacao = 3000  # Valor de locação (exemplo)

# Valores para cálculo de rentabilidade
taxa_depreciacao = 0.6
taxa_lucro = 0.5
prazo_locacao = 12

resultado = calcular_rentabilidade(valor_compra, taxa_depreciacao, taxa_lucro, prazo_locacao, valor_locacao)
print(resultado)
````
> Este script contém a função `calcular_rentabilidade` é utilizada para calcular a rentabilidade do veículo com base nos dados obtidos na consulta.
