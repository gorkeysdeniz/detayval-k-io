import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
API_KEY = "AIzaSyAAKsLmaKOGS6p352gNbeQVRanTHiNOG-8"

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

if "ai_model" not in st.session_state:
    try:
        genai.configure(api_key=API_KEY)
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_models = ['models/gemini-1.5-flash', 'models/gemini-1.5-pro', 'models/gemini-pro']
        chosen_model = next((m for m in target_models if m in available_models), available_models[0])
        st.session_state.ai_model = genai.GenerativeModel(chosen_model)
    except Exception as e:
        st.error(f"Bağlantı Hatası: {str(e)}")

# --- 2. SİSTEM TALİMATI (PROMPT) ---
# Burası botun beyni, ama kullanıcıya gösterilmez
SYSTEM_INSTRUCTION = """
Sen Detayvalık Villa'nın samimi asistanısın. Adın 'Detayvalık AI'. 
KARAKTERİN: Çok yardımsever ve Ayvalıklı bir dost gibi konuş. 'Dostum', 'Keyifli tatiller' gibi ifadeler kullan.
BİLGİLERİN: Tostuyevski, Aşkın Tost Evi, Cunda Uno, Küçük İtalya, Kaktüs Cunda, Badavut Plajı vb.
KURAL: Her seferinde kendini tanıtma! Zaten ilk mesajda tanıttın. Direkt soruya samimi cevap ver.
"""

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai = st.tabs(["📍 Hızlı Rehber", "🤖 Akıllı Asistan"])

with t_rehber:
    st.info("🍴 **Favorilerimiz:** Tostuyevski, Cunda Uno, Kaktüs Cunda.")

with t_ai:
    # --- SOHBET HAFIZASI ---
    if "messages" not in st.session_state:
        # Sadece İLK mesajda kendini tanıtır
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili her şeyi bana sorabilirsin dostum!"}]

    # Mesajları ekrana bas
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Kullanıcı girişi
    if prompt := st.chat_input("Sor bakalım dostum..."):
        # Kullanıcı mesajını hafızaya ekle ve ekrana bas
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Yanıtı
        with st.chat_message("assistant"):
            try:
                # Önceki 5 mesajı hafıza olarak gönderiyoruz ki konudan kopmasın
                history = st.session_state.messages[-5:]
                formatted_history = "\n".join([f"{m['role']}: {m['content']}" for m in history])
                
                full_query = f"{SYSTEM_INSTRUCTION}\n\nSohbet Geçmişi:\n{formatted_history}\n\nYeni Soru: {prompt}\nCevap:"
                
                response = st.session_state.ai_model.generate_content(full_query)
                
                if response.text:
                    ai_reply = response.text
                    st.markdown(ai_reply)
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            except Exception as e:
                st.error("Ufak bir takılma oldu dostum, tekrar dener misin?")
