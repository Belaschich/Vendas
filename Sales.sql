--- Lendo a tabela
select * from sales

-- Faturamento Shopping
SELECT 
    Shopping,
    Round(sum(Faturamento_total),2) AS Faturamento
FROM sales
GROUP BY Shopping 
ORDER BY faturamento DESC;

-- Ticket Medio por Categoria

SELECT 
    Categoria,
    ROUND(SUM(Faturamento_total) / SUM(Quantidade), 2) AS ticket_medio
FROM sales
GROUP BY Categoria 
ORDER BY ticket_medio DESC;


-- Top 5 Clientes

SELECT 
    ID_Cliente ,
    SUM(Faturamento_total) AS total_gasto
FROM sales
GROUP BY ID_Cliente 
ORDER BY total_gasto DESC
LIMIT 5;

