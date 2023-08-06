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

