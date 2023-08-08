from consulta_fipe import consultar_valor_veiculo

def calcular_valor_locacao(valor_compra, taxa_depreciacao_desejada, taxa_lucro_desejada, prazo_locacao_desejado):

    # A cada semestre aumenta-se 0,5% de depreciação
    semestres_extras = prazo_locacao_desejado / 6

    # Aumentando a taxa de depreciação em meio porcento para cada semestre extra
    taxa_depreciacao_atualizada = taxa_depreciacao_desejada + (semestres_extras * 0.005)

    valor_depreciado = valor_compra * taxa_depreciacao_atualizada

    # Cálculo do valor de venda considerando a depreciação
    valor_venda = valor_compra - (valor_compra * taxa_depreciacao_atualizada)

    # Cálculo do valor de locação necessário para atingir a taxa de lucro desejada
    valor_locacao_necessario = ((valor_compra + (valor_compra * taxa_lucro_desejada)) - valor_venda) / prazo_locacao_desejado

    # Cálculo do rental rate (porcentagem do valor de locação em relação ao valor de compra)
    rental_rate = (valor_locacao_necessario / valor_compra) * 100

    faturamento_total = (valor_locacao_necessario * prazo_locacao_desejado) + valor_venda

    return round(valor_locacao_necessario, 2), round(valor_venda, 2), round(rental_rate, 2), round(faturamento_total,2), round(taxa_depreciacao_atualizada,2), round(valor_depreciado,2)

data = {
    "codigoTabelaReferencia": 300,
    "codigoTipoVeiculo": 1,
    "codigoMarca": 56,
    "codigoModelo": 7409,
    "ano": "2023-3",
    "codigoTipoCombustivel": 3,
    "anoModelo": 2023,
    "tipoConsulta": "tradicional"
}

valor_veiculo = consultar_valor_veiculo(data)
valor_compra = float(valor_veiculo["Valor"].replace("R$", "").replace(".", "").replace(",", "."))

# Valores desejados para cálculo de rentabilidade
taxa_depreciacao = 0.20
taxa_lucro = 0.10
prazo_locacao = 20

valor_locacao_necessario, valor_venda, rental_rate, faturamento_total, taxa_depreciacao_atualizada, valor_depreciado = calcular_valor_locacao(valor_compra, taxa_depreciacao, taxa_lucro, prazo_locacao)

print("Valor de Locação: R$ {:.2f}".format(valor_locacao_necessario))
print("Valor de Venda: R$ {:.2f}".format(valor_venda))
print("Rental Rate: {:.2f}%".format(rental_rate))
print("Faturamento Total: R$ {:.2f}".format(faturamento_total))
print("Taxa de depreciação: {:.2f}%".format(taxa_depreciacao_atualizada*100))
print("Valor Depreciado: R$ {:.2f}".format(valor_depreciado))

