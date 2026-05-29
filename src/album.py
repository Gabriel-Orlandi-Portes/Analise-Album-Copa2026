# --------------------------------------------
# FIGURINHAS BRILHANTES
# --------------------------------------------
# Define cromos brilhantes, sem contar com os escudos, apenas as figurinhas 00 e FWC1 ao FWC 19.

especiais = ['00'] + [f'FWC{i}' for i in range(1, 20)]


# --------------------------------------------
# FIGURINHAS NORMAIS
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
    "EUA", "PAR", "AUS", "TUR", "GER", "CUW",
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

