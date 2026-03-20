import streamlit as st
import google.generativeai as genai

# --- 1. GÜVENLİ AI YAPILANDIRMASI ---
# Anahtarı Secrets'tan çekiyoruz (Artık kodda anahtar yok!)
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Lütfen Streamlit Settings > Secrets kısmına GEMINI_API_KEY ekle!")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# Model Seçici (Sabit Hafıza)
if "ai_model" not in st.session_state:
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_models = ['models/gemini-1.5-flash', 'models/gemini-pro']
        chosen_model = next((m for m in target_models if m in available_models), available_models[0])
        st.session_state.ai_model = genai.GenerativeModel(chosen_model)
    except Exception as e:
        st.error(f"Bağlantı Hatası: {str(e)}")

# --- 2. SİSTEM TALİMATI ---
SYSTEM_INSTRUCTION = "Sen Detayvalık Villa asistanısın. Samimi, Ayvalıklı bir dostsun. Tostuyevski, Cunda Uno, Kaktüs Cunda favorindir. İlk mesaj dışında kendini tanıtma."

# --- 3. TASARIM & KAYMA ENGELLEYİCİ ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai = st.tabs(["📍 Rehber", "🤖 Akıllı Asistan"])

with t_rehber:
    st.info("🍴 Favoriler: Tostuyevski, Cunda Uno, Kaktüs Cunda.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili her şeyi bana sorabilirsin dostum!"}]

    # MESAJLARI SABİT TUTAN KONTEYNER
    chat_container = st.container()

    # Kullanıcı girişi (En altta sabit)
    if prompt := st.chat_input("Sor bakalım dostum..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Yanıt üretme
        try:
            history = st.session_state.messages[-3:] # Hafızayı taze tutmak için son 3 mesaj
            context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
            response = st.session_state.ai_model.generate_content(f"{SYSTEM_INSTRUCTION}\n\n{context}\nAsistan:")
            if response.text:
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except:
            st.error("Ufak bir takılma oldu.")

    # Tüm mesajları konteyner içinde göster (Kaymayı bu engeller)
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
