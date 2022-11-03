#pip install plotly
#Exemplo: vamos imprimir as primeiras linhas deste banco de dados

import plotly.express as px
gapminder = px.data.gapminder()
print(gapminder.head(15))

#Coropleta da expectativa de vida
"""
Um coropleto é um mapa que usa diferenças de cor em áreas definidas sobre uma propriedade comum
 para visualizar os dados como um resumo agregado de uma região (neste caso, um país). 
 Plotly Express facilita a plotagem de choropleths. O código abaixo mostra como obter informações do gapminder. 
 Defina o parâmetro para o qual deseja colorir o coropleto. 
 Aqui, queríamos que o coropleto sombreie regiões com base na expectativa de vida ( lifeExp ). 
 hover_name mostra os dados definidos ao passar o mouse . 
 animation_frame se refere ao parâmetro no qual a animação deve ser feita (principalmente, 
 esse parâmetro são os dados da série temporal).

"""
fig = px.choropleth(gapminder, 
                    locations ="iso_alpha", 
                    color ="lifeExp", 
                    hover_name ="country",  
                    color_continuous_scale = px.colors.sequential.Plasma, 
                    scope ="world", 
                    animation_frame ="year") 
fig.show()