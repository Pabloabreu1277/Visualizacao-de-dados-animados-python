#Contorno de densidade do PIB per capita x expectativa de vida.
"""
A relação entre a expectativa de vida e o PIB per capita ao longo do tempo
é um componente importante para as estatísticas de dados governamentais ou nacionais. 
Os governos podem (e têm) usado isso para estabelecer correlação entre os dois e isso
 explica porque o aumento na expectativa de vida também aumentou o PIB per capita. 
A abordagem pode ser visualizada usando um gráfico de contorno de densidade e um histograma. 

"""
import plotly.express as px 
  
gapminder = px.data.gapminder() 
gapminder.head(15) 
  
fig = px.density_contour(gapminder,  
                         x ="gdpPercap",  
                         y ="lifeExp",  
                         color ="continent",  
                         marginal_y ="histogram", 
                         animation_frame ='year',  
                         animation_group ='country',  
                         range_y =[25, 100]) 
fig.show()