import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="SmartOdds AI", page_icon="⚽")

# Configurare API directă din Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Lipsește cheia API din Secrets!")

st.title("⚽ SmartOdds AI Engine")
st.subheader("Analiză Privată Pronosticuri")

liga = st.selectbox("Alege Liga:", ["Liga 1 RO", "Champions League", "Premier League", "Serie A", "La Liga", "Bundesliga"])
meci = st.text_input("Introdu Meciul (Ex: Dinamo - Craiova)")

if st.button("🚀 GENEREAZĂ ANALIZA"):
    if meci:
        with st.spinner('AI-ul analizează statisticile...'):
            try:
                # Folosim direct modelul flash - cea mai simplă metodă
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Ești expert în pariuri. Analizează meciul {meci} din {liga}. Oferă probabilități 1X2, pont HT/FT și scor corect. Răspunde în română."
                
                response = model.generate_content(prompt)
                
                st.success("✅ Analiza finalizată!")
                st.markdown("---")
                st.write(response.text)
                    
            except Exception as e:
                st.error(f"Eroare tehnică: {str(e)}")
    else:
        st.warning("Te rog scrie echipele!")

st.markdown("---")
st.caption("© 2026 SmartOdds AI Engine")
