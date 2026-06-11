from simulacao import Simular_Album
import pandas as pd


N_SIMULACOES = 1000

# ============================================
# LISTA PARA ARMAZENAR RESULTADOS

resultados = []


# ============================================
# EXECUTANDO SIMULAÇÕES

for i in range(N_SIMULACOES):

    pacotes_comprados, repetidas_total, repetidas_normais, repetidas_brilhantes, colecao, custo_total = Simular_Album()


    resultados.append({

        "pacotes": pacotes_comprados,

        "custo": custo_total,

        "repetidas_total": repetidas_total,

        "repetidas_normais": repetidas_normais,

        "repetidas_brilhantes": repetidas_brilhantes

    })



# ============================================
# TRANSFORMANDO EM DATAFRAME

df = pd.DataFrame(resultados)



# ============================================
# EXPORTANDO CSV

df.to_csv(
    "../data/simulacoes.csv",
    index=False
)


print("=" * 40)
print("DADOS GERADOS")
print("=" * 40)

print(f"Simulações realizadas: {len(df)}")

print("Arquivo salvo com sucesso!")