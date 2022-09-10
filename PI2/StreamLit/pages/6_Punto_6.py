import streamlit as st
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_covid = i.df_covid
#deaths_covid
"6 - ¿Cuántas muertes por covid hubo, por Estado, durante el año 2021?"

muertes = df_covid[['date','state','deaths_covid']]
muertes['deaths_covid'] = pd.to_numeric(muertes['deaths_covid'])
muertes['date'] = pd.to_datetime(muertes['date'])
muertes_2021 = muertes.query("date >= '2021-01-01' and date <='2021-12-31'")
tabla_muertes_2021 = muertes_2021.groupby('state')['deaths_covid'].sum().sort_values(ascending=False)
#tabla_grafico = muertes_2021.groupby('state')['date','deaths_covid'].sum().sort_values(by='date',ascending=False)
tabla_muertes_2021
x_muertes_2021 = muertes_2021['date']
y_muertes_2021 = muertes_2021['deaths_covid']
sns.set_theme(style="darkgrid", context="talk")
sns.set(font_scale=1.5)
gNY = sns.relplot(data=muertes_2021, x='date',y='deaths_covid',
                        hue='state',
                        height= 8,
                        aspect=2, kind='line')

gNY.figure.autofmt_xdate(rotation=90)
plt.xlabel('Fechas', fontsize=16)
plt.ylabel('Muertes diarias', fontsize=16)
plt.title('Muertes diarias en el 2021', fontsize=20)
#plt.show();
st.pyplot(gNY)
