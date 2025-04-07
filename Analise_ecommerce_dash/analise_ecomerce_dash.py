import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import plotly.figure_factory as ff

df = pd.read_csv('C:/Users/vanes/PycharmProjects/Analise_ecommerce_dash/ecommerce_estatistica.csv')
lista_nota = sorted(df['Nota'].unique())
options = [{'label': nivel, 'value':nivel} for nivel in lista_nota]

print(df.head().to_string())


def criar_graficos(graficos_ecommerce):

    filtro_df = df[df['Nota'].isin(graficos_ecommerce)]

     # Histograma com frequência de notas(avaliações) no ecommerce
    fig1 = px.histogram(filtro_df, x='Nota', nbins=30, color_discrete_sequence=['blue'])
    fig1.update_traces(
        marker=dict(opacity=0.7, line=dict(color="black", width=1)))
    fig1.update_layout(
        title='Avaliações Mais Frequentes do Ecommerce',
        xaxis_title='Notas - Avaliações',
        yaxis_title='Frequência',
        title_x=0.5)

    # Gráfico de dispersão relacionando nota e desconto
    fig2 = px.scatter(filtro_df, x='Nota',y='Desconto', title='Relação entre Nota e Desconto', color_discrete_sequence=['purple'])
    fig2.update_traces(marker=dict(opacity=0.7, line=dict(color="black", width=1), size=10))
    fig2.update_layout(title_x=0.5)

    # Mapa de Calor nota vs preço x desconto x marca
    corr = filtro_df[['Nota','Preço','Desconto','Marca_Cod']].corr() # Calcular a matriz de correlação
    fig3 = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu', title='Correlação entre Variáveis')
    fig3.update_layout(title_x=0.5)

    # Gráfico de barras relação nota e quantidade vendida
    fig4 = px.bar(filtro_df, x='Nota', y='Qtd_Vendidos_Cod', color_discrete_sequence=['blue'])
    fig4.update_layout(
        title='Quantidade de Vendidas por Nota',
        xaxis_title='Nota',
        yaxis_title='Quantidade Vendidas',
        title_x=0.5)

    # Gráfico de Pizza - Distribuição das Notas
    notas_count = filtro_df['Nota'].value_counts()
    notas_count = notas_count[notas_count > 5]
    fig5 = px.pie(names=notas_count.index, values=notas_count.values, title='Distribuição das Notas no Ecommerce')
    fig5.update_layout(title_x=0.5)

    # Gráfico de Densidade - Avaliações (Notas)
    fig6 = ff.create_distplot([filtro_df['Nota']], group_labels=['Notas'], show_hist=False, show_rug=False)
    fig6.update_layout(
        title='Densidade Avaliações - Nota',
        xaxis_title='Avaliações - Notas',
        yaxis_title='Densidade',
        title_x=0.5
    )

    # Gráfico de Regressão - Nota x Desconto
    fig7 = px.scatter(filtro_df, x='Nota', y='Desconto', trendline="ols", opacity=0.5, color_discrete_sequence=['blue'])
    fig7.update_layout(
    title='Regressão: Relação entre Nota e Desconto',
        xaxis_title='Nota',
        yaxis_title='Desconto',
        title_x=0.5
)
    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

def cria_app():
    # criar aplicação DASH
    app = Dash(__name__)

    # Layout aplicação DASH
    app.layout = html.Div([
        html.H1('Analise Ecommerce', style={'textAlign': 'center'}),
        html.H2('Gráficos Ecommerce', style={'textAlign': 'center'}),
        html.Div([
            html.Label('Selecione as notas que deseja visualizar:', style={
                'fontSize': '18px',
                'fontWeight': 'bold',
                'marginBottom': '10px',
                'display': 'block'
            }),
            dcc.Checklist(
                id='id_graficos_ecommerce',
                options=options,
                value=lista_nota,
                labelStyle={'display': 'inline-block', 'marginRight': '10px'}
            )
        ], style={'width': '80%', 'margin': 'auto'}),
        # dcc.Checklist( id='id_graficos_ecommerce', options=options, value=lista_nota),
        dcc.Graph(id='id_histograma'),
        dcc.Graph(id='id_grafico_dispersao'),
        dcc.Graph(id='id_mapa_calor'),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_pizza'),
        dcc.Graph(id='id_grafico_densidade'),
        dcc.Graph(id='id_grafico_regressao')
    ])
    return app


# Executar app
if __name__ == '__main__':
    app = cria_app()

    @app.callback(
        [
            Output('id_histograma','figure'),
            Output('id_grafico_dispersao','figure'),
            Output('id_mapa_calor', 'figure'),
            Output('id_grafico_barra', 'figure'),
            Output('id_grafico_pizza', 'figure'),
            Output('id_grafico_densidade', 'figure'),
            Output('id_grafico_regressao', 'figure'),
        ],
        [Input('id_graficos_ecommerce', 'value')]
    )
    def atualiza_grafico(graficos_ecommerce):
        fig1, fig2, fig3, fig4, fig5, fig6, fig7 = criar_graficos(graficos_ecommerce)
        return [fig1, fig2, fig3, fig4, fig5, fig6, fig7]
    app.run_server(debug=True, port=8050)