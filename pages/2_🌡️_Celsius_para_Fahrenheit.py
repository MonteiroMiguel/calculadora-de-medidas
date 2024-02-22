import streamlit as st
st.set_page_config(
    page_title='°C para °F',
    page_icon='🌡️'
)
def fahrenheit_to_celsius():
    st.session_state.celsius = (st.session_state.fahrenheit - 32) / 1.8

def celsius_to_fahrenheit():
    st.session_state.fahrenheit = (st.session_state.celsius * 1.8) + 32

st.title("🌡️ Conversor de Celsius para Fahrenheit ")

col_1, col_2 = st.columns(2) 
with col_1:
    celsius = st.number_input('°C',value=0.0,step=1.0, key='celsius', on_change=celsius_to_fahrenheit)

with col_2:
    fahrenheit = st.number_input('°F',value=32.0,step=1.0, key='fahrenheit', on_change=fahrenheit_to_celsius)
