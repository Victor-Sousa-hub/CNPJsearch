import pandas as pd
import json

# Carregar o arquivo Excel
xlsx_file = "Enquadramento.xlsx"  # Substitua pelo caminho do arquivo
output_json = "enquadramento.json"  # Arquivo de saída

try:
    # Ler a primeira aba do Excel
    df = pd.read_excel(xlsx_file)

    # Converter para JSON
    df.to_json(output_json, orient="records", force_ascii=False, indent=4)

    print(f"Arquivo JSON gerado com sucesso: {output_json}")
except Exception as e:
    print(f"Erro ao converter o arquivo: {e}")
