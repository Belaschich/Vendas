""" 
Projeto Trade Marketing
Executor: Izabela Schich
Data: 20/02/2026
"""

# %% Biblioteca
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %% Lendo o arquivo
df = pd.read_csv("customer_shopping_data.csv")
print(df.head())

# %% Verificando os tipos de coluna
print(df.info())
print(df.describe())

# %% Convertendo colunas necessárias
df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True)
print(df.info())

# %% Criando colunas de Datas
df["Ano"] = df["invoice_date"].dt.year
df["Mes"] = df["invoice_date"].dt.month
df["Mes_Nome"] = df["invoice_date"].dt.month_name()


# %% Verificando Na / Null nas colunas
print(df.isna().sum())


# %% KPIS
df["Faturamento_total"] = df["quantity"] * df["price"].round(2)
Faturamento_Total = df["Faturamento_total"].sum().round(2) #Faturamento Total
qtd_venda = df["quantity"].sum().round(2) # Quantidade de produtos vendidos
Ticket_Medio = (Faturamento_Total/qtd_venda).round(2) # Ticket Medio
# %%Faturamento por Shopping
Faturamento_shopping = df.groupby("shopping_mall")["Faturamento_total"].sum().sort_values(ascending=False).round(2)

# %% Quantidade Vendida  na Shopping
Qtd_venda_Shopping = df.groupby("shopping_mall")["quantity"].sum().sort_values(ascending=False)

#Qtd_venda_Shopping.plot(kind="bar")
#plt.show()

# %% Ticket medio por Shopping
Ticket_Medio_Shopping =(Faturamento_shopping/Qtd_venda_Shopping).round(2)

df["Ticket_Medio_Shopping"] = df["Ticket_Medio_Shopping"] = df["shopping_mall"].map(Ticket_Medio_Shopping)
# Criando a clusterização das lojas

CD = (Ticket_Medio*0.75).round(2)
BC = (Ticket_Medio*1).round(2)

def classificar(ticket):
    if ticket <= CD:
        return "CD"
    elif ticket > CD and ticket <= BC:
        return "BC"
    else:
        return "AB"

df["Classificacao_Shopping"] = df["Ticket_Medio_Shopping"] .apply(classificar)

# %% Segmentação por idade
df["Grupo_Idade"] = pd.cut(
    df["age"],
    bins=[0, 18, 25, 35, 45, 60, 100],
    labels=["0-18", "19-25", "26-35", "36-45", "46-60", "60+"]
)
df["Faturamento_Grupo_Idade"] = (df.groupby("Grupo_Idade")["Faturamento_total"].transform("sum")).round(2)
df["Qtd_venda_Grupo_Idade"] = (df.groupby("Grupo_Idade")["quantity"].transform("sum")).round(2)
df["Ticket_medio_Grupo_Idade"] = (df["Faturamento_Grupo_Idade"]/df["Qtd_venda_Grupo_Idade"] ).round(2)

#%% Renomeando as Linhas
df["gender"].unique()
df["gender"] = df["gender"].replace({
    "Female": "Feminino",
    "Male": "Masculino"
})

df["category"].unique()
df["category"] = df["category"].replace({
    "Clothing": "Roupas",
    "Shoes": "Sapatos",
    "Books": "Livros",
    "Cosmetics": "Cosmeticos",
    "Food & Beverage": "Alimentacao",
    "Toys": "Brinquedos",
    "Technology": "Tecnologia",
    "Souvenir": "Souvenir"
})

df["payment_method"].unique()
df["payment_method"] = df["payment_method"].replace({
    "Credit Card": "Cartao de Credito",
    "Debit Card": "Cartao de Debito",
    "Cash": "Dinheiro"
})

df["Mes_Nome"].unique()
df["Mes_Nome"] = df["Mes_Nome"].replace({
    
    "January":"Janeiro",
    "February":"Fevereiro",
    "March":"Marco",
    "April":"Abril",
    "May":"Maio",
    "June":"Junho",
    "July":"Julho",
    "August": "Agosto",
    "September":"Setembro",
    "October":"Outubro",
    "November": "Novembro",
    "December": "Dezembro"
})

# %% Renomeando Colunas

df.rename(columns={
    "invoice_no": "Numero_Nota",
    "customer_id": "ID_Cliente",
    "gender": "Genero",
    "age": "Idade",
    "category": "Categoria",
    "quantity": "Quantidade",
    "price": "Preco",
    "payment_method": "Forma_Pagamento",
    "invoice_date": "Data_Venda",
    "shopping_mall": "Shopping",
    "price":"Preco"
}, inplace=True)

# %% Criando a tabela
df = df[[
    "Data_Venda",
    "Numero_Nota",
    "ID_Cliente",
    "Genero",
    "Idade",
    "Categoria",
    "Quantidade",
    "Preco",
    "Faturamento_total",
    "Forma_Pagamento",
    "Shopping",
    "Classificacao_Shopping",
    "Ticket_Medio_Shopping",
    "Grupo_Idade",
    "Faturamento_Grupo_Idade",
    "Qtd_venda_Grupo_Idade",
    "Ticket_medio_Grupo_Idade",
    "Ano",
    "Mes",
    "Mes_Nome"
]]
# %% Visualização

df.groupby("Categoria")["Preco"].sum().plot(kind="bar")
plt.show()

# %% Salvar o arquivo em csv para usar no power bi

df.to_csv("Sales.csv", index=False)
print("Fim!")
# %%
