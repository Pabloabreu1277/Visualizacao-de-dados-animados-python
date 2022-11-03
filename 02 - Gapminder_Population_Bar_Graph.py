#Population Bar Graph
"""
Agora vamos fazer um gráfico de barras animado usando o mesmo 
conjunto de dados usando a população como nossos dados primários nesta instância. 
Seja ox dos dados o continente ey a população e, quando passa o mouse sobre os nomes dos países, 
devem ser mostrados. Então, vamos definir o foco como 'país' . 
É importante especificar o intervalo, pois ajuda a compreender a escala dos dados com os quais estamos trabalhando. 
O parâmetro em que a animação é feita é, claro, o ano. 

"""

import plotly.express as px 
  
  
gapminder = px.data.gapminder() 
gapminder.head(15) 
  
fig = px.bar(gapminder,  
             x ="continent",  
             y ="pop", 
             color ='lifeExp', 
             animation_frame ='year', 
             hover_name ='country',  
             range_y =[0, 4000000000]) 
fig.show()

