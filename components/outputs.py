import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def display_header():
    st.markdown(
        """
        <div class="main-header">
            <h1>📊 Calculadora de IPI <span class="gradient-text">Premium</span></h1>
            <p>Consulte e compare instantaneamente os valores de materiais com e sem o Imposto sobre Produtos Industrializados.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_kpi_cards(results: dict):
    """
    Exibe cartões de resumo modernos usando HTML/CSS personalizado.
    """
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            f"""
            <div class="kpi-card card-without-ipi">
                <h3>Sem IPI</h3>
                <div class="kpi-value">R$ {results['total_sem_ipi']:,.2f}</div>
                <p class="kpi-label">Valor base do material</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown(
            f"""
            <div class="kpi-card card-ipi">
                <h3>Valor do IPI</h3>
                <div class="kpi-value value-ipi">R$ {results['ipi_valor']:,.2f}</div>
                <p class="kpi-label">Imposto ({results['ipi_porcentagem']:.2f}%)</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col3:
        st.markdown(
            f"""
            <div class="kpi-card card-with-ipi">
                <h3>Total com IPI</h3>
                <div class="kpi-value value-total">R$ {results['total_com_ipi']:,.2f}</div>
                <p class="kpi-label">Custo total da aquisição</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def display_chart(results: dict):
    """
    Cria um gráfico de rosca interativo usando Plotly.
    """
    labels = ['Valor Base do Material', 'Valor do IPI']
    values = [results['total_sem_ipi'], results['ipi_valor']]
    
    if sum(values) == 0:
        st.info("Insira valores maiores que zero para ver a composição gráfica.")
        return
        
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.6,
        marker=dict(colors=['#3B82F6', '#8B5CF6']),
        hoverinfo='label+percent+value',
        textinfo='percent',
        textfont_size=14
    )])
    
    fig.update_layout(
        title_text="Composição do Custo Total",
        title_font_color="#FAFAFA",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(
            font=dict(color="#94A3B8"),
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        margin=dict(t=50, b=50, l=10, r=10),
        height=320
    )
    
    st.plotly_chart(fig, use_container_width=True)

def display_table(results: dict):
    """
    Gera uma tabela limpa e permite baixar o CSV.
    """
    data = {
        "Descrição": ["Valor do Material (Sem IPI)", "Alíquota de IPI (%)", "Valor do IPI", "Valor Total (Com IPI)"],
        "Valor / Taxa": [
            f"R$ {results['total_sem_ipi']:,.2f}",
            f"{results['ipi_porcentagem']:.2f}%",
            f"R$ {results['ipi_valor']:,.2f}",
            f"R$ {results['total_com_ipi']:,.2f}"
        ]
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Criar dados para exportação de CSV
    csv_data = {
        "Descricao": ["Valor Material (Sem IPI)", "Aliquota IPI", "Valor IPI", "Valor Total (Com IPI)"],
        "Valor": [results['total_sem_ipi'], results['ipi_porcentagem'] / 100, results['ipi_valor'], results['total_com_ipi']]
    }
    csv_df = pd.DataFrame(csv_data)
    csv = csv_df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Baixar Detalhamento em CSV",
        data=csv,
        file_name="calculo_ipi.csv",
        mime="text/csv"
    )