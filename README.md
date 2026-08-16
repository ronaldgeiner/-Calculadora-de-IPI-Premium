# 📊 Calculadora de IPI Premium

Este é um aplicativo interativo e moderno desenvolvido em **Python** utilizando o framework **Streamlit**. O objetivo principal do projeto é calcular e consultar de forma rápida o valor de um material considerando a incidência do **IPI (Imposto sobre Produtos Industrializados)**.

O design do aplicativo foi customizado para rodar em um **Tema Escuro (Dark Mode)** elegante e responsivo, ideal para apresentações e consultas corporativas.

---

## 🛠️ Tecnologias Utilizadas

*   **[Python](https://www.python.org/):** Linguagem de programação base do projeto.
*   **[Streamlit](https://streamlit.io/):** Framework para criação rápida de aplicativos web interativos em Python.
*   **[Plotly](https://plotly.com/python/):** Biblioteca para geração de gráficos interativos e dinâmicos.
*   **[Pandas](https://pandas.pydata.org/):** Biblioteca de manipulação de dados estruturados (usada para gerar a tabela e exportação de CSV).

---

## 📁 Arquitetura de Pastas do Projeto

O projeto foi estruturado seguindo boas práticas de desenvolvimento (Separação de Conceitos), dividindo a lógica matemática da parte visual:

```text
IPI_CALCULADORA/
├── .venv/                 # Pasta do Ambiente Virtual (isolamento de bibliotecas)
├── requirements.txt       # Lista de dependências/bibliotecas do projeto
├── README.md              # Este manual de instruções do projeto
├── app.py                 # Ponto de entrada (orquestrador principal do app)
├── core/                  # Pasta dedicada à lógica matemática e regras de negócio
│   ├── __init__.py        # Inicializador do pacote core
│   └── calculator.py      # Contém a classe de cálculo IPI_CALCULADORA
├── components/            # Pasta dedicada aos elementos visuais da tela
│   ├── __init__.py        # Inicializador do pacote components (vazio)
│   ├── layout.py          # Configurações de página e injeção de estilo CSS
│   └── outputs.py         # Cartões de valores, gráficos e tabelas de resultados
└── assets/                # Pasta de arquivos estáticos (design e estilo)
    └── style.css          # Estilos CSS personalizados para o Tema Escuro
```

---

## ⚙️ Como Instalar e Rodar o Aplicativo

Siga os passos abaixo para executar o aplicativo no seu computador utilizando o **VS Code**:

### 1. Pré-requisitos
Certifique-se de que você tem o Python instalado no seu computador.

### 2. Ativar o Ambiente Virtual (`venv`)
Abra o terminal integrado do VS Code e ative o ambiente virtual para garantir que as bibliotecas fiquem isoladas:
```powershell
.venv\Scripts\Activate.ps1
```
*(Você verá a indicação `(.venv)` no início da linha do terminal).*

### 3. Instalar as Dependências
Com o ambiente ativado, execute o comando abaixo para baixar as bibliotecas necessárias listadas no `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Executar o Aplicativo
Inicie o servidor do Streamlit executando o arquivo principal:
```bash
streamlit run app.py
```

O aplicativo será iniciado e abrirá uma janela automaticamente no seu navegador padrão no endereço `http://localhost:8501`.

---

## 🧠 Detalhes de Implementação (Lógica em Português)

A lógica de negócios foi desenvolvida na classe `IPI_CALCULADORA` dentro do arquivo `core/calculator.py` através do método `calcular`:

*   **Entrada de Dados:** Recebe o valor base do material (R$) e a porcentagem da alíquota do IPI (%).
*   **Fórmula do IPI:** 
    $$\text{Valor do IPI} = \text{Valor do Material} \times \left(\frac{\text{Alíquota do IPI \%}}{100}\right)$$
*   **Fórmula do Total:** 
    $$\text{Total com IPI} = \text{Valor do Material} + \text{Valor do IPI}$$
*   **Retorno:** Devolve um dicionário organizado contendo todos os dados calculados para serem exibidos na interface do Streamlit.
