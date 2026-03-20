import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=API_KEY)
    else:
        st.error("Secrets kısmında API anahtarı bulunamadı!")
except Exception as e:
    st.error(f"Yapılandırma Hatası: {e}")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# Model Başlatma (Hata payını azaltmak için kontrol ekledik)
if "ai_model" not in st.session_state:
    try:
        st.session_state.ai_model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Model başlatılamadı: {e}")

# --- 2. SİSTEM TALİMATI ---
SYSTEM_INSTRUCTION = """
Sen Detayvalık Villa asistanısın. Ayvalıklı samimi bir dostsun. 
BİLGİLER: Tostuyevski, Cunda Uno, Kaktüs Cunda favorindir. 
KURAL: Kısa, samimi ve öz cevaplar ver. İlk mesaj hariç kendini tanıtma.
"""

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "💊 Eczane"])

with t_rehber:
    st.info("🍴 Favoriler: Tostuyevski, Cunda Uno, Kaktüs Cunda.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Ayvalık hakkında ne bilmek istersin?"}]

    # MESAJLARI GÖSTER
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # KULLANICI GİRİŞİ
    if prompt := st.chat_input("Sor bakalım..."):
        # Kullanıcı mesajını anında ekrana bas ve hafızaya al
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)

        # AI YANITI ÜRET
        with chat_container:
            with st.chat_message("assistant"):
                try:
                    # Sadece son 2 mesajı gönderiyoruz (Hata riskini azaltmak için en hafif hali)
                    history = st.session_state.messages[-2:]
                    context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
                    
                    full_prompt = f"{SYSTEM_INSTRUCTION}\n\nGeçmiş:\n{context}\nSoru: {prompt}"
                    
                    response = st.session_state.ai_model.generate_content(full_prompt)
                    
                    if response and response.text:
                        ai_reply = response.text
                        st.markdown(ai_reply)
                        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                    else:
                        st.warning("Boş yanıt döndü, lütfen tekrar sormayı dener misin?")
                except Exception as e:
                    # Hatayı daha net görebilmek için teknik mesajı da ekledik
                    st.error(f"Ufak bir takılma: {str(e)[:50]}... Lütfen tekrar yazar mısın?")

with t_eczane:
    st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
