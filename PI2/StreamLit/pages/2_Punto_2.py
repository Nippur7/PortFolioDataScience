import streamlit as st
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_covid = i.df_covid
ocupacion_estados = df_covid[['date','state', 'inpatient_beds','inpatient_beds_used','inpatient_beds_used_covid','previous_day_admission_adult_covid_confirmed','previous_day_admission_pediatric_covid_confirmed','hospital_onset_covid']]
ocupacion_estados['inpatient_beds'] = pd.to_numeric(ocupacion_estados['inpatient_beds'])
ocupacion_estados['inpatient_beds_used'] = pd.to_numeric(ocupacion_estados['inpatient_beds_used'])
ocupacion_estados['inpatient_beds_used_covid'] = pd.to_numeric(ocupacion_estados['inpatient_beds_used_covid'])
ocupacion_estados['previous_day_admission_adult_covid_confirmed'] = pd.to_numeric(ocupacion_estados['previous_day_admission_adult_covid_confirmed'])
ocupacion_estados['previous_day_admission_pediatric_covid_confirmed'] = pd.to_numeric(ocupacion_estados['previous_day_admission_pediatric_covid_confirmed'])
ocupacion_estados['hospital_onset_covid'] = pd.to_numeric(ocupacion_estados['hospital_onset_covid'])
ocupacion_estados['date'] = pd.to_datetime(ocupacion_estados['date'])
ocupacion_estados_2020=ocupacion_estados.query("date >= '2020-01-01' and date <='2020-06-30'")
filtroNY = ocupacion_estados_2020['state'] == 'NY'
OnlyNY = ocupacion_estados_2020[filtroNY]
y_NY = OnlyNY['inpatient_beds_used_covid']
x_NY = OnlyNY['date']
#sns.lineplot(y_NY,x_NY)
sns.set_theme(style="darkgrid", context="talk")
sns.set(font_scale=1.5)
gNY = sns.relplot(data=OnlyNY, y=y_NY,x=x_NY,
                        height= 8,
                        aspect=2, kind='line')

gNY.figure.autofmt_xdate(rotation=90)
plt.xlabel('Días', fontsize=16)
plt.ylabel('Cantidad de Ocupación', fontsize=16)
plt.title('Ocupación de camas durante la cuarentena "Lockdown"', fontsize=20)
"2 - Analice la ocupación de camas (Común) por COVID en el Estado de Nueva York durante la cuarentena establecida e indique:"

"-Intervalos de crecimiento y decrecimiento"
"-Puntos críticos (mínimos y máximos)"
st.pyplot(gNY)
"Como se observa en el gráfico el punto máximo se encuentra en el día 14/04/2020"
"Desde ese punto comienza a decrecer"
#OnlyNY[['date','inpatient_beds_used_covid']]
Tabla2 = OnlyNY.sort_values('inpatient_beds_used_covid', ascending=False)
Tabla2[['date','inpatient_beds_used_covid']]