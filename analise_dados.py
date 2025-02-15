import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv("supermarket_sales - Sheet1.csv")

# Exibir informações básicas
print(df.info())
print("\nResumo estatístico:")
print(df.describe())

# 🚀 Receita total
receita_total = df["cogs"].sum()
print(f"\n💰 Receita total: ${receita_total:,.2f}")

# 📊 Método de pagamento mais comum
pagamento_mais_usado = df["Payment"].value_counts()
print("\n💳 Métodos de pagamento mais usados:")
print(pagamento_mais_usado)

# ⭐ Média de avaliação dos clientes
media_rating = df["Rating"].mean()
print(f"\n⭐ Média de satisfação dos clientes: {media_rating:.2f}")

# 🌍 Faturamento por cidade
faturamento_por_cidade = df.groupby("City")["cogs"].sum()
print("\n🏙️ Faturamento por cidade:")
print(faturamento_por_cidade)

# 🔥 Gráfico: Métodos de pagamento
plt.figure(figsize=(6, 4))
sns.barplot(x=pagamento_mais_usado.index, y=pagamento_mais_usado.values, palette="viridis")
plt.title("💳 Métodos de Pagamento Mais Utilizados")
plt.xlabel("Método de Pagamento")
plt.ylabel("Quantidade de Transações")
plt.show()

# 🌍 Gráfico: Faturamento por cidade
plt.figure(figsize=(6, 4))
sns.barplot(x=faturamento_por_cidade.index, y=faturamento_por_cidade.values, palette="coolwarm")
plt.title("🏙️ Faturamento por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Faturamento ($)")
plt.show()
