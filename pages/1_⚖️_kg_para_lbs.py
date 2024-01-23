import streamlit as st

st.set_page_config(
    page_title='Kg para lbs',
    page_icon='⚖️'
)

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2046

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2046

st.title("⚖️ Conversor de kg para lbs")
col_1, col_2 = st.columns(2)

with col_1:
    kg = st.number_input('Kg',step=1.0, key='kg', on_change=kg_to_lbs)
with col_2:
    lbs = st.number_input('lbs',step=1.0, key='lbs', on_change=lbs_to_kg)