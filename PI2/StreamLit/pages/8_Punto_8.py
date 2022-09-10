import streamlit as st
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_covid = i.df_covid
"8 - Siguiendo las respuestas anteriores, ¿cuál fue el peor mes de la pandemia para USA en su conjunto? Puede utilizar otras medidas que considere necesarias."

muertes = df_covid[['date','state','deaths_covid']]
muertes['deaths_covid'] = pd.to_numeric(muertes['deaths_covid'])
muertes['date'] = pd.to_datetime(muertes['date'])
muertes['MES'] = muertes['date'].dt.month
muertes['ANIO'] = muertes['date'].dt.year
muertes['AnioMes'] = muertes['ANIO'].apply(str) + muertes['MES'].apply(lambda x: f'{x:02d}')
#df_v1['SEMANA'] = df_v1['FECHA'].dt.week
#df_v1['ANIO'] = df_v1['FECHA'].dt.year
#df_v1['DIA'] = df_v1['FECHA'].dt.weekday
#df_v1['ANIOSEMANA'] = df_v1['ANIO'].apply(str) + df_v1['SEMANA'].apply(lambda x: f'{x:02d}')
#
#muertes_2021 = muertes.query("date >= '2021-01-01' and date <='2021-12-31'")
tabla_muertes_2021 = muertes.groupby('AnioMes')['deaths_covid'].sum().sort_values(ascending=False)
#tabla_grafico = muertes_2021.groupby('state')['date','deaths_covid'].sum().sort_values(by='date',ascending=False)
st.dataframe(data=tabla_muertes_2021, width=700,height=300)
x_muertes_2021 = muertes['AnioMes']
y_muertes_2021 = muertes['deaths_covid']
sns.set_theme(style="darkgrid", context="talk")
sns.set(font_scale=1.5)
gNY = sns.relplot(data=muertes, x='AnioMes',y='deaths_covid',
                        #hue='state',
                        height= 8,
                        aspect=2, kind='line')

gNY.figure.autofmt_xdate(rotation=90)
plt.xlabel('Fechas', fontsize=16)
plt.ylabel('Muertes diarias', fontsize=16)
plt.title('Muertes diarias en el 2021', fontsize=20)
plt.show();
st.pyplot(gNY)
#st.plotly_chart(gNY)
