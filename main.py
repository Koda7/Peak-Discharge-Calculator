import streamlit as st
from utils import *


if 'runoff' not in st.session_state:
    st.session_state.peak_discharge = None
    st.session_state.error = None
    st.session_state.runoff = "0"
    st.session_state.intensity = "0"
    st.session_state.area = "0"

def calculate_peak_discharge():
    try:
        runoff = float(st.session_state.runoff)
        intensity = float(st.session_state.intensity) * intensity_units[st.session_state.intensity_unit]
        area = float(st.session_state.area) * area_units[st.session_state.area_unit]
        st.session_state.peak_discharge = runoff * intensity * area
        st.session_state.error = None
    except Exception as e:
        st.session_state.peak_discharge = None
        st.session_state.error = "Invalid input"

st.title('Peak discharge')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.form("peak_discharge_form", clear_on_submit=False):
    runoff_coefficient = st.text_input("Runoff Coeffecient",key="runoff")
    rainfall_intensity = st.text_input("Rainfall Intensity",key="intensity")
    rainfall_intensity_unit = st.selectbox("Select Rainfall Intensity Unit", intensity_units.keys(),key="intensity_unit")
    catchment_area = st.text_input("Catchment Area",key="area")
    catchment_area_unit = st.selectbox("Select Catchment Area Unit", area_units.keys(),key="area_unit")

    submit = st.form_submit_button("Submit",on_click=calculate_peak_discharge)

if(st.session_state.peak_discharge):
    st.success("Peak Discharge is %0.9f m\u00b3/s" % (st.session_state.peak_discharge))
if(st.session_state.error):
    st.error(st.session_state.error)