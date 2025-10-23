# 🤖 Projeto de Data Science e Machine Learning

Projeto com notebooks usados para limpar, pré-processar, explorar e treinar modelos sobre o dataset "Spotify Top 2000".

Dataset original: [link para o Kaggle](https://www.kaggle.com/datasets/abdelrahman16/spotify-analysis-and-visualization)

Notebooks

- data_clean.ipynb — limpeza inicial e geração do CSV com os dados tratados.
- eda.ipynb — análise exploratória sobre o dataset limpo.
- pre_processing.ipynb — transformações detalhadas e preparação de features.
- model.ipynb — experimentos de modelagem / pipelines de recomendação e avaliação.

Datasets (gerados pelos notebooks)

- spotify_top_2000_songs.csv — raw (origem: Kaggle).
- data_clean.csv — dataset inicial limpo, utilizado em EDA e pré-processamento.
- pre_processing.csv — saída intermediária com features preparadas para modelagem.

Observações

- Execute os notebooks na ordem lógica (data_clean → pre_processing → eda → model) para regenerar os CSVs.
- Consulte os notebooks para detalhes das transformações e decisões de pré-processamento.

Licença / Fonte

- Dados provenientes do link do Kaggle (acima). Ver licença do repositório principal do projeto para termos de uso.
