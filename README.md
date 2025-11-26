# Análise de Vendas de Micro Empresa — Insights Exploratórios

Análise exploratória de aproximadamente 4.800 vendas reais de uma pequena loja.  
O objetivo é entender padrões básicos, como quais produtos mais vendem, como as vendas se comportam ao longo de semanas e meses, quais formas de pagamento são mais usadas e como datas sazonais afetam a loja.  
O projeto foi inspirado na disciplina de “Métodos e Técnicas de Pesquisa para Computação” da minha faculdade, que escolhi explorar o tema “A aplicação da análise de dados e da modelagem preditiva como apoio à tomada de decisão em pequenas empresas”.

A ideia só foi possível graças ao acesso a um relatório real de vendas da loja, permitindo que a análise fosse feita com dados reais em vez de um dataset sintético, servindo de embasamento tanto pro meu projeto de pesquisa e um bom projeto pro meu github

---

## Visão Geral

Os dados originais precisaram ser divididos em quatro arquivos Excel (por limitações do software e do computador local), cada um com formatação inconsistente. O primeiro passo foi limpar e organizar tudo em um único CSV final.
Depois disso, o foco foi explorar os dados e gerar insights que realmente ajudassem um pequeno negócio a entender seu próprio comportamento de vendas.

---

## Estrutura

- [`01_preparation`](https://github.com/ocaiosilv/smallshop-sales-EDA/tree/main/01_preparation) → limpeza, padronização e correção de inconsistências  
- [`02_EDA.ipynb`](https://github.com/ocaiosilv/smallshop-sales-EDA/blob/main/02_EDA.ipynb) → análise exploratória de dados (EDA)  
- [`total_sales.csv`](https://github.com/ocaiosilv/smallshop-sales-EDA/blob/main/Sales_Data/total_vendas.csv) → dataset final usado na análise

---

## O Que Foi Feito

- Limpeza e unificação dos quatro relatórios exportados do sistema da loja.  
- Correção de valores ausentes e padronização de etiquetas.  
- Identificação de itens incomuns (produtos de teste, erros de registro etc.).  
- Exploração de frequência de vendas, rotação de produtos e efeitos sazonais.  
- Análise de distribuições (quartis, mediana).  
- Observação das vendas semanais e mensais.  
- Identificação dos produtos mais vendidos e dos que mais geraram receita.  
- Análise da distribuição das formas de pagamento.

---

## Insights

- **Há muitos produtos únicos**, mas muitos foram vendidos apenas uma vez — indicando baixa rotação ou itens que não devem ser comprados em grande quantidade.  
- A semana do **Dia das Crianças** (dia 6 a 12 de outubro) foi o maior pico do ano — quase *5×* a média semanal — provavelmente porque a loja fica ao lado de duas escolas.  
- **Outras datas comemorativas** (Dia das Mães, dos Pais, Páscoa) pouco afetaram o volume de vendas.
- As primeiras semanas têm volume baixo devido à adaptação ao sistema

  
  ![Gráfico semanal de vendas](https://github.com/user-attachments/assets/8b3cbeab-9ce2-42c2-b9b5-bff55fe31165)

  
- **O valor médio por venda é baixo**, compatível com os produtos da loja.  
- **Mediana é próxima da média**, indicando estabilidade no valor gasto por cliente.  
- **PIX é, de longe, a forma de pagamento mais usada**.

  
  ![Gráfico das formas de pagamento](https://github.com/user-attachments/assets/4924edb7-73b5-4d61-b4ce-548b5030d0d5)

---

## Ferramentas Utilizadas

- Python  
- Pandas  
- Matplotlib  
- Jupyter Notebook

