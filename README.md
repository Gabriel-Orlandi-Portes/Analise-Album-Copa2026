# 📊 Análise Estatística do Álbum da Copa do Mundo 2026

## 📌 Objetivo

Este projeto tem como objetivo analisar, através de simulações e técnicas de análise de dados, o custo estimado para completar o álbum de figurinhas da Copa do Mundo 2026.

A proposta é utilizar Python para modelar a abertura de pacotes, acompanhar a evolução da coleção, calcular estatísticas e visualizar padrões relacionados ao comportamento da coleção.

---

# 🏆 Informações do Álbum

O álbum foi modelado considerando:

- Total de cromos: **980**
- Cromos normais: **912**
- Cromos brilhantes: **68**
- Figurinhas por pacote: **7**
- Preço por pacote: **R$ 7,00**
- Preço estimado do álbum capa dura: **R$ 75,00**

---

# ✨ Organização das Figurinhas

As figurinhas foram divididas em dois grupos:

## Cromos brilhantes

Incluem:

- Figurinha especial `00`
- Figurinhas `FWC1` até `FWC19`
- Escudos das seleções (`SIGLA1`)

Exemplo:

```
BRA1 → Escudo brilhante
BRA2 → Jogador normal
BRA3 → Jogador normal
BRA20 → Jogador normal
```

---

# ⚙️ Metodologia

A simulação funciona da seguinte forma:

1. O álbum completo é criado automaticamente através de listas.
2. Cada pacote possui 7 figurinhas aleatórias.
3. A coleção do usuário é armazenada utilizando `set()`.
4. O processo continua até completar todas as figurinhas.
5. Durante a simulação são registrados:

- Quantidade de pacotes necessários
- Custo total da coleção
- Quantidade de figurinhas repetidas
- Repetidas normais
- Repetidas brilhantes

---

# 📁 Estrutura do Projeto

```
📁 Analise-Album-Copa2026/
│
├── data/      
|     └── simulacoes.csv
|
├── notebooks/
|     
│
├── src/
|   ├── album.py
│   ├── simulacao.py
│   └── 1000_simulacoes.py
|
|
|
├── README.md
└── .gitignore

```

---

# 🧩 Arquivos do Projeto

## `album.py`

Responsável pela criação da estrutura do álbum.

Este arquivo gera:

- Figurinhas especiais
- Seleções
- Figurinhas normais
- Figurinhas brilhantes
- Álbum completo

Exemplo:

```python
album = cromos_especiais + cromos_selecoes
```

---

## `simulacao.py`

Responsável pela lógica da simulação.

A função principal:

```python
Simular_Album()
```

Realiza:

- Compra dos pacotes
- Sorteio das figurinhas
- Controle da coleção
- Contagem de repetidas
- Cálculo do custo final

Retorna:

- Pacotes comprados
- Repetidas totais
- Repetidas normais
- Repetidas brilhantes
- Coleção completa
- Custo total

---

## `1000_simulacoes.py`

Responsável por executar várias simulações automaticamente.

Quantidade atual:

```python
N_SIMULACOES = 1000
```

Cada execução gera novos dados contendo:

- Quantidade de pacotes necessários
- Custo final
- Quantidade de repetidas
- Separação entre repetidas normais e brilhantes

Os resultados são armazenados em:

```
data/simulacoes.csv
```

---

# 📊 Análise de Dados

Os dados gerados serão analisados utilizando:

- Pandas
- NumPy
- Matplotlib

As análises serão feitas no notebook:

```
notebooks/analise_album_copa2026.ipynb
```

Serão analisados:

- Média de pacotes necessários
- Distribuição dos custos
- Quantidade média de repetidas
- Comparação entre cromos normais e brilhantes
- Visualizações através de gráficos

---

# 🚀 Como executar o projeto

## 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## 2. Acesse a pasta

```bash
cd analise-album-copa2026
```

---

## 3. Instale as dependências

```bash
pip install pandas numpy matplotlib
```

---

## 4. Execute as simulações

Entre na pasta:

```bash
cd src
```

Execute:

```bash
python 1000_simulacoes.py
```

Após executar, o arquivo será atualizado:

```
data/simulacoes.csv
```

---

# 🧪 Exemplo de resultado

Uma simulação individual retorna:

```
RESULTADO DA SIMULAÇÃO

Pacotes comprados: XXX

Figurinhas encontradas: 980

Repetidas totais: XXX

Repetidas normais: XXX

Repetidas brilhantes: XXX

Custo total: R$ XXXX
```

---

# 📈 Próximas análises

O projeto pretende responder:

- Quantos pacotes são necessários em média para completar o álbum?
- Qual o custo médio da coleção?
- Quantas figurinhas repetidas aparecem?
- Quantas repetidas brilhantes aparecem?
- Como as trocas podem reduzir o custo?
- Qual o impacto de diferentes probabilidades de raridade?

---

# 🛠 Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git/GitHub

---

# 📌 Status do Projeto

🚧 Em desenvolvimento

Próximas etapas:

- [ ] Criar análises exploratórias no notebook
- [ ] Criar gráficos
- [ ] Analisar distribuição dos custos
- [ ] Estudar impacto das trocas
- [ ] Adicionar modelos de raridade
- [ ] Criar novas simulações

---

# 👨‍💻 Autor

Gabriel Orlandi

Projeto desenvolvido para estudo de:

- Python
- Simulações
- Análise de Dados
- Visualização de informações
