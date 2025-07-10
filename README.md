# Airbnb Rio - Previsão de Preço de Imóvel

Este projeto contém um modelo de machine learning para prever o preço da diária de imóveis no Airbnb do Rio de Janeiro, além de uma aplicação Streamlit para facilitar o uso do modelo.

---

## Estrutura do Projeto

- `Solução Airbnb Rio.ipynb` — Notebook com a análise exploratória, limpeza dos dados, modelagem e avaliação.  
- `deploy.py` — Aplicação Streamlit para previsão interativa com inputs de usuário.  
- `modelo.joblib` — Modelo ExtraTrees treinado e salvo para uso no deploy.  
- `dados.csv` — Dados usados para garantir que as features estão alinhadas no deploy.

---

## Como usar

### Pré-requisitos

- Python 3.8+  
- Instalar dependências:

```bash
pip install streamlit pandas scikit-learn seaborn matplotlib plotly joblib
```
### Rodando a aplicação

No terminal, dentro da pasta do projeto, execute:

```bash
streamlit run deploy.py
```
A aplicação abrirá no navegador, onde você poderá preencher as informações do imóvel e obter a previsão de preço.

### Notas

- Certifique-se de que os arquivos `modelo.joblib` e `dados.csv` estão na mesma pasta do `deploy.py`.
- O modelo foi treinado com dados até maio de 2020; atualizações podem ser necessárias para novos dados.

### Contato

Lucas Amorim  
[LinkedIn](https://www.linkedin.com/in/lucas-amorim-powerbi/)

