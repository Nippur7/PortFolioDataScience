import streamlit as st

st.set_page_config(
    page_title="Global Energy consumption and CO2 - Home",
    layout="wide"
)


st.title('Global Energy consumption and CO2')

st.markdown("""
            <div style="text-align: justify;">
            This data is property of HABLAX.INC.


            </div>
            """, unsafe_allow_html=True)
@st.experimental_memo
def load_dashboard():
    return 'https://app.powerbi.com/reportEmbed?reportId=97ef94c8-08cd-4850-85cf-beeebfb7a7e7&autoAuth=true&ctid=458a0ded-ee7b-47cc-8185-2f3d6065b450'

st.components.v1.iframe(load_dashboard(), height=700)
