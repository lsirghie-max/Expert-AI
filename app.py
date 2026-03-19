import streamlit as st
import google.generativeai as genai

# Configurare pagină
st.set_page_config(page_title="SmartOdds AI", page_icon="⚽")

# --- PARTEA CEA MAI IMPORTANTĂ: CHEIA API ---
# Verificăm dacă cheia este setată în secțiunea Secrets a Streamlit Cloud
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ Eroare: Cheia API nu este setată în Streamlit Secrets!")
    st.info("Mergi la Manage App -> Settings -> Secrets și adaugă: GOOGLE_API_KEY = 'CHEIA_TA'")

# Interfața aplicației
st.title("⚽ SmartOdds AI Engine")
st.subheader("Analiză Privată Pronosticuri")

# Opțiuni pentru utilizator
liga = st.selectbox("Alege Liga:", ["Champions League", "Premier League", "Liga 1 RO", "La Liga", "Serie A", "Bundesliga", "Altele"])
meci = st.text_input("Introdu Meciul (Ex: FCSB - Rapid)")

# Butonul de generare
if st.button("🚀 GENEREAZĂ ANALIZA"):
    if meci:
        with st.spinner('AI-ul analizează statisticile...'):
            try:
                # Instrucțiunile pentru AI
                prompt = f"""
                Ești un expert în pariuri sportive. Analizează meciul {meci} din {liga}.
                Oferă:
                1. Probabilități 1X2 în procente.
                2. Pont HT/FT (Pauză/Final).
                3. Scor corect probabil.
                4. O scurtă argumentare.
                Răspunde în limba română.
                """
                
                response = model.generate_content(prompt)
                
                # Afișarea rezultatului
                st.success("✅ Analiza este gata!")
                st.markdown("---")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"A apărut o eroare: {e}")
    else:
        st.warning("Te rog să scrii numele meciului!")

# Footer
st.markdown("---")
st.caption("© 2026 SmartOdds AI Engine")
