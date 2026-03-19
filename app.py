import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="SmartOdds AI", page_icon="⚽")

# Verificăm dacă cheia există în Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Folosim 'gemini-pro' pentru stabilitate maximă
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("Eroare: Cheia API nu este setată în Streamlit Secrets!")

st.title("⚽ SmartOdds AI Engine")
st.subheader("Analiză Privată Pronosticuri")

liga = st.selectbox("Alege Liga:", ["Liga 1 RO", "Champions League", "Premier League", "La Liga", "Serie A", "Bundesliga", "Altele"])
meci = st.text_input("Introdu Meciul (Ex: Dinamo - Craiova)")

if st.button("🚀 GENEREAZĂ ANALIZA"):
    if meci:
        with st.spinner('AI-ul analizează statisticile...'):
            try:
                prompt = f"Analizează meciul {meci} din {liga}. Oferă probabilități 1X2, un pont HT/FT și scor corect probabil. Răspunde în română."
                response = model.generate_content(prompt)
                st.success("✅ Analiza finalizată!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Eroare AI: {e}")
    else:
        st.warning("Te rog introdu echipele.")

st.markdown("---")
st.caption("© 2026 SmartOdds AI Engine")
