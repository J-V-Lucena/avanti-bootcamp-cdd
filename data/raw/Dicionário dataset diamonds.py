import pandas as pd
import seaborn as sns

diamonds = sns.load_dataset("diamonds")

# Criando o dicionário com os dados do dataset

dicionario = pd.DataFrame([
    {
        "variavel": "carat",
        "descricao": "Peso do diamante em quilates",
        "tipo": "Quantitativa",
        "subtipo": "Contínua"
    },{
        "variavel": "cut",
        "descricao": "Qualidade do corte do diamante",
        "tipo": "Qualitativa",
        "subtipo": "Ordinal"
    },{
        "variavel": "color",
        "descricao": "Cor do diamante",
        "tipo": "Qualitativa",
        "subtipo": "Ordinal"
    },{
        "variavel": "clarity",
        "descricao": "Medida da clareza do diamante",
        "tipo": "Qualitativa",
        "subtipo": "Ordinal"
    },{
        "variavel": "depth",
        "descricao": "Profundidade total do diamante como proporção da largura",
        "tipo": "Quantitativa",
        "subtipo": "Contínua"
    },{
        "variavel": "table",
        "descricao": "Largura do topo do diamante em relação ao ponto mais largo",
        "tipo": "Quantitativa",
        "subtipo": "Contínua"
    },{
        "variavel": "price",
        "descricao": "Preço do diamante em dólares americanos",
        "tipo": "Quantitativa",
        "subtipo": "Contínua"
    },{
        "variavel": "x",
        "descricao": "Comprimento em milímetros",
        "tipo": "Quantitativa",
        "subtipo": "Contínua"
    },{
        "variavel": "y",
        "descricao": "Largura em milímetros",
        "tipo": "Quantitativa",
        "subtipo": "Contínua"
    },{
        "variavel": "z",
        "descricao": "Profundidade em milímetros",
        "tipo": "Quantitativa",
        "subtipo": "Contínua"
    }
])

print(dicionario)