import streamlit as st
import pandas as pd
import sqlite3


#conectar ao banco SQLite
conn = sqlite3.connect("../data/quotes.db")

#carregar os dados para um dataframe
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

#fechar conexão com o banco de dados
conn.close()

#titulo da aplicação
st.title("Pesquisa de Mercado - Tênis Esportivos no Mercado Livre")

st.write(df)
