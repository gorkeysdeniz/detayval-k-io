import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
API_KEY = "AIzaSyBVh5prpNUgJXGFfDQXOhnSk5AqBz-Y5Bc"

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# AI Modelini Hazırla
try:
    genai.configure(api_key=API_KEY)
    # Model ismini 'gemini-1.5-flash' olarak sabitledik
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("AI Yapılandırma Hatası!")

# --- 2. ASİSTANIN HAFIZASI (PROMPT) ---
SYSTEM_PROMPT = """
Sen Detayvalık Villa'nın dijital asistanısın. Adın 'Detayvalık AI'. 
İLK CÜMLEN ŞUDUR: "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin."

KARAKTERİN: İlk cümlen resmi olsun ama devamında çok samimi, yardımsever, Ayvalık'ın tozunu yutmuş bir dost gibi konuş. 'Dostum', 'Keyifli tatiller' gibi ifadeler kullan.

BİLGİLERİN:
- TOST: Tostuyevski, Aşkın Tost Evi, Tadım Tost Evi.
- PİZZA: Cunda Uno, Küçük İtalya Küçükköy, Pizza Teos, Tino Pizza.
- KOKTEYL: Kaktüs Cunda, Ciello Cunda, Luna Cunda, Rituel1873.
- CAFELER: Pinos Cafe Sarımsaklı, Nona Cunda, Crew Coffe.
- PLAJLAR: Ücretli (Ayvalık Sea Long, Ajlan, Kesebir, Scala), Ücretsiz (Badavut, Sarımsaklı, Ortunç).
- TARİHİ YERLER: Ayazma, Rahmi Koç Müzesi, Taksiyarhis Kilisesi, Yel Değirmeni.
"""

# --- 3. TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #FDFDFD; }
    .main-header { 
        background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); 
        color: white; padding: 25px; border-radius: 20px; text-align: center; 
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# Sekmeler
t_rehber, t_ai = st.tabs(["📍 Rehber", "🤖 Akıllı Asistan"])

with t_rehber:
    st.info("🍴 **Tost:** Tostuyevski & Aşkın Tost Evi favorimizdir.")
    st.success("🌊 **Plaj:** Sakinlik için Badavut'u deneyin.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin."}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Dostum aklına takılanı sor..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # generate_content'i en yalın haliyle çağırıyoruz
                response = model.generate_content(f"{SYSTEM_PROMPT}\n\nKullanıcı: {prompt}")
                
                # Yanıtın içinde text olup olmadığını kontrol ediyoruz
                if response and hasattr(response, 'text'):
                    ai_text = response.text
                    st.markdown(ai_text)
                    st.session_state.messages.append({"role": "assistant", "content": ai_text})
                else:
                    st.warning("Dostum, yanıtı oluştururken bir takılma oldu. Lütfen tekrar sor.")
            except Exception as e:
                # Hata 404 ise alternatif bir model denemesi yapalım (Opsiyonel ama güvenli)
                st.error(f"Teknik bir sorun oluştu. Hata: {str(e)}")
