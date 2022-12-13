from openpyxl import load_workbook
import os


def ler_pasta():
    pasta_provisoes = load_workbook('plan_provisoes.xlsx')
    planilha = pasta_provisoes.active

    for linha in planilha.values:
        print(linha[0])


if __name__ == '__main__':
    dados_funcionario = ler_pasta()
    # ler_pasta()
    print(dados_funcionario)
    # data = dados_funcionario.get('NASCIMENTO')[0:10].split('-')
    # nova_data = data[2] + data[1] + data[0]
    # print(nova_data)
