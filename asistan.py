import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
# API Anahtarın yerleştirildi
API_KEY = "AIzaSyBVh5prpNUgJXGFfDQXOhnSk5AqBz-Y5Bc"

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# AI Modelini Hazırla (Model ismini 'models/gemini-1.5-flash-latest' olarak güncelledik)
try:
    genai.configure(api_key=API_KEY)
    # En güncel ve uyumlu model ismiyle çağırıyoruz
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
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
- CAFE: Pinos Cafe Sarımsaklı, Nona Cunda, Crew Coffe.
- PLAJLAR: Ücretli (Ayvalık Sea Long, Ajlan, Kesebir, Scala), Ücretsiz (Badavut, Sarımsaklı, Ortunç).
- TARİH: Ayazma, Rahmi Koç Müzesi, Taksiyarhis, Yel Değirmeni.

Eğer evle ilgili teknik (şofben, klima vb.) soru gelirse 'Dostum teknik detaylar henüz eklenmedi, ev sahibine soralım' de.
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
    st.info("🍴 **Hızlı Öneri:** Tost için Tostuyevski, Pizza için Cunda Uno!")
    st.success("🌊 **Plaj:** Sakinlik için Badavut'u deneyin.")
    st.write("Tüm detaylar için yandaki asistanla sohbet edebilirsin.")

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
                full_request = f"{SYSTEM_PROMPT}\n\nKullanıcı: {prompt}"
                # Yanıtı daha güvenli bir yöntemle alıyoruz
                response = model.generate_content(full_request)
                
                if response:
                    # Bazı güvenlik filtrelerine takılırsa kontrol ediyoruz
                    try:
                        ai_text = response.text
                        st.markdown(ai_text)
                        st.session_state.messages.append({"role": "assistant", "content": ai_text})
                    except:
                        st.warning("Bu konuda şimdilik bilgi veremiyorum dostum, başka bir şey sorar mısın?")
                else:
                    st.warning("Yanıt alınamadı, lütfen tekrar dener misin?")
            except Exception as e:
                st.error(f"Teknik bir sorun: {str(e)}")
