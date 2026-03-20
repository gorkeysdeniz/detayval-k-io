import streamlit as st
import google.generativeai as genai

# --- 1. GÜVENLİ AI YAPILANDIRMASI ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=API_KEY)
    else:
        st.error("Secrets kısmında API anahtarı bulunamadı!")
except Exception as e:
    st.error(f"Yapılandırma Hatası: {e}")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# Model Seçici (En kararlı çalışan modeli bulur)
if "ai_model" not in st.session_state:
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_models = ['models/gemini-1.5-flash', 'models/gemini-pro']
        chosen_model = next((m for m in target_models if m in models), models[0])
        st.session_state.ai_model = genai.GenerativeModel(chosen_model)
    except Exception as e:
        st.error(f"Bağlantı Hatası: {str(e)}")

# --- 2. SİSTEM TALİMATI ---
SYSTEM_INSTRUCTION = "Sen Detayvalık Villa asistanısın. Samimi, Ayvalıklı bir dostsun. Tostuyevski, Cunda Uno, Kaktüs Cunda favorindir. İlk mesaj dışında kendini tanıtma."

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "💊 Eczane"])

with t_rehber:
    st.info("🍴 Favoriler: Tostuyevski, Cunda Uno, Kaktüs Cunda.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili her şeyi bana sorabilirsin dostum!"}]

    # MESAJLARI SABİT TUTAN KONTEYNER
    chat_container = st.container()

    # Kullanıcı girişi
    if prompt := st.chat_input("Sor bakalım dostum..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        try:
            # Hafızayı taze tutmak için son mesajlar
            history = st.session_state.messages[-3:]
            context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
            
            # AI Yanıtı Üretme
            response = st.session_state.ai_model.generate_content(f"{SYSTEM_INSTRUCTION}\n\n{context}\nAsistan:")
            
            if response and response.text:
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                st.rerun() # Sayfayı tazeleyip akışı sağlar
        except Exception as e:
            st.error(f"Ufak bir takılma: {str(e)[:50]}")

    # Mesajları konteyner içinde göster (Kaymayı bu engeller)
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

with t_eczane:
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Resmi Listeyi Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
