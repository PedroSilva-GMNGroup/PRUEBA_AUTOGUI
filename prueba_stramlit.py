import streamlit as st
import pyautogui as auto
import time 

st.set_page_config(
    page_title="MiAplicación",
    page_icon=":gear:",
    layout="wide"
)

time.sleep(3)
auto.moveTo(100,100)
time.sleep(1)
auto.moveTo(250,250)
time.sleep(1)
auto.moveTo(500,500)
time.sleep(1)
auto.moveTo(1000,1000)