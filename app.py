import streamlit as st
import google.generativeai as genai
import datetime

# Configurare stil Profesional
st.set_page_config(page_title="SmartOdds Pro Engine", page_icon="⚽", layout="wide")

# CSS pentru aspect de site de pariuri
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .match-card { border: 1px solid #333; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #1e1e1e; }
    </style>
    """, unsafe_allow_html=True)

# Configurare AI
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("API Key missing!")

# Sidebar - Meniu lateral
st.sidebar.title("⚽ SmartOdds Pro")
st.sidebar.markdown("---")
league = st.sidebar.selectbox("Select League", ["Premier League", "Champions League", "La Liga", "Serie A", "Bundesliga", "World Cup"])
timeframe = st.sidebar.radio("Timeframe", ["Today's Matches", "This Week"])

st.title(f"📊 {league} - Predictions")
st.info(f"Analysis based on real-time data and historical statistics for {datetime.date.today()}")

# Simulare meciuri (Aici AI-ul va genera predictii pentru meciurile tari)
# Nota: Pentru meciuri 100% reale live e nevoie de un Football Data API Key separat
if league == "Premier League":
    matches = ["Liverpool vs Man City", "Arsenal vs Chelsea", "Tottenham vs West Ham"]
else:
    matches = ["Real Madrid vs Barcelona", "Bayern vs Dortmund"]

for match in matches:
    with st.container():
        st.markdown(f"""<div class="match-card">
            <h3>{match}</h3>
            <p>Status: Pre-Match Analysis Available</p>
        </div>""", unsafe_allow_html=True)
        
        if st.button(f"Analyze {match}", key=match):
            with st.spinner('Calculating probabilities...'):
                prompt = f"""
                Act as a professional football analyst like Opta or Gracenote. 
                Analyze {match} in {league}.
                Provide:
                1. Win Probability (1X2) in %
                2. Correct Score Prediction
                3. Over/Under 2.5 Goals probability
                4. Both Teams to Score (BTTS) Yes/No
                5. Top 3 Confidence Reasons.
                Use English language. Format with bold numbers.
                """
                response = model.generate_content(prompt)
                st.markdown("---")
                st.markdown(response.text)
                st.markdown("---")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 SmartOdds Global")
