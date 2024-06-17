import pandas as pd
import sqlite3
from datetime import datetime

#Definir o caminho para o arquivo JSONL
df = pd.read_json("../data/data.jsonl", lines=True)

#setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

#adicionar coluna _source com um valor fixo
df["_source"] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

# Adicionar a coluna _data_coleta com a data e hora atuais
df["_data_coleta"] = datetime.now()

#tratar os valores nulos para colunas numéricas e texto
df["old_price_reais"] = df["old_price_reais"].fillna(0).astype(float)
df["old_price_cents"] = df["old_price_cents"].fillna(0).astype(float)
df["new_price_reais"] = df["new_price_reais"].fillna(0).astype(float)
df["new_price_cents"] = df["new_price_cents"].fillna(0).astype(float)
df["reviews_rating_number"] = df["reviews_rating_number"].fillna(0).astype(float)

#
#remover parenteses do reviews_amount

df["reviews_amount"] = df["reviews_amount"].str.replace("[\(\)]", "", regex=True)
df["reviews_amount"] = df["reviews_amount"].fillna(0).astype(int)


#tratar os preços como float e calcular os totais gerais
df["old_price"] = df["old_price_reais"] + df["old_price_cents"] / 100
df["new_price"] = df["new_price_reais"] + df["new_price_cents"] / 100

#remover as colunas antigas de preço
df.drop(columns=['old_price_reais', 'old_price_cents', 'new_price_reais', 'new_price_cents'], inplace=True)

#conectar a um banco de dados SQLite ou cirar um novo
conn = sqlite3.connect("../data/quotes.db")

#salvar o DataFrame no banco de dados SQLite
df.to_sql("mercadolivre_items", conn, if_exists="replace", index=False)

#fechar conexão com banco de dados SQLite
conn.close()


print(df.head())