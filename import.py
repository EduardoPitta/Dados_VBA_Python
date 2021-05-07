import pandas as pd
from csv import writer
file_path = "c:/Users/eduar/OneDrive/Área de Trabalho/kapitalo/Banco.csv"
df = pd.read_csv('c:/Users/eduar/OneDrive/Área de Trabalho/kapitalo/Dados.csv')

def append_list_as_row(path, list):
    with open(path, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list)
        
for index, row in df.iterrows():
    append_list_as_row(file_path, [ str(row['ID']), row['Broker'], row['Produto'], row['Product Type'], str(row['Compra/Venda']), str(row['Qty']), str(row['Price']), str(row['Account Number'])])

