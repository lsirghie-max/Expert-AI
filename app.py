import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np
import time

# CONFIGURARE QUANTUM v10
st.set_page_config(page_title="SmartOdds Quantum AI", page_icon="🧬", layout="wide")

# Interfață stil Terminal Profesional
st.markdown("""
    <style>
    .stApp { background-color: #02040a; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { 
        background: #00ff41; color: black; border: none; font-weight: bold; 
        width: 100%; height: 50px; border-radius: 5px;
    }
    .live-dot { height: 10px; width: 10px; background-color: #ff0000; border-radius: 50%; display: inline-block; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# CONECTARE API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Folosim Pro pentru că ai setat instrucțiunile în AI Studio
    model = genai.GenerativeModel('gemini-1.5-pro') 
else:
    st.error("⚠️ API Key lipsă în Streamlit Secrets!")
    st.stop()

st.sidebar.title("🧬 QUANTUM CONTROL")
sport = st.sidebar.selectbox("Category", ["Football", "Horse Racing", "Greyhounds"])
st.title("🛡️ SMARTODDS QUANTUM ENGINE")
st.markdown(f"**STATUS:** <span class='live-dot'></span> **SYSTEM LIVE**", unsafe_allow_html=True)

event = st.text_input("ENTER MATCH / RACE NAME:", placeholder="e.g. Real Madrid vs Man City")

# Grafic Momentum
if 'data' not in st.session_state: st.session_state.data = [50.0]
st.session_state.data.append(max(5, min(95, st.session_state.data[-1] + np.random.normal(0, 2))))
if len(st.session_state.data) > 20: st.session_state.data.pop(0)
st.line_chart(st.session_state.data)

if st.button("EXECUTE QUANTUM SCAN"):
    if event:
        with st.spinner('SCANNING GLOBAL DATA...'):
            # AI-ul va folosi acum instrucțiunile pe care le-ai pus în AI Studio
            response = model.generate_content(f"Analyze the following event: {event} for {sport}. Find the value edge.")
            st.markdown("### 🧬 QUANTUM INSIGHT:")
            st.write(response.text)

# Refresh automat pentru grafic
time.sleep(10)
st.rerun()
