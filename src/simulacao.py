from album import album, cromos_brilhantes
import random

# ============================================
# DEFININDO DADOS DE PACOTES E ALBUM
# ============================================

PRECO_PACOTE = 7
FIGURINHAS_POR_PACOTE = 7
PRECO_ALBUM = 75

# ============================================
# CRIANDO FUNÇÃO PARA SIMULAR O ÁLBUM COMPLETO
# ============================================

def Simular_Album():

    colecao = set()

    pacotes_comprados = 0

    repetidas_normais = 0
    repetidas_brilhantes = 0


    while len(colecao) < len(album):
        pacotes_comprados += 1
        pacote = random.choices(album, k= FIGURINHAS_POR_PACOTE)

        for figurinha in pacote:
            if figurinha in colecao:

                if figurinha in cromos_brilhantes:
                    repetidas_brilhantes += 1
                else:
                    repetidas_normais += 1

            colecao.add(figurinha)

    repetidas_total = repetidas_normais + repetidas_brilhantes
    custo_total = (pacotes_comprados * PRECO_PACOTE) + PRECO_ALBUM  

    return pacotes_comprados, repetidas_total, repetidas_normais, repetidas_brilhantes, colecao, custo_total


# ============================================
# MOSTRA UMA SIMULAÇÃO, APENAS QUANDO RODAR NESSE ARQUIVO
# ============================================


if __name__ == "__main__":

    pacotes_comprados, repetidas_total, repetidas_normais, repetidas_brilhantes, colecao, custo_total = Simular_Album()

    print("=" * 40)
    print("RESULTADO DA SIMULAÇÃO")
    print("=" * 40)

    print(f"Pacotes comprados: {pacotes_comprados}")
    print(f"Figurinhas encontradas: {len(colecao)} \n")

    print(f"Repetidas totais: {repetidas_total}")
    print(f"Repetidas normais: {repetidas_normais}")
    print(f"Repetidas brilhantes: {repetidas_brilhantes}")

    print(f"Custo total: R$ {custo_total:.2f}")

    print("=" * 40)