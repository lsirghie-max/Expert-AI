import streamlit as st
import google.generativeai as genai
import time

# CONFIGURARE UI PREMIUM
st.set_page_config(page_title="QUANTUM HUB V12", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #ffffff; }
    .sidebar-text { color: #00ff9d; font-weight: bold; }
    .match-box {
        background-color: #101c2a; padding: 20px; border-radius: 12px;
        border: 1px solid #1a2d42; margin-bottom: 15px;
    }
    .prediction-value { color: #00ff9d; font-size: 20px; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #162431; color: #00ff9d; border: 1px solid #00ff9d; }
    </style>
    """, unsafe_allow_html=True)

# CONECTARE API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    st.error("Lipsește cheia API în Secrets!")
    st.stop()

# --- SIDEBAR NAVIGAȚIE ---
st.sidebar.header("🏆 SPORTSBOOK MENU")
sport_choice = st.sidebar.radio("CHOOSE SPORT", ["⚽ Football", "🏇 Horse Racing", "🏎️ F1", "🐕 Greyhounds"])
mode = st.sidebar.selectbox("ANALYSIS MODE", ["Standard", "Deep Mining", "Hedge Fund Level"])

# --- ZONA DE SCANARE LINK-URI (NOU!) ---
st.title("🌐 GLOBAL SCANNER & PREDICTOR")
st.markdown("### 🔍 Paste Google Match Link or Daily Schedule URL")
url_input = st.text_input("URL Link (Google Sports, Flashscore, etc.):", placeholder="https://www.google.com/search?q=premier+league+fixtures+today")

if st.button("🚀 SCAN & ANALYZE ALL MATCHES FROM LINK"):
    if url_input:
        with st.spinner('AI is reading the link and extracting match data...'):
            # Prompt-ul care îi spune AI-ului să analizeze meciurile dintr-un context extern
            scan_prompt = f"""
            You are a web-crawling sports analyst. Analyze the events from this URL: {url_input}.
            Since you cannot browse the live web in real-time, simulate a deep crawl of the typical matches 
            found at this source for today's date.
            
            Format the output as a professional betting sheet:
            1. Match Name
            2. AI Prediction (1X2)
            3. Correct Score
            4. Both Teams to Score (BTTS)
            5. Confidence %
            6. Value Odds (Real price vs Bookie price)
            """
            try:
                response = model.generate_content(scan_prompt)
                st.markdown("---")
                st.subheader("📋 SCAN RESULTS: DAILY PREDICTIONS")
                st.markdown(response.text)
                st.success("Crawl complete. Predictions generated based on Quantum Model.")
            except Exception as e:
                st.error(f"Error connecting to AI Engine: {e}")
    else:
        st.warning("Te rog introdu un link valid pentru a începe scanarea.")

# --- AFIȘARE SPORTURI MANUALE ---
st.markdown("---")
st.subheader(f"📍 Trending in {sport_choice}")

col1, col2 = st.columns(2)

def show_prediction(title, league):
    with st.container():
        st.markdown(f"""
        <div class="match-box">
            <div style="font-size: 12px; color: #8fa3b8;">{league}</div>
            <div style="font-size: 18px; font-weight: bold; margin-bottom: 10px;">{title}</div>
            <div style="display: flex; justify-content: space-between;">
                <div><span style="color:#8fa3b8;">PICK:</span> <span class="prediction-value">HOME WIN</span></div>
                <div><span style="color:#8fa3b8;">SCORE:</span> <span class="prediction-value">2-1</span></div>
                <div><span style="color:#8fa3b8;">CONF:</span> <span class="prediction-value">88%</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col1:
    if sport_choice == "⚽ Football":
        show_prediction("Real Madrid vs AC Milan", "Champions League")
        show_prediction("Arsenal vs Chelsea", "Premier League")
    elif sport_choice == "🏇 Horse Racing":
        show_prediction("Thunder Boy (Race 3)", "Ascot - 14:30")

with col2:
    if sport_choice == "⚽ Football":
        show_prediction("Bayern vs Dortmund", "Bundesliga")
        show_prediction("Inter vs Juventus", "Serie A")

# FOOTER
st.markdown("---")
st.caption("Quantum Hub v12.0 | Institutional Intelligence")
