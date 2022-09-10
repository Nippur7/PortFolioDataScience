import streamlit as st
import sys
sys.path.append("PI2\StreamLite\Intro.py")
import Intro as i
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_covid = i.df_covid
"3 - ¿Cuáles fueron los cinco Estados que más camas UCI -Unidades de Cuidados Intensivos- utilizaron durante el año 2020? La medición debe realizarse en términos absolutos."
#staffed_adult_icu_bed_occupancy_coverage
#state
#date

estados_icu_util = df_covid[['date','state', 'staffed_icu_adult_patients_confirmed_and_suspected_covid']]
estados_icu_util['date'] = pd.to_datetime(estados_icu_util['date'])
estados_icu_util['staffed_icu_adult_patients_confirmed_and_suspected_covid']= pd.to_numeric(estados_icu_util['staffed_icu_adult_patients_confirmed_and_suspected_covid'])
estados_icu_util_2020 = estados_icu_util.query("date >= '2020-01-01' and date <='2020-12-31'").groupby('state')['staffed_icu_adult_patients_confirmed_and_suspected_covid'].sum().sort_values(ascending=False).head(5)
estados_icu_util_2020
sns.set_theme(style="darkgrid", context="talk")
sns.set(font_scale=1.5)
gNY = sns.relplot(data=estados_icu_util_2020,
                        height= 8,
                        aspect=2, kind='line')

gNY.figure.autofmt_xdate(rotation=90)
plt.xlabel('Estados', fontsize=16)
plt.ylabel('Camas Ocupadas', fontsize=16)
plt.title('Ocupación de camas de Unidad de Cuidados Intensivos (UCI) durante el 2020', fontsize=20)
#plt.show();
st.pyplot(gNY)