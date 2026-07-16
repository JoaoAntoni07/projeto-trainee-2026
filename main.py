import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# configuração inicial da página web
st.set_page_config(page_title="Simulador House Prices", page_icon="🏡", layout="centered")

# Títulos e Textos na tela
st.title("🏡 Simulador de Preços de Imóveis")
st.write("""
Bem-vindo(a) ao simulador preditivo do House Prices! 
Ajuste as características no menu ao lado esquerdo para que a nossa Inteligência Artificial calcule o valor estimado da casa em tempo real.
""")

# Treinando o modelo 
# O @st.cache_data faz com que o Streamlit treine o modelo apenas 1 vez, deixando o site super rápido!
@st.cache_data
def carregar_e_treinar():
    # Carrega a base de treino original
    df = pd.read_csv('train.csv')
    
    # Selecionamos apenas as variáveis mais fortes para facilitar o simulador
    features = ['OverallQual', 'GrLivArea', 'GarageCars']
    
    # Removemos qualquer linha que tenha algum buraco nessas colunas
    df = df.dropna(subset=features + ['SalePrice'])
    
    X = df[features]
    y = np.log1p(df['SalePrice']) # Aplicamos o mesmo logaritmo do nosso projeto!
    
    # Treina a Regressão Linear
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    return modelo

# Executa a função para guardar o cérebro da IA na variável
modelo_ia = carregar_e_treinar()

# Criando o Menu Lateral (Sidebar) com os botões deslizantes
st.sidebar.header("Ajuste as Características")

qualidade = st.sidebar.slider(
    "Qualidade Geral (1 a 10)", 
    min_value=1, max_value=10, value=5, 
    help="1 = Muito Ruim, 10 = Excelente"
)

area = st.sidebar.number_input(
    "Área Habitável (sq ft)", 
    value=1500, step=50
)

# Variável de controle para sabermos se podemos fazer a previsão ou não
area_valida = True

# Checagem: Se a área for muito pequena ou muito grande, mostramos o erro
if area < 300 or area > 4000:
    st.sidebar.error("Valor inválido! Por favor, adicione uma área entre 300 e 4000 sq ft.")
    area_valida = False

carros_garagem = st.sidebar.slider(
    "Tamanho da Garagem (Nº de Carros)", 
    min_value=0, max_value=4, value=2
)

st.markdown("---") # Linha divisória
# Se a área NÃO for válida, o botão fica desabilitado
if st.button("Prever Preço da Casa", type="primary", disabled=not area_valida):
    
    escolhas_usuario = pd.DataFrame({
        'OverallQual': [qualidade],
        'GrLivArea': [area],
        'GarageCars': [carros_garagem]
    })
    # A máquina faz a previsão (em logaritmo)
    previsao_log = modelo_ia.predict(escolhas_usuario)[0]
    
    # Desfazemos o logaritmo para dólares
    previsao_dolar = np.expm1(previsao_log)
    
    # Exibimos o resultado com um efeito visual na tela
    st.success(f"O valor estimado para esta casa é de **${previsao_dolar:,.2f}**")
    st.balloons() # Solta balões na tela quando acerta!