import streamlit as st
from core import CalculadoraIpi
from components.layout import configure_page, inject_custom_css
from components.outputs import display_header, display_kpi_cards, display_chart, display_table

def main():
    # 1. Configurações básicas e CSS
    configure_page()
    inject_custom_css()
    
    # 2. Cabeçalho
    display_header()
    
    # 3. Painel lateral para entrada de dados
    st.sidebar.markdown("### 📥 Entrada de Dados")
    
    # Rótulo atualizado para representar o cálculo reverso (Com IPI)
    valor_total = st.sidebar.number_input(
        "Valor Total da Nota (Com IPI) (R$)",
        min_value=0.0,
        value=1000.0,
        step=50.0,
        format="%.2f",
        help="Digite o preço total contendo o valor do material e o imposto."
    )
    
    aliquota = st.sidebar.number_input(
        "Alíquota do IPI (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.5,
        format="%.2f",
        help="Digite a alíquota de IPI utilizada para o cálculo reverso."
    )
    
    st.sidebar.info(
        "💡 Os valores são atualizados automaticamente a cada alteração nos campos acima."
    )
    
    # 4. Instancia a classe CalculadoraIpi que você desenvolveu e faz as contas
    calc = CalculadoraIpi(valor_total, aliquota)
    results = calc.para_dicionario()
    
    # 5. Exibe os cartões com os resultados
    display_kpi_cards(results)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Divide a tela inferior: Gráfico e Tabela
    col_chart, col_table = st.columns([1, 1])
    
    with col_chart:
        display_chart(results)
        
    with col_table:
        st.subheader("Detalhamento da Consulta")
        display_table(results)

if __name__ == "__main__":
    main()