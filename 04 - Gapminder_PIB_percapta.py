#Gráfico de dispersão do PIB per capita x expectativa de vida

"""
A mesma abordagem pode ser usada para um tipo diferente de gráfico, ou seja,
 o gráfico de dispersão. O código abaixo mostra como isso é feito. 
 facet_col é usado para dividir nosso gráfico em sub-gráficos de dados do continente, 
 como mostrado abaixo. 

"""

import plotly.express as px 
  
  
gapminder = px.data.gapminder() 
gapminder.head(15) 
  
fig = px.scatter( 
    gapminder,  
    x ="gdpPercap",  
    y ="lifeExp",  
    animation_frame ="year",  
    animation_group ="country", 
    size ="pop",  
    color ="continent",  
    hover_name ="country",  
    facet_col ="continent", 
    size_max = 45, 
    range_y =[25, 90] 
) 
fig.show()

"""

Conclusão
Portanto, neste artigo, aprendemos a codificar o seguinte usando Plotly Express e Python.

Choropleth Animado
Gráfico de Barras Animado
Gráfico animado de contorno de densidade
Gráfico de dispersão animado
O mesmo conhecimento pode ser estendido
para conjuntos de dados mais complexos, 
para gerar visualizações animadas e pode
ser usado com modelos de previsão para animar
dados previstos. 

"""