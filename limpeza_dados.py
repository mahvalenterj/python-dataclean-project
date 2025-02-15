import pandas as pd

# Carregar o CSV original
df = pd.read_csv("supermarket_sales - Sheet1.csv")

# Remover valores nulos
df = df.dropna()

# Padronizar nomes das colunas (removendo espaços)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Converter colunas de datas, se houver
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

# Salvar o CSV limpo
df.to_csv("supermarket_sales_clean.csv", index=False)

print("Arquivo limpo salvo como 'supermarket_sales_clean.csv'")
