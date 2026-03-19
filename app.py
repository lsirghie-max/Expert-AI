import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="SmartOdds AI", page_icon="⚽")

# Cheia ta API
YOUR_API_KEY = "AIzaSyDtpJqV1PF5yKOQz1HjrqbU3L-NMrrCY54" 
genai.configure(api_key=YOUR_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("⚽ SmartOdds AI Engine")
st.subheader("Analiză Privată Pronosticuri")

campionat = st.selectbox("Liga:", ["Champions League", "Europa League", "Premier League", "Serie A", "Liga 1 RO"])
meci = st.text_input("Meciul (Ex: Roma - Bologna)")

if st.button("GENEREAZĂ ANALIZA"):
    if meci:
        with st.spinner('Analizez datele...'):
            prompt = f"Analizează meciul {meci} din {campionat}. Oferă probabilități 1X2, un pont HT/FT și scor corect probabil."
            response = model.generate_content(prompt)
            st.success("Rezultat:")
            st.write(response.text)
    else:
        st.warning("Scrie numele echipelor!")
