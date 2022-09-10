import streamlit as st
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt
df_covid = i.df_covid
#deaths_covid
#critical_staffing_shortage_today_yes
"7 - ¿Qué relación presenta la falta de personal médico, con la cantidad de muertes por covid durante el año 2021?"

muertes = df_covid[['date','state','deaths_covid','critical_staffing_shortage_today_yes']]
muertes['deaths_covid'] = pd.to_numeric(muertes['deaths_covid'])
muertes['critical_staffing_shortage_today_yes'] = pd.to_numeric(muertes['critical_staffing_shortage_today_yes'])
muertes['date'] = pd.to_datetime(muertes['date'])
muertes_2021 = muertes.query("date >= '2021-01-01' and date <='2021-12-31'")
#muertes_2021
x_muertes_2021 = muertes_2021['date']
y_muertes_2021 = muertes_2021['deaths_covid']
sns.set_theme(style="darkgrid", context="talk")
sns.set(font_scale=1.5)
gd2021 = sns.relplot(data=muertes_2021, x='date',y='deaths_covid',
                        #hue='state',
                        height= 8,
                        aspect=2, kind='line')
gs2021 = sns.relplot(data=muertes_2021, x='date',y='critical_staffing_shortage_today_yes',
                        #hue='state',
                        height= 8,
                        aspect=2, kind='line')
gd2021.figure.autofmt_xdate(rotation=90)
gs2021.figure.autofmt_xdate(rotation=90)
#plt.xlabel('Fecha', fontsize=16)
#plt.ylabel('Cantidad de Hospitales Sin recursos', fontsize=16)
#plt.title('Cantidad de Hospitales Colapsados', fontsize=20)
#plt.show();
st.pyplot(gd2021)
st.pyplot(gs2021)