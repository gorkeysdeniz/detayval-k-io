import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
# Yeni API Anahtarın buraya yerleştirildi
API_KEY = "AIzaSyAAKsLmaKOGS6p352gNbeQVRanTHiNOG-8"

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# AI Modelini Hazırla
try:
    genai.configure(api_key=API_KEY)
    # En stabil ve güncel model ismi
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("AI Yapılandırma Hatası!")

# --- 2. ASİSTANIN HAFIZASI (PROMPT) ---
SYSTEM_PROMPT = """
Sen Detayvalık Villa'nın dijital asistanısın. Adın 'Detayvalık AI'. 
İLK CÜMLEN ŞUDUR: "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin."

KARAKTERİN: İlk cümlen her zaman yukarıdaki gibi resmi olsun. Ancak kullanıcı cevap verdikten sonra çok samimi, yardımsever, Ayvalık'ın tozunu yutmuş bir dost gibi konuş. 'Dostum', 'Keyifli tatiller', 'Ayvalık'ın tadını çıkar' gibi samimi ifadeler kullan.

BİLGİ BANKAN (Senin favori mekanların):
- TOSTÇULAR: Tostuyevski, Aşkın Tost Evi, Tadım Tost Evi. (Gerçek Ayvalık tostu bunlardır de).
- PİZZACILAR: Cunda Uno, Küçük İtalya Küçükköy, Pizza Teos, Tino Pizza Ristorante.
- KOKTEYL & GECE: Kaktüs Cunda, Ciello Cunda, Luna Cunda, Rituel1873.
- CAFELER: Pinos Cafe Sarımsaklı, Nona Cunda, Crew Coffe.
- PLAJLAR (Ücretli): Ayvalık Sea Long, Ajlan Beach, Kesebir Beach, Scala Beach.
- PLAJLAR (Ücretsiz): Badavut Plajı (Rüzgarlı havalarda bile çarşaf gibidir), Sarımsaklı Plajı, Ortunç Koyu.
- TARİHİ YERLER: Ayvalık Ayazması, Rahmi Koç Müzesi, Taksiyarhis Kilisesi, Yel Değirmeni.

TEKNİK KONULAR: Evin teknik detayları henüz sisteme girilmedi. Eğer evle ilgili (şofben, anahtar, klima bozuk vb.) teknik soru gelirse: 
'Dostum bu teknik detayları henüz hafızama atmadık, ev sahibimize WhatsApp üzerinden sormanı rica ederim.' de.
"""

# --- 3. TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #FDFDFD; }
    .main-header { 
        background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); 
        color: white; padding: 25px; border-radius: 20px; text-align: center; 
        margin-bottom: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# Sekmeler
t_rehber, t_ai = st.tabs(["📍 Öne Çıkanlar", "🤖 Akıllı Asistan"])

with t_rehber:
    st.info("🥪 **Tost:** Tostuyevski & Aşkın Tost Evi favorimizdir.")
    st.success("🍕 **Pizza:** Cunda Uno ve Küçük İtalya'yı denemelisiniz.")
    st.warning("🌊 **Plaj:** Sakinlik için Badavut Plajı tam size göre.")

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
                # Modeli en basit haliyle çağırıyoruz
                response = model.generate_content(f"{SYSTEM_PROMPT}\n\nSoru: {prompt}")
                
                if response and hasattr(response, 'text'):
                    ai_text = response.text
                    st.markdown(ai_text)
                    st.session_state.messages.append({"role": "assistant", "content": ai_text})
                else:
                    st.warning("Yanıt alınamadı, lütfen tekrar dener misin?")
            except Exception as e:
                st.error(f"Teknik bir sorun: {str(e)}")
