#%%
# Libs para Modelagem e Matrizes
import numpy as np
import pandas as pd 

# Libs para análises gráficas 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.graph_objects as go 

# Lib para ignorar avisos
import warnings 

# Desabilitando avisos 
warnings.filterwarnings('ignore')

#%%
# Lendo dados 

Base_dados = pd.read_excel('Vase_004_Magalu _Sem_Resolução.xlsx')

# Verificar dados 
Base_dados.shape
#%%
Base_dados.head()
#%%
Base_dados.info()
#%%
# Análises por tabela 
Base_dados.describe()
#%%
# Series Temporais 
Dados = Base_dados.set_index('Data')

(Dados.head)

# Grafico Análise das Ações da magalu - Fechamento 

plt.style.use ('seaborn-darkgrid')
plt.figure( figsize=(16,5))
plt.title('Análise das Ações da magalu - Fechamento ', fontsize= 16, loc='left')
plt.plot(Dados.index, Dados['Fechamento'])

plt.xlabel('Periodo da Coração')
plt.ylabel('Valor da Ação')
plt.show();

print(Dados.tail())

# Análise de media movel e media tendencia 
Media_Movel = Dados['Fechamento'].rolling(5).mean()
Media_Tendencia = Dados['Fechamento'].rolling(30).mean()

plt.style.use('seaborn-darkgrid')
plt.figure( figsize=(16, 5) )
plt.title('Análise das ações da magalu - Fechamento', fontsize=15, loc='left')

plt.plot( Dados.index, Dados['Fechamento'] )
plt.plot( Dados.index, Media_Movel )
plt.plot( Dados.index, Media_Tendencia )

plt.xlabel('Período da Coração')
plt.ylabel('Valor da Ação (R$)')
plt.show();

#Boxplot Mensal 
Base_dados['Mês'] = Base_dados['Data'].dt.month 

plt.figure ( figsize= (16,5))
sns.boxplot(data=Base_dados, x='Mês', y='Fechamento')
plt.show();

# Gráfico de comparação 
Grafico = go.Figure(
    data=[
        go.Candlestick(
            x= Dados.index,
            open= Dados['Abertura'],
            high = Dados['Maior'],
            low = Dados['Menor'],
            close = Dados['Fechamento'],
        )
    ]
)

Grafico.update_layout( xaxis_rangeslider_visible=False)

Grafico.show()