Análise de Ecommerce 

Descrição

Este projeto tem como objetivo analisar dados de um ecommerce utilizando gráficos interativos desenvolvidos com as bibliotecas Dash, Plotly Express e Plotly Figure Factory. A aplicação permite a seleção dinâmica de avaliações (notas) para visualizar diferentes aspectos do desempenho de vendas, descontos, correlações entre variáveis e distribuição estatística.

Estrutura do Projeto

Arquivo CSV com os dados da análise: ecommerce_estatistica.csv

Variáveis utilizadas do arquivo CSV:
Nota: Avaliação do produto (valor numérico)
Desconto: desconto aplicado do preço
Preço: Valor original do produto
Marca_Cod: Código representando a marca
Qtd_Vendidos_Cod: Quantidade de unidades vendidas

Como Executar o Projeto:
Certifique-se de ter o Python instalado (versão 3.7 ou superior)
Instale as dependências:pip install pandas dash plotly
Execute o script app.py: python app.py
Acesse a aplicação no navegador: http://127.0.0.1:8050

Funcionalidades da Interface:
Checklist com todas as notas (avaliações) disponíveis
Atualização automática dos gráficos conforme a seleção das notas(avaliações) 

Gráficos Disponíveis:
Histograma: Frequência das avaliações
Dispersão: Relação entre nota e desconto
Mapa de Calor: Correlação entre nota, preço, desconto e marca
Gráfico de Barras: Quantidade vendida por nota
Gráfico de Pizza: Distribuição de notas com mais de 5 ocorrências
Gráfico de Densidade: Distribuição das notas como curva
Gráfico de Regressão: Tendência entre nota e desconto

Funções Principais:
criar_graficos(graficos_ecommerce)
Recebe uma lista de notas e retorna os gráficos correspondentes baseados nos dados filtrados
cria_app()
Cria a aplicação Dash e define o layout com todos os componentes
atualiza_grafico(graficos_ecommerce)
Callback responsável por atualizar os gráficos com base nas seleções feitas pelo usuário
