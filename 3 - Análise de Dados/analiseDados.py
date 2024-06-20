import pandas as pd
import plotly.express as px

#Recebimento da planilha em Excel
dados = pd.read_excel("vendas.xlsx")


grafico = px.histogram(dados, x="loja",
                              y= "preco",
                              color= "forma_pagamento",
                              text_auto = True,
                              title = "Faturamento por Loja")
grafico.show()
