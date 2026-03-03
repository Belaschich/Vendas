# 📊 Retail Sales Analysis 

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo analisar a performance de vendas em shoppings centers, identificando:

📈 Shoppings com maior faturamento

🛍 Categorias mais lucrativas

💳 Forma de pagamento predominante

💰 Ticket médio geral e por segmento

👥 Perfil demográfico dos clientes

A proposta é simular um cenário real de negócio, aplicando técnicas de Python, SQL e Power BI para geração de insights estratégicos.

## 🛠 Ferramentas Utilizadas

🐍 Python (Pandas, Matplotlib)

🗄 SQL

📊 Power BI

📁 GitHub

## 📁 Base de Dados

A base utilizada contém informações de vendas no varejo com as seguintes colunas:

Coluna	                Descrição
invoice_no	            Número da fatura
customer_id	            Identificador do cliente
gender	                Gênero do cliente
age	                    Idade
category	            Categoria do produto
quantity	            Quantidade comprada
price	                Preço unitário
payment_method	        Forma de pagamento
invoice_date	        Data da venda
shopping_mall	        Shopping onde ocorreu a venda

## 🔎 Etapas do Projeto
### 1️⃣ Tratamento e Transformação de Dados (Python)

Criação da métrica de faturamento:

df["faturamento_total"] = df["quantity"] * df["price"]

Conversão da coluna de data

Criação de colunas de ano e mês

Segmentação por faixa etária

### 2️⃣ Análises Exploratórias

Principais análises realizadas:

Faturamento por Shopping

Faturamento por Categoria

Ticket Médio

Distribuição por Forma de Pagamento

Análise temporal de vendas

### 3️⃣ Análises em SQL

Exemplo de query utilizada:

SELECT 
    Shopping,
    SUM(Quantidade * Preco) AS faturamento
FROM sales
GROUP BY Shopping
ORDER BY faturamento DESC;

### Consultas aplicadas:

Faturamento por shopping

Ticket médio por categoria

Top 5 clientes

Performance por período

## 📊 Dashboard Power BI

O dashboard foi desenvolvido para fornecer uma visão executiva do negócio contendo:

### 🔹 KPIs:

Faturamento Total

Ticket Médio

Total de Vendas

### 🔹 Visualizações:

Barras → Faturamento por Shopping

Barras → Faturamento por Categoria

Pizza → Forma de Pagamento

Linha → Evolução do Faturamento Mensal

### 🔹 Segmentações:

Ano

Shopping

Categoria

O objetivo do dashboard é permitir análise interativa e suporte à tomada de decisão.

![Power Bi](https://github.com/user-attachments/assets/97c604a2-08f2-410d-9d77-5b660612bf06)

## 📌 Principais Insights
- Shopping com maior faturamento: Mall Of Istanbul
- Categoria mais lucrativa: Roupas
- Forma de pagamento predominante: Dinheiro
- Ticket médio: R$ 841,97

## 🚀 Conclusão

O projeto demonstra aplicação prática de:

✔ Limpeza e transformação de dados
✔ Construção de métricas de negócio
✔ SQL analítico
✔ Criação de dashboard executivo
✔ Storytelling com dados

Este projeto simula uma demanda real de mercado, onde o objetivo é transformar dados brutos em informações estratégicas.

## 📌 Próximos Passos

Implementar análise de segmentação de clientes

Criar clusterização por perfil de consumo

Publicar versão com deploy online do dashboard

Criar documentação técnica detalhada

## 👩‍💻 Sobre Mim

Sou profissional em transição para a área de Dados, com foco em Análise de Dados e Business Intelligence.
Estou desenvolvendo projetos práticos utilizando Python, SQL e Power BI.

📎 LinkedIn: https://www.linkedin.com/in/izabela-schich/
📎 Contato: izabela.schick@gmail.com

