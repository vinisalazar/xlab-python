"""
Um script Python para automatizar algum processo
"""

from glob import glob
import pandas as pd

planilhas = glob("*.xlsx")


def processar_planilhas(nome_do_arquivo):
    """
    Calcula o número de linhas e colunas na planilha.
    """
    print("Importando", nome_do_arquivo)
    df = pd.read_excel(nome_do_arquivo)
    
    print(nome_do_arquivo, "tem", df.shape[0], "linhas.")
    print(nome_do_arquivo, "tem", df.shape[1], "colunas.")
    print("Finalizado para", nome_do_arquivo)
    
    
print("Processando", len(planilhas), "arquivos.")
for arquivo in planilhas:
    processar_planilhas(arquivo)

    
print("Finalizado para todos os arquivos.")
