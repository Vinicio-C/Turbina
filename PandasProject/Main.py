import pandas as pd
import seaborn as sns #para gráficos (upgrade do matplotlib)
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

turbina = pd.read_csv('T1.csv')#Fazendo leitura do arquivo .csv
turbina.columns = ['Data/hora','Potência(kW)','Velocidade do vento(m/s)','Curva Teórica(kWh)',
                   'Direção do Vento(º)']#Renomeando as primeiras colunas
del turbina['Direção do Vento(º)']#Deletando toda a coluna de Direção do Vento
turbina['Data/hora'] = pd.to_datetime(turbina['Data/hora'], format="%d %m %Y %H:%M")#Formatando para datetime

#Criando os gráficos
#sns.scatterplot(data=turbina, x= 'Velocidade do vento(m/s)', y='Potência(kW)')
#sns.scatterplot(data=turbina, x= 'Velocidade do vento(m/s)', y='Curva Teórica(kWh)')

#Tratando os dados para descartar os irrelevantes
#Colocando os dados em forma de lista
pot_real = turbina['Potência(kW)'].tolist()
pot_teorica = turbina['Curva Teórica(kWh)'].tolist()

#Adicionando as potências max e min
pot_max = []
pot_min = []
dentro_limite = []

for potencia in pot_teorica:
    pot_max.append(potencia*1.05)#adicionando +5%
    pot_min.append(potencia*0.95)#adicionando -5%

#Verificando os dados que estão dentro ou fora do limite
for p, potencia in enumerate(pot_real):
    if potencia>=pot_min[p] and potencia<=pot_max[p]:
        dentro_limite.append("Dentro")
    elif potencia == 0:
        dentro_limite.append("Zero")
    else:
        dentro_limite.append("Fora")

#Colocando tudo dentro do dataframe
turbina["Dentro Limite"] = dentro_limite#Adicionando nova coluna

#Adicionando gráfico com os dados tratados
cores = {"Dentro":"blue","Fora":"red","Zero":"orange"}#Adicionando um dicionário para uma palata de cores
#Hue diferencia os valores do gráfico com base na variável colocada
#S significa o tamanho dos dados apresentados no gráfico
sns.scatterplot(data=turbina, x= 'Velocidade do vento(m/s)', y='Potência(kW)', hue="Dentro Limite", s=1, palette=cores)#pallete alterna as cores do agrado do usuário

plt.show()#Mostra o gráfico