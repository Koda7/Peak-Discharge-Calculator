from distutils.command.upload import upload
from utils import *
import streamlit as st
import pandas as pd

if 'runoff_excel' not in st.session_state:
    st.session_state.uploaded = False
    st.session_state.runoff_excel = "0"
    st.session_state.intensity_file = None
    st.session_state.area_excel = "0"

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def calculate(row):
    return row[0] * row[1] * row[2] * intensity_units[st.session_state.intensity_unit] * area_units[st.session_state.area_unit]

def calculate_peak_discharge():
    st.session_state.uploaded = True

st.title('Peak discharge')

uploaded_file = st.file_uploader("Upload Excel file (xlsx,csv)", type=[".xlsx", ".csv"])
with st.form("peak_discharge_form", clear_on_submit=False):
    rainfall_intensity_unit = st.selectbox("Select Rainfall Intensity Unit", intensity_units.keys(),key="intensity_unit")
    runoff_coefficient = st.text_input("Runoff Coeffecient",key="runoff_excel")
    catchment_area = st.text_input("Catchment Area",key="area_excel")
    catchment_area_unit = st.selectbox("Select Catchment Area Unit", area_units.keys(),key="area_unit")

    submit = st.form_submit_button("Submit",on_click=calculate_peak_discharge)

if uploaded_file is not None and st.session_state.uploaded:
    try:
        df = pd.DataFrame()
        if uploaded_file.name.split(".")[-1] == "csv":
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file,engine='openpyxl')
        rainfall_column = df.columns[0]
        df['Runoff Coeffecient'] = float(st.session_state.runoff_excel)
        df['Catchment Area (%s)' % (st.session_state.area_unit)] = float(st.session_state.area_excel)
        df['Peak Discharge (m\u00b3/s)'] = df.apply (lambda row: calculate(row), axis=1)
        st.table(df)
    except Exception as e:
        print(e)
        st.error("Invalid Input")
    
