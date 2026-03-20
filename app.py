import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="QUANTUM PRO", layout="wide")

# CODUL DE AVARIE - CHEIA ESTE DEJA AICI
genai.configure(api_key="AIzaSyAFXbkQDtHJRxdyFVHvSMftI_jPRGaid44")
model = genai.GenerativeModel("gemini-1.5-flash")

st.markdown("<style>.stApp { background-color: #050a0f; color: white; } .card { background-color: #101c2a; padding: 20px; border-radius: 15px; border-left: 5px solid #00ff9d; margin-bottom: 20px; }</style>", unsafe_allow_html=True)

st.title("🌐 QUANTUM SCANNER")

url = st.text_input("Lipește link-ul aici:")

if st.button("🚀 ANALIZEAZĂ"):
    if url:
        with st.spinner("AI-ul lucrează..."):
            try:
                res = model.generate_content(f"Analizează meciurile de aici: {url}. Dă-mi: Meci, Predicție, Scor și Încredere %.")
                st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Eroare: {e}")

st.subheader("📍 Predicții Live")
st.markdown("<div class='card'><b>Real Madrid vs Milan</b><br><span style='color:#00ff9d'>PICK: 1 | SCOR: 3-1 | 90%</span></div>", unsafe_allow_html=True)
