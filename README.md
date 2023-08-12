# Projeto de Rentabilidade (Pricing)
Este projeto em Python tem como objetivo calcular a rentabilidade de um veículo com base nos dados da Tabela FIPE e no valor de locação.

## Análise de Rentabilidade
- **Dataset:** [Kaggle](https://www.kaggle.com/datasets/yuremartins/car-rental-data)
- **Notebook:** [Pricing](https://www.kaggle.com/code/yuremartins/pricing)

## Requisição da API da Tabela FIPE

![image](https://github.com/yuremartins/Projeto-de-Rentabilidade-Pricing/blob/main/notebooks/PrtSc/Consulta%20de%20Ve%C3%ADculo.png?raw=true)

```
def consultar_valor_veiculo(data):
    url = "ConsultarValorComTodosParametros"
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br"
    }
    response = requests.post(f"http://veiculos.fipe.org.br/api/veiculos/{url}", json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
```

 > Este script contém a função `consultar_valor_veiculo`, responsável por realizar requisições HTTP POST à API da Tabela FIPE e retornar os dados em formato JSON.

## Consulta de Valor de Veículo na Tabela FIPE

![image](https://github.com/yuremartins/Projeto-de-Rentabilidade-Pricing/blob/main/notebooks/PrtSc/Resultado%20da%20Consulta.png?raw=true)

````
def consulta_veiculo(request):
    if request.method == 'POST':
        form = forms.VeiculoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            valor_veiculo = consultar_valor_veiculo(data)
            if valor_veiculo:
                return render(request, 'resultado_consulta.html', {'valor_veiculo': valor_veiculo})
    else:
        form = forms.VeiculoForm()
    
    return render(request, 'consulta_veiculo.html', {'form': form})
````
> Este script contém a função `consulta_veiculo`, que consulta os detalhes de um veículo específico na Tabela FIPE, incluindo o valor de compra.

## Calculadora de Rentabilidade

![image](https://github.com/yuremartins/Projeto-de-Rentabilidade-Pricing/blob/main/notebooks/PrtSc/Valor%20do%20Ve%C3%ADculo.png?raw=true)

````
def mostrar_valor(request):
    valor_veiculo = request.GET.get('valor')
    return render(request, 'mostrar_valor.html', {'valor_veiculo': valor_veiculo})
````

````
def processar_prazo(request):
    if request.method == 'POST':
        prazo_contrato = request.POST.get('prazo_contrato')
        valor_veiculo = request.POST.get('valor_veiculo')
        segmento_nome = request.POST.get('segmento') 
        
        valor_veiculo = ''.join(filter(str.isdigit, valor_veiculo))

        valor_veiculo = valor_veiculo[:-2]

        prazo_locacao = int(prazo_contrato)

        taxa_lucro = 0.10

        valor_compra = float(valor_veiculo.replace("R$", ""))

        # Dicionário de taxas de depreciação por segmento
        taxas_depreciacao = {
            "agro": 0.25,
            "energia": 0.36,
            "engenharia": 0.29,
            "mineracao": 0.50,
            "outros": 0.24
        }

        if segmento_nome in taxas_depreciacao:
            taxa_depreciacao_desejada = taxas_depreciacao[segmento_nome]
        else:
            print("Segmento não encontrado nas taxas de depreciação. Usando taxa padrão de 0.20.")
            taxa_depreciacao_desejada = 0.20

        valor_locacao_necessario, valor_venda, rental_rate, faturamento_total, taxa_depreciacao_atualizada, valor_depreciado = calcular_valor_locacao(valor_compra, taxa_depreciacao_desejada, taxa_lucro, prazo_locacao)

        taxa_depreciacao_percentual = taxa_depreciacao_atualizada * 100

        return render(request, 'resultado_processamento.html', {
            'valor_veiculo': valor_veiculo,
            'prazo_contrato': prazo_contrato,
            'valor_locacao_necessario': valor_locacao_necessario,
            'valor_venda': valor_venda,
            'rental_rate': rental_rate,
            'faturamento_total': faturamento_total,
            'taxa_depreciacao_atualizada': taxa_depreciacao_atualizada,
            'taxa_depreciacao_percentual': taxa_depreciacao_percentual,
            'valor_depreciado': valor_depreciado,
            'segmento': segmento_nome
        })
````
## Resultado do Processamento

![image](https://github.com/yuremartins/Projeto-de-Rentabilidade-Pricing/blob/main/notebooks/PrtSc/Resultado%20do%20Processamento.png?raw=true)

````
def calcular_valor_locacao(valor_compra, taxa_depreciacao_desejada, taxa_lucro_desejada, prazo_locacao_desejado):
    
    semestres_extras = prazo_locacao_desejado / 6

    taxa_depreciacao_atualizada = taxa_depreciacao_desejada + (semestres_extras * 0.005)

    valor_depreciado = valor_compra * taxa_depreciacao_atualizada

    valor_venda = valor_compra - (valor_compra * taxa_depreciacao_atualizada)

    valor_locacao_necessario = ((valor_compra + (valor_compra * taxa_lucro_desejada)) - valor_venda) / prazo_locacao_desejado

    rental_rate = (valor_locacao_necessario / valor_compra) * 100

    faturamento_total = (valor_locacao_necessario * prazo_locacao_desejado) + valor_venda

    return round(valor_locacao_necessario, 2), round(valor_venda, 2), round(rental_rate, 2), round(faturamento_total, 2), round(taxa_depreciacao_atualizada, 2), round(valor_depreciado, 2)

````
> Este script contém a função `calcular_valor_locacao` é utilizada para calcular o valor de locação do veículo com base nos dados obtidos na consulta.
