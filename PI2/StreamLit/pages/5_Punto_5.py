import streamlit as st
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_covid = i.df_covid
#total_staffed_adult_icu_beds
#staffed_icu_adult_patients_confirmed_covid
#total_staffed_pediatric_icu_beds
#staffed_icu_pediatric_patients_confirmed_covid

"5 - ¿Qué porcentaje de camas UCI corresponden a casos confirmados de COVID-19? Agrupe por Estado."
"Se asume que la pregunta es con respecto al 2020"
icu_ocupacion = df_covid[['date','state', 'total_staffed_adult_icu_beds','staffed_icu_adult_patients_confirmed_covid','total_staffed_pediatric_icu_beds','staffed_icu_pediatric_patients_confirmed_covid']]


icu_ocupacion['total_staffed_adult_icu_beds'] = pd.to_numeric(icu_ocupacion['total_staffed_adult_icu_beds'])
icu_ocupacion['staffed_icu_adult_patients_confirmed_covid'] = pd.to_numeric(icu_ocupacion['staffed_icu_adult_patients_confirmed_covid'])
icu_ocupacion['total_staffed_pediatric_icu_beds'] = pd.to_numeric(icu_ocupacion['total_staffed_pediatric_icu_beds'])
icu_ocupacion['staffed_icu_pediatric_patients_confirmed_covid'] = pd.to_numeric(icu_ocupacion['staffed_icu_pediatric_patients_confirmed_covid'])
icu_ocupacion['date'] = pd.to_datetime(icu_ocupacion['date'])

icu_ocupacion_2020 = icu_ocupacion.query("date >= '2020-01-01' and date <='2020-12-31'")
"En esta ocasion se encontró valores **NULOS**"
st.write(icu_ocupacion_2020.isnull().sum())
#icu_ocupacion_2020.fillna(1)
icu_ocupacion_2020['%_camas_ICU_Adultos'] = icu_ocupacion_2020['staffed_icu_adult_patients_confirmed_covid'] / icu_ocupacion_2020['total_staffed_adult_icu_beds']
icu_ocupacion_2020['%_camas_ICU_Pediatrico'] = icu_ocupacion_2020['staffed_icu_pediatric_patients_confirmed_covid'] / icu_ocupacion_2020['total_staffed_pediatric_icu_beds']
#icu_ocupacion_2020.info()
#icu_ocupacion_2020.fillna(1)

#st.write(icu_ocupacion_2020.info())
#icu_ocupacion_2020.dropna(inplace=True)
#icu_ocupacion_2020
tabla_porcentajes = icu_ocupacion_2020.groupby('state')['%_camas_ICU_Adultos','%_camas_ICU_Pediatrico'].sum().sort_values(by='%_camas_ICU_Adultos' ,ascending=False)
tabla_porcentajes.fillna(0,inplace=True)
st.dataframe(tabla_porcentajes)
