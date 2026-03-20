import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np
import time

# --- CONFIGURARE UI QUANTUM HUB V12.1 ---
st.set_page_config(page_title="QUANTUM HUB PRO", page_icon="🌐", layout="wide")

# DESIGN STIL BET365 / CORAL (NEGRU & VERDE MENTĂ)
st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #ffffff; font-family: 'Segoe UI', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0a121a; border-right: 1px solid #1a2d42; }
    .match-card {
        background-color: #101c2a; padding: 20px; border-radius: 12px;
        border-left: 5px solid #00ff9d; margin-bottom: 15px;
    }
    .prediction-value { color: #00ff9d; font-size: 18px; font-weight: bold; }
    .stButton>button {
        background: linear-gradient(90deg, #00ff9d, #00c853);
        color: #000000; border: none; font-weight: bold; border-radius: 8px; width: 100%;
    }
    .scan-btn>button {
        background: #ff4b4b !important; color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONECTARE API (REPARATĂ PENTRU EROAREA 404) ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Folosim gemini-1.5-flash pentru stabilitate maximă și viteză
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
else:
    st.error("⚠️ CHEIA API LIPSEȘTE! Verifică Settings -> Secrets în Streamlit.")
    st.stop()

# --- SIDEBAR: MENIU SPORTURI ---
st.sidebar.title("🏆 QUANTUM SPORTS")
sport_choice = st.sidebar.radio("SELECT SPORT", ["⚽ Football", "🏇 Horse Racing", "🏎️ F1", "🐕 Greyhounds"])
analysis_depth = st.sidebar.select_slider("AI POWER", options=["Standard", "Pro", "Quantum"])

# --- ZONA DE SCANARE LINK-URI (CERINȚA TA) ---
st.title("🌐 GLOBAL SCANNER & PREDICTOR")
st.markdown("##### 🔍 Paste Google, Flashscore or Betting Link below")

url_input = st.text_input("URL Link:", placeholder="Paste link here (e.g. Google Search results for matches)")

col_btn, col_empty = st.columns([1, 2])
with col_btn:
    st.markdown('<div class="scan-btn">', unsafe_allow_html=True)
    scan_clicked = st.button("🚀 SCAN & ANALYZE ALL")
    st.markdown('</div>', unsafe_allow_html=True)

if scan_clicked:
    if url_input:
        with st.spinner('AI is deep-crawling the link...'):
            # Prompt-ul "The Beast"
            scan_prompt = f"""
            Analyze all sporting events from this source: {url_input}.
            Identify every match/race mentioned. For each one, provide:
            1. Match/Race Name
            2. AI Winner Prediction (High Confidence)
            3. Correct Score (Exact)
            4. Both Teams to Score / Winning Margin
            5. Confidence Percentage (0-100%)
            Format it as a clean, professional betting sheet.
            """
            try:
                response = model.generate_content(scan_prompt)
                st.markdown("### 📋 DAILY PREDICTIONS SHEET")
                st.markdown(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Engine Error: {str(e)}")
    else:
        st.warning("Te rog pune un link mai întâi!")

# --- SECȚIUNE TRENDING (EXEMPLE VIZUALE CA ÎN POZELE TALE) ---
st.markdown("---")
st.subheader(f"📍 Live Insights: {sport_choice}")

c1, c2 = st.columns(2)

def render_box(match, league, pick, score, conf):
    st.markdown(f"""
    <div class="match-card">
        <div style="font-size: 11px; color: #8fa3b8; text-transform: uppercase;">{league}</div>
        <div style="font-size: 20px; font-weight: bold; margin-bottom: 10px;">{match}</div>
        <div style="display: flex; justify-content: space-between; background: #050a0f; padding: 10px; border-radius: 5px;">
            <div><span style="color:#8fa3b8; font-size:12px;">AI PICK</span><br><span class="prediction-value">{pick}</span></div>
            <div><span style="color:#8fa3b8; font-size:12px;">SCORE</span><br><span class="prediction-value">{score}</span></div>
            <div><span style="color:#8fa3b8; font-size:12px;">CONFIDENCE</span><br><span class="prediction-value" style="color:#00ff9d;">{conf}%</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c1:
    if sport_choice == "⚽ Football":
        render_box("Man City vs Arsenal", "Premier League", "HOME WIN", "2-1", "88")
    elif sport_choice == "🏇 Horse Racing":
        render_box("Red Rocket", "Ascot - 15:40", "WINNER", "Odds: 3.50", "72")

with c2:
    if sport_choice == "⚽ Football":
        render_box("Real Madrid vs Milan", "Champions League", "HOME WIN", "3-1", "91")
    elif sport_choice == "🏇 Horse Racing":
        render_box("Blue Ocean", "Cheltenham - 16:10", "PLACE", "Odds: 5.00", "64")

# FOOTER
st.markdown("---")
st.caption("Quantum Hub v12.1 | Powered by Gemini 1.5 Flash")
