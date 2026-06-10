from simulacao import Simular_Album

# ============================================
# RODANDO 1.000 SIMULAÇÕES
# ============================================

N_SIMULACOES = 1000

resultados_pacotes = []  # Resultado das qtde de pacotes necessários para completar o álbum em cada simulação
resultados_custos = []  # Resultado do valor necessário para completar o álbum em cada simulação

resultados_repetidas_totais = []
resultados_repetidas_normais = []
resultados_repetidas_brilhantes = []

for i in range(N_SIMULACOES):

    pacotes_comprados, repetidas_total, repetidas_normais, repetidas_brilhantes, colecao, custo_total = Simular_Album()

    resultados_pacotes.append(pacotes_comprados)
    resultados_custos.append(custo_total)

    resultados_repetidas_totais.append(repetidas_total)
    resultados_repetidas_normais.append(repetidas_normais)
    resultados_repetidas_brilhantes.append(repetidas_brilhantes)

# ============================================
# ANÁLISE DOS RESULTADOS
# ============================================

media_pacotes = sum(resultados_pacotes) / N_SIMULACOES

media_custo = sum(resultados_custos) / N_SIMULACOES

media_repetidas = sum(resultados_repetidas_totais) / N_SIMULACOES

media_repetidas_normais = sum(resultados_repetidas_normais) / N_SIMULACOES

media_repetidas_brilhantes = sum(resultados_repetidas_brilhantes) / N_SIMULACOES







