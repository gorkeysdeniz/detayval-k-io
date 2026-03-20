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

# Model Seçici - Sadece bir kez çalışır
if "ai_model" not in st.session_state:
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_models = ['models/gemini-1.5-flash', 'models/gemini-pro']
        chosen_model = next((m for m in target_models if m in models), models[0])
        st.session_state.ai_model = genai.GenerativeModel(chosen_model)
    except Exception as e:
        st.error(f"Bağlantı Hatası: {e}")

# --- 2. SİSTEM TALİMATI ---
SYSTEM_INSTRUCTION = "Sen Detayvalık Villa asistanısın. Samimi, Ayvalıklı bir dostsun. İlk mesaj hariç kendini tanıtma. Kısa cevap ver."

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "💊 Eczane"])

with t_rehber:
    st.info("🍴 Favoriler: Tostuyevski, Cunda Uno, Kaktüs Cunda.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Ayvalık hakkında ne bilmek istersin?"}]

    # Mesajları gösteren ana kutu
    chat_box = st.container()

    # Önce eski mesajları ekrana bas
    with chat_box:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Kullanıcıdan yeni mesaj al
    if prompt := st.chat_input("Sor bakalım dostum..."):
        # Kullanıcı mesajını hemen ekrana ve hafızaya ekle
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_box.chat_message("user"):
            st.markdown(prompt)
        
        # AI Yanıtı Üretme (Kota dostu yöntem)
        try:
            with chat_box.chat_message("assistant"):
                # Sadece son 2 mesajı gönder (Kotaları korur)
                history = st.session_state.messages[-2:]
                context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
                
                response = st.session_state.ai_model.generate_content(f"{SYSTEM_INSTRUCTION}\n\n{context}")
                
                if response and response.text:
                    ai_reply = response.text
                    st.markdown(ai_reply)
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        except Exception as e:
            if "429" in str(e):
                st.error("Dostum çok hızlı sordun, Google biraz dinlenmemi istiyor. 30 saniye sonra tekrar dener misin?")
            else:
                st.error(f"Ufak bir takılma: {str(e)[:50]}")

with t_eczane:
    st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
