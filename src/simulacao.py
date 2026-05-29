from album import album
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
    repetidas = 0

    while len(colecao) < len(album):
        pacotes_comprados += 1
        pacote = random.choices(album, k= FIGURINHAS_POR_PACOTE)

        for figurinha in pacote:
            if figurinha in colecao:
                repetidas += 1
            colecao.add(figurinha)

    custo_total = (pacotes_comprados * PRECO_PACOTE) + PRECO_ALBUM  

    return pacotes_comprados, repetidas, colecao, custo_total


if __name__ == "__main__":

    pacotes_comprados, repetidas, colecao, custo_total = Simular_Album()

    print("=" * 40)
    print("RESULTADO DA SIMULAÇÃO")
    print("=" * 40)

    print(f"Pacotes comprados: {pacotes_comprados}")
    print(f"Figurinhas encontradas: {len(colecao)}")
    print(f"Figurinhas repetidas: {repetidas}")
    print(f"Custo total: R$ {custo_total:.2f}")

    print("=" * 40)