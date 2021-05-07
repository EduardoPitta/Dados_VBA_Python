import csv
import pandas as pd


#Função para calculo de média ponderada
def calc_media(prices,ammount):
    acima=0
    baixo=0
    i=0
    if ammount != []:
        while i<len(prices):
            acima = acima + (prices[i]*ammount[i])
            baixo = baixo + ammount[i]
            i=i+1
        return acima/baixo
    else:
        return 0

#Lê o arquivo da base de dados
df = pd.read_csv('c:/Users/eduar/OneDrive/Área de Trabalho/kapitalo/Banco.csv')

#aqui armazenamos os valores únicos para Brokers e Produtos
brokers = df.Broker.unique()
produtos = df.Produto.unique()

#Criamos uma nova data frame com as informações do relatório
relatorio = pd.DataFrame(columns = ['Broker','Produto','Media Ponderada'])

#Para cada Broker unico
for broker in brokers:
    #Faremos uma lista com os indices de todas as movimentaçoes
    index_broker = list(df.loc[df['Broker'] == broker].index)
    #Para cada produto unico
    for produto in produtos:
        prices = []
        quantities = []
        #Faremos uma lista dos indices de cada ocorrencia deles
        index_produto = list(df.loc[df['Produto'] == produto].index)
        #Se o indice existir em ambas as listas, quer dizer que o broker operou com este produto, os valores de quatidade e preco vão ser armazenados nas listas prices e quantities
        #Caso ele nã otenha operado a função de calculo de media vai retornar 0
        for item in index_produto:
            if item in index_broker:
                prices.append(df.iloc[item]['Price'])
                quantities.append(df.iloc[item]['Qty'])
        #Calculo da média para o produto atual
        media = calc_media(prices,quantities)
        #Dados que vão ser colocados na datafrade do relatório
        row={'Broker':broker, 'Produto':produto, 'Media Ponderada':"{:,.2f}".format(media)}
        #Coloca linha na dataframe
        relatorio = relatorio.append(row,ignore_index=True)

print(relatorio)
relatorio.to_excel('c:/Users/eduar/OneDrive/Área de Trabalho/kapitalo/Relatorio.xlsx', index=False)
        
