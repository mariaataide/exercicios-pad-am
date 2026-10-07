#  1. Para cada bolsa, calcule dois indicadores: o retorno médio (em %)
#  e a amplitude do período (valor máximo menos o mínimo — uma medida
#  simples de "o quanto a bolsa oscilou").

# Carrega as bibliotecas
from statsmodels import datasets
import pandas as pd

# Carrega as cotações das 4 bolsas europeias
indices = datasets.get_rdataset("EuStockMarkets").data

def indicador(coluna, indicador = "amplitude"):
    if indicador == "amplitude":
        ind = round(float(coluna.max() - coluna.min()), 2)
    if indicador == "retorno":
        ind = round(coluna.pct_change().mean() * 100, 2)

    return ind

a = {}
r = {}

for col in indices.columns:
    a[col] = indicador(indices[col], indicador="amplitude")
    r[col] = indicador(indices[col], indicador="retorno")

print("Amplitude:", a)
print("Retorno:", r)

# 2. Monte um DataFrame-resumo com uma linha por bolsa e as colunas
#  retorno e amplitude. 

indicadores_df = pd.DataFrame([a, r])
indicadores_df.index = {"Amplitude": 0, "Retorno": 1}
    
# 3. Escreva uma função que, dado o retorno, devolva uma recomendação

## Critérios:
## Amplitude < 4000 and Retorno > 0.05 -> comprar
## Amplitude < 4000 and Retorno == 0.05 -> manter
## Amplitude > 4000 -> vender

def recomendacao(col):
    if float(indicadores_df.loc["Amplitude", col]) < 4000 and float(indicadores_df.loc["Retorno", col]) > 0.05:
        return "Comprar"
    elif float(indicadores_df.loc["Amplitude", col]) < 4000 and float(indicadores_df.loc["Retorno", col]) == 0.05:
        return "Manter"
    else:
        return "Vender"

recomendacao_dict = {}

for coluna in indicadores_df.columns:
    recomendacao_dict[coluna] = recomendacao(coluna)

print(recomendacao_dict)

# 4. Descubra e imprima qual bolsa teve o maior retorno do período 
# (sem usar métodos que você ainda não viu — dá para achar com um 
# for e comparações, guardando o líder numa variável).

retorno = {}

for col in indices.columns:
    retorno[col] = indicador(coluna=indices[col], indicador="retorno")

print(retorno)

maior_retorno = "" # vazio
maior = -1

for col in retorno:
    if retorno[col] > maior:
        maior = retorno[col]
        maior_retorno = col

print("Bolsa mais volátil: ", maior_retorno, "Volatilidade: ", maior)

