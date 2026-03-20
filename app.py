import streamlit as st
import google.generativeai as genai

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(page_title="QUANTUM HUB PRO", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #ffffff; }
    .match-card { background-color: #101c2a; padding: 20px; border-radius: 12px; border-left: 5px solid #00ff9d; margin-bottom: 15px; }
    .prediction-value { color: #00ff9d; font-size: 18px; font-weight: bold; }
    .stButton>button { background: #00ff9d; color: black; font-weight: bold; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- CONECTARE API (VARIANTA ANTI-404) ---
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Aici e reparația: folosim 'gemini-1.5-flash' fără prefixe inutile
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Cheia API lipsește din Secrets!")
    st.stop()

# --- INTERFAȚA ---
st.title("🌐 GLOBAL SCANNER & PREDICTOR")

url_input = st.text_input("URL Link (Google Search, Flashscore etc):")

if st.button("🚀 SCAN & ANALYZE ALL"):
    if url_input:
        with st.spinner('AI is analyzing...'):
            try:
                # Testăm conexiunea cu un prompt simplu
                response = model.generate_content(f"Analyze the sports events for today from this context: {url_input}. Provide winner and score.")
                st.markdown("### 📋 REZULTATE SCANARE")
                st.write(response.text)
            except Exception as e:
                # Dacă dă eroare, încercăm metoda alternativă de nume
                try:
                    alt_model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
                    response = alt_model.generate_content(f"Analyze: {url_input}")
                    st.write(response.text)
                except:
                    st.error(f"Eroare persistente: {e}. Verifică dacă cheia API este activă în Google AI Studio!")

# --- CARDURI EXEMPLE ---
st.markdown("---")
st.subheader("📍 Live Insights")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="match-card"><b>Man City vs Arsenal</b><br><span class="prediction-value">PICK: 1 | SCORE: 2-1</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="match-card"><b>Real Madrid vs Milan</b><br><span class="prediction-value">PICK: 1 | SCORE: 3-0</span></div>', unsafe_allow_html=True)
    
