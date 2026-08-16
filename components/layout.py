import streamlit as st

def configure_page():
    """
    Configura as opções básicas da página do Streamlit no navegador.
    """
    st.set_page_config(
        page_title="Calculadora de IPI Premium", # Nome que aparece na aba do navegador
        page_icon="📊",                         # Ícone da aba do navegador
        layout="wide",                          # Usa toda a largura da tela (melhor para gráficos)
        initial_sidebar_state="expanded"        # Deixa a barra lateral aberta por padrão
    )

def inject_custom_css():
    """
    Lê o nosso arquivo CSS personalizado e injeta ele na tela do Streamlit.
    """
    try:
        # Abre o arquivo de estilo que vamos criar na pasta assets
        with open("assets/style.css", "r", encoding="utf-8") as f:
            # st.markdown com unsafe_allow_html=True nos permite injetar código CSS na página
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # Se o arquivo de estilo ainda não existir, o app não quebra
        pass