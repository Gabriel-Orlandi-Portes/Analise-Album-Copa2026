# --------------------------------------------
# FIGURINHAS ESPECIAIS
# --------------------------------------------
# Define cromos brilhantes, sem contar com os escudos, apenas as figurinhas 00 e FWC1 ao FWC 19.

cromos_especiais = ['00'] + [f'FWC{i}' for i in range(1, 20)]

# --------------------------------------------
# FIGURINHAS DAS SELEÇÕES
# --------------------------------------------
# Cria todas as seleções do álbum, organizadas de SIGLA1 até SIGLA20, sendo a número 1, brilhante
# Exemplo:
# BRA1 -> Escudo brilhante
# BRA2 -> Jogador normal
# ...
# BRA20

selecoes = [
    "MEX", "RSA", "KOR", "CZE", "CAN", "BIH",
    "QAT", "SUI", "BRA", "MAR", "HAI", "SCO", 
    "USA", "PAR", "AUS", "TUR", "GER", "CUW",
    "CIV", "ECU", "NED", "JPN", "SWE", "TUN",
    "BEL", "EGY", "IRN", "NZL", "ESP", "CPV",
    "KSA", "URU", "FRA", "SEN", "IRQ", "NOR",
    "ARG", "ALG", "AUT", "JOR", "POR", "COD",
    "UZB", "COL", "ENG", "CRO", "GHA", "PAN"
]


# --------------------------------------------
# GERAR FIGURINHAS DAS SELEÇÕES - 1 A 20
# --------------------------------------------

cromos_selecoes = []

for selecao in selecoes: 
    
    for numero in range(1, 21):
        figurinha = f'{selecao}{numero}'

        cromos_selecoes.append(figurinha)


# Cria uma lista contendo todas as figurinhas brilhantes do álbum:
# - 00
# - FWC1 até FWC19
# - Escudos das 48 seleções (SIGLA1)

escudos = [f'{selecao}1' for selecao in selecoes]

cromos_brilhantes = cromos_especiais + escudos


# --------------------------------------------
# album junta os cromos especiais e normais
# --------------------------------------------

album = cromos_especiais + cromos_selecoes


# --------------------------------------------
# TESTES LOCAIS
# --------------------------------------------

if __name__ == "__main__":

    print(f"Total de cromos: {len(album)}")
    print(f"Total de brilhantes (especiais e seleções): {len(cromos_brilhantes)}")
    print(f"Total de especiais: {len(cromos_especiais)}")

    print("\nPrimeiros 30 cromos:")
    print(album[:30])

    print("\nCromos brilhantes (especiais e seleções):")
    print(cromos_brilhantes)