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


# --------------------------------------------
# Cria a variável cromos_brilhantes, que junta os escudos de seleções e os cromos_especiais em uma variável
# --------------------------------------------

escudos = [f'{selecao}1' for selecao in selecoes]

cromos_brilhantes = cromos_especiais + escudos

# --------------------------------------------
# album junta os cromos especiais e normais
# --------------------------------------------

album = cromos_especiais + cromos_selecoes

# print(len(album)) --> Mostra o total de cromos criados (980)