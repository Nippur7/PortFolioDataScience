import streamlit as st
from datetime import datetime
import pandas as pd
from sodapy import Socrata
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
df_covid = i.df_covid

def downloadData ():
    client = Socrata("healthdata.gov", None)
    results = client.get("g62h-syeh", limit=50000)
    return(pd.DataFrame.from_records(results))

#df_covid = pd.read_csv('../PI2/COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv',sep=',', encoding='utf-8')
#df_covid = downloadData()
" 1 - ¿Cuáles fueron los 5 Estados con mayor ocupación hospitalaria por COVID? Criterio de ocupación por cama común. Considere la cantidad de camas ocupadas con pacientes confirmados y tome como referencia los 6 primeros meses del 2020 - recuerde incluir la cifra de infectados en esos meses (acumulativo). ¿Influye el rango etario en este comportamiento?"
#Transformamos datos
ocupacion_estados = df_covid[['date','state', 'inpatient_beds','inpatient_beds_used','inpatient_beds_used_covid','previous_day_admission_adult_covid_confirmed','previous_day_admission_pediatric_covid_confirmed','hospital_onset_covid']]
ocupacion_estados['inpatient_beds'] = pd.to_numeric(ocupacion_estados['inpatient_beds'])
ocupacion_estados['inpatient_beds_used'] = pd.to_numeric(ocupacion_estados['inpatient_beds_used'])
ocupacion_estados['inpatient_beds_used_covid'] = pd.to_numeric(ocupacion_estados['inpatient_beds_used_covid'])
ocupacion_estados['previous_day_admission_adult_covid_confirmed'] = pd.to_numeric(ocupacion_estados['previous_day_admission_adult_covid_confirmed'])
ocupacion_estados['previous_day_admission_pediatric_covid_confirmed'] = pd.to_numeric(ocupacion_estados['previous_day_admission_pediatric_covid_confirmed'])
ocupacion_estados['hospital_onset_covid'] = pd.to_numeric(ocupacion_estados['hospital_onset_covid'])
ocupacion_estados['date'] = pd.to_datetime(ocupacion_estados['date'])

#filtramos la fecha requerida
ocupacion_estados_2020=ocupacion_estados.query("date >= '2020-01-01' and date <='2020-06-30'")
estados_max_ocup = ocupacion_estados_2020.sort_values(by=['inpatient_beds_used_covid'],ascending=False)
#filtro_estados_2020 = pd.DataFrame(ocupacion_estados_2020.groupby('state')['inpatient_beds_used_covid'].sum().sort_values(ascending=False)).head(5)
filtro_estados_2020 = pd.DataFrame(ocupacion_estados_2020.groupby('state')['inpatient_beds_used_covid','hospital_onset_covid'].sum().sort_values(by='inpatient_beds_used_covid', ascending=False)).head(5)
#filtro_estados_2020
st.write(filtro_estados_2020)
st.write("Según los datos consultados **El rango etario** **no** influye en este comportamiento, al ser valores despreciables en relación a los totales")
