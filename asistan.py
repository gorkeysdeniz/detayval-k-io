import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
API_KEY = "AIzaSyAAKsLmaKOGS6p352gNbeQVRanTHiNOG-8"

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# Dinamik Model Seçici (404 Hatasını Bitiren Kısım)
if "ai_model" not in st.session_state:
    try:
        genai.configure(api_key=API_KEY)
        # Mevcut modelleri listele ve en uygununu seç
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Öncelik sırasına göre dene: 1.5 Flash -> 1.5 Pro -> Pro
        target_models = ['models/gemini-1.5-flash', 'models/gemini-1.5-pro', 'models/gemini-pro']
        chosen_model = next((m for m in target_models if m in available_models), available_models[0])
        
        st.session_state.ai_model = genai.GenerativeModel(chosen_model)
    except Exception as e:
        st.error(f"Bağlantı Kurulamadı: {str(e)}")

# --- 2. ASİSTANIN HAFIZASI ---
SYSTEM_PROMPT = """
Sen Detayvalık Villa'nın dijital asistanısın. Adın 'Detayvalık AI'. 
Giriş cümlen: "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin."
Mekanlar: Tostuyevski, Aşkın Tost Evi, Cunda Uno, Küçük İtalya, Kaktüs Cunda, Badavut Plajı.
Karakterin: İlk cümle resmi, sonrası çok samimi Ayvalıklı bir dost.
"""

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai = st.tabs(["📍 Rehber", "🤖 Akıllı Asistan"])

with t_rehber:
    st.info("🍴 Tost için Tostuyevski, Pizza için Cunda Uno favorimiz!")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin."}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("Sor bakalım dostum..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # Hafızadaki modeli kullan
                response = st.session_state.ai_model.generate_content(f"{SYSTEM_PROMPT}\nSoru: {prompt}")
                if response.text:
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Bir takılma oldu: {str(e)}")
