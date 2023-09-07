import streamlit as st
import os
st.set_page_config(
    page_title="HABLAX.INC Dashboard - Home",
    layout="wide"
)

# user = st.text_input("Ingrese el Usuario", type="default", key='user')
# passw = st.text_input("Ingrese la contraseña", type ="password", key= 'contra')
with st.form("login"):
    user = st.text_input("Ingrese el Usuario", type="default", key='user')
    passw = st.text_input("Ingrese la contraseña", type ="password", key= 'contra')
    submit = st.form_submit_button('Enviar')

if submit and user == st.secrets['user'] and passw == st.secrets['pass']:
    st.session_state['validate'] = True
    st.success("Ingreso exitoso, puede usar en el menú de la izquierda la opción Dashboard")
else:
        #        st.write('Error')
    if not submit:
        st.warning("Debe ingresar un usuario y una contraseña para poder continuar.")
    else:
        st.write("Usuario y/o contraseña erróneos")