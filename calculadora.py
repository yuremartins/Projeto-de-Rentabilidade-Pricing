from consulta_fipe import consultar_valor_veiculo

def calcular_valor_locacao(valor_compra, taxa_depreciacao_desejada, taxa_lucro_desejada, prazo_locacao_desejado):
    # Cálculo do valor de venda considerando a depreciação
    valor_venda = valor_compra - (valor_compra * taxa_depreciacao_desejada)

    # Cálculo do valor de locação necessário para atingir a taxa de lucro desejada
    valor_locacao_necessario = valor_venda / ((1 + taxa_lucro_desejada) ** prazo_locacao_desejado)

    # Cálculo do rental rate (porcentagem do valor de locação em relação ao valor de compra)
    rental_rate = (valor_locacao_necessario / valor_compra) * 100

    return round(valor_locacao_necessario, 2), round(valor_venda, 2), round(rental_rate, 2)

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

# Valores desejados para cálculo de rentabilidade
taxa_depreciacao = 0.4
taxa_lucro = 0.2
prazo_locacao = 12

valor_locacao, valor_venda, rental_rate = calcular_valor_locacao(valor_compra, taxa_depreciacao, taxa_lucro, prazo_locacao)

print("Valor de Locação: R$ {:.2f}".format(valor_locacao))
print("Valor de Venda: R$ {:.2f}".format(valor_venda))
print("Rental Rate: {:.2f}%".format(rental_rate))

