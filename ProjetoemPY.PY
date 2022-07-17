import pandas as pd

#Lendo as planilhas
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';', encoding='utf-8')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';', encoding='utf-8')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';', encoding='utf-8')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';', encoding='utf-8')

display(vendas_df)
display(produtos_df)
display(lojas_df)
display(clientes_df)


#Juntando as 4 planilhas através do método .merge()
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

vendas_df = vendas_df.rename(columns={'Genero': 'Genero dos clientes'})

#Removendo colunas...
vendas_df = vendas_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)

display(vendas_df)


#Definindo quais colunas quero que fiquem no meu projeto.
vendas_df = vendas_df[['Nome da Loja', 'Data da Venda', 'Quantidade Vendida', 'Quantidade Devolvida', 'País', 'Genero dos clientes','ID Produto', 'Descricao do Produto']]
display(vendas_df)


#Informações de gênero de clientes na empresa
genero = vendas_df['Genero dos clientes'].value_counts()
genero_df = pd.DataFrame(data = genero)
my_colors = ['blue', 'orange']
genero_df.plot.pie(subplots = True, colors = my_colors, autopct='%.2f%%', figsize = (10, 5))
print('Como podemos ver, nossa clientela é mista, o que nos dá vantagem por ter uma abrangência maior do público num total.')


#Gráfico de barras com lojas que mais venderam na empresa
lojas_ranking = vendas_df.groupby('Nome da Loja').sum() 
lojas_ranking = lojas_ranking.sort_values('Quantidade Vendida', ascending = False)

lojas_ranking['Quantidade Vendida'][:10].plot.barh(figsize = (8, 5))
print('Ranking das nossas 10 Lojas que mais venderam no período analisado')
print('Parabéns à Loja Contoso Catalog pelo resultado de mais de um milhão de vendas')


#Gráfico pie mostrando de qual país vem a maior parte das vendas
faturamento_pais = vendas_df[['Nome da Loja', 'Quantidade Vendida', 'País']]
faturamento_pais = faturamento_pais.groupby('País').sum()
faturamento_pais = faturamento_pais.sort_values('Quantidade Vendida', ascending = False)
faturamento_pais[:5].plot.pie(subplots = True, figsize = (13, 7), autopct='%.2f%%')
print('Maior parte da receita provinda dos EUA')


#Quais os 5 produtos mais vendidos?
produto_ranking = vendas_df[['ID Produto', 'Descricao do Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]
produto_ranking = produto_ranking.groupby(by=['ID Produto']).sum()
produto_ranking = produto_ranking.sort_values(by='Quantidade Vendida', ascending = False)
produto_ranking[:10].plot.barh(figsize=(8,6), stacked = True)
print('índice baixíssimo de devoluções')


