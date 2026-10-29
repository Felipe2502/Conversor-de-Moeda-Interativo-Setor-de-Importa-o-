# 5
print("####### Exercício 5:")

def converter_para_real(valor_em_dolares, cotacao_dolar):
    valor_em_real = valor_em_dolares * cotacao_dolar
    return valor_em_real

def processar_lista_precos(lista_precos_dolar, cotacao_dolar):
    for item in lista_precos_dolar:
        valor_reais = converter_para_real(item, cotacao_dolar)
    print(f"O item custa US${item} e em reais: R${valor_reais}")

precos_usd = [100, 50, 250]
cotacao_dolar = 5.20

processar_lista_precos(precos_usd, cotacao_dolar)