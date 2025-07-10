# %%
import pandas as pd
import streamlit as st
import joblib

st.set_page_config(page_title="Previsão Airbnb", page_icon="🏠", layout="centered")

st.title("🏠 Previsão de Valor de Imóvel - Airbnb")
st.markdown("---")

# Dicionários iniciais
x_numericos = {
    'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 
    'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 
    'ano': 0, 'mes': 0, 'numero_amenities': 0, 'host_listings_count': 0
}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {
    'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
    'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
    'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
}

dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0

st.subheader("📍 Informações de Localização e Detalhes do Imóvel")
# Inputs numéricos
for item in x_numericos:
    if item in ['latitude', 'longitude']:
        valor = st.number_input(f'{item.title()}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item.replace("_", " ").title()}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item.replace("_", " ").title()}', value=0)
    x_numericos[item] = valor

st.markdown("---")
st.subheader("✅ Configurações Adicionais")

# Inputs True/False
for item in x_tf:
    valor = st.selectbox(f'{item.replace("_", " ").title()}', ('Sim', 'Não'))
    x_tf[item] = 1 if valor == 'Sim' else 0

# Inputs de listas
for item in x_listas:
    valor = st.selectbox(f'{item.replace("_", " ").title()}', x_listas[item])
    for v in x_listas[item]:
        dicionario[f'{item}_{v}'] = 1 if v == valor else 0

st.markdown("---")
with st.expander("ℹ️ Ver tradução das categorias"):
    st.markdown("""
    | Categoria | Opções em inglês | Tradução pt-br |
    |---|---|---|
    | **Tipo de Propriedade** | Apartment | Apartamento |
    |  | Bed and breakfast | Pousada |
    |  | Condominium | Condomínio |
    |  | Guest suite | Suíte para hóspedes |
    |  | Guesthouse | Casa de hóspedes |
    |  | Hostel | Hostel |
    |  | House | Casa |
    |  | Loft | Loft |
    |  | Outros | Outros |
    |  | Serviced apartment | Apartamento com serviço |
    | **Tipo de Quarto** | Entire home/apt | Imóvel inteiro |
    |  | Hotel room | Quarto de hotel |
    |  | Private room | Quarto privativo |
    |  | Shared room | Quarto compartilhado |
    | **Política de Cancelamento** | flexible | Flexível |
    |  | moderate | Moderada |
    |  | strict | Rígida |
    |  | strict_14_with_grace_period | Rígida com 14 dias de carência |
    | **Outros** | host_is_superhost | É superhost |
    |  | instant_bookable | Reserva instantânea |
    |  | amenities | Comodidades |
    """)


# Botão para prever
botao = st.button('🔮 Prever valor do imóvel')

if botao:
    with st.spinner('Calculando previsão...'):
        dicionario.update(x_numericos)
        dicionario.update(x_tf)
        valores_x = pd.DataFrame(dicionario, index=[0])

        dados = pd.read_csv('dados.csv')
        colunas = list(dados.columns)[1:-1]
        valores_x = valores_x[colunas]

        modelo = joblib.load('modelo.joblib')
        preco = modelo.predict(valores_x)

    st.success(f"💰 Valor estimado do imóvel: **R$ {preco[0]:,.2f}**")


# %%



