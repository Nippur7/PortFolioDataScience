import streamlit as st
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import cufflinks as cf
from IPython.display import display, HTML
#matplotlib.use('WebAgg')

cf.set_config_file(sharing='public', theme='white', offline=False)
df_covid = i.df_covid
#total_pediatric_patients_hospitalized_confirmed_covid
#total_staffed_pediatric_icu_beds

"4 - ¿Qué cantidad de camas se utilizaron, por Estado, para pacientes pediátricos con COVID durante el 2020?"


pedriatricos = df_covid[['date','state', 'total_pediatric_patients_hospitalized_confirmed_covid']]
pedriatricos['date'] = pd.to_datetime(pedriatricos['date'])
pedriatricos['total_pediatric_patients_hospitalized_confirmed_covid']= pd.to_numeric(pedriatricos['total_pediatric_patients_hospitalized_confirmed_covid'])
pedriatricos.head()
pediatricos_2020 = pedriatricos.query("date >= '2020-01-01' and date <='2020-12-31'")
tabla_pediatricos = pediatricos_2020.groupby('state')['total_pediatric_patients_hospitalized_confirmed_covid'].sum().sort_values(ascending=False).head(5)
tabla_pediatricos
mascara = pediatricos_2020[pediatricos_2020['state'].isin(tabla_pediatricos.index)]
#mascara
x_pedriatricos = mascara['date']
y_pediatricos = mascara['total_pediatric_patients_hospitalized_confirmed_covid']
sns.set_theme(style="darkgrid", context="talk")
sns.set(font_scale=1.5)
gNY = sns.relplot(data=mascara, x=x_pedriatricos,y=y_pediatricos,
                        hue='state',
                        height= 8,
                        aspect=2, kind='line')

gNY.figure.autofmt_xdate(rotation=90)
plt.xlabel('Fecha', fontsize=16)
plt.ylabel('Camas Ocupadas', fontsize=16)
plt.title('Ocupación de camas ICU pediatricas por Estado durante el 2020', fontsize=20)
#plt.show();
st.pyplot(gNY)
#mascara.iplot(kind='bar',x='date',y='total_pediatric_patients_hospitalized_confirmed_covid', xTitle='Fecha',yTitle='Cantidad de Camas Ocupadas',title='Ocupación de camas por estado durante el 2020')




