import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Web App v1.0",
    page_icon="⚕️",
)
st.sidebar.success("Seleccionar la opción arriba.")
st.header("Informe sobre Datos recolectados durante la emergencia Sanitaria producida por el Virus SARS COVID-19 en Estados Unidos")
"***Solicitado por el Centro de Control y Prevención de Enfermedades (CDC)***"
"**Análisis de datos covid EE.UU. desde el 01 de enero de 2020 al 04 de agosto de 2022**"
"El CDC (centro de control y prevención de enfermedades) de EE. UU. es la entidad encargada de monitorear la salud pública y desarrollar estrategias para la prevención y control de enfermedades. Por esto ha contratado a nuestra consultora para organizar, en base a los datos recolectados, los recursos hospitalarios para prevenir que lo ocurrido durante la pandemia COVID-19 suceda de vuelta"
"Nos disponibilizan desde el departamento de Data Engineering un archivo .csv, el cuál podemos usar para realizar nuestro análisis. Nuestro Team Líder, a su vez, nos facilitó información sobre la API, aclarando que podemos usarla como alternativa. El análisis solicitado, debe contemplar los datos hasta el 01/08/2022 inclusive."
df_covid = pd.read_csv('../COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv',sep=',', encoding='utf-8')