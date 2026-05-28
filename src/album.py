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
    "ARG", "BRA", "FRA", "GER",
    "USA", "MEX", "ESP", "POR",
    "ENG", "ITA", "NED", "BEL",
    "URU", "CRO", "JPN", "KOR",
    "SEN", "MAR", "CAN", "AUS",
    "SUI", "DEN", "POL", "SRB",
    "COL", "CHI", "PER", "ECU",
    "PAR", "BOL", "VEN", "CRC",
    "CMR", "GHA", "NGA", "EGY",
    "QAT", "SAU", "IRN", "IRQ",
    "UAE", "NZL", "SWE", "NOR",
    "UKR", "TUR", "COD", "ALG"
]

