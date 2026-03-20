import streamlit as st
import google.generativeai as genai

# --- 1. AYARLAR & AI KURULUMU ---
# API Anahtarın buraya yerleştirildi
API_KEY = "AIzaSyBVh5prpNUgJXGFfDQXOhnSk5AqBz-Y5Bc" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. ASİSTANIN BİLGİ BANKASI (PROMPT) ---
SYSTEM_PROMPT = """
Sen Detayvalık Villa'nın dijital asistanısın. Adın 'Detayvalık AI'. 
Giriş cümlen ŞUDUR: "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin."

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
    .stTabs [data-baseweb="tab-list"] { gap: 15px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #f0f2f6; border-radius: 10px; padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Başlık
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Misafir Paneli</h1><p>Ege\'nin en akıllı rehberi yanınızda!</p></div>', unsafe_allow_html=True)

# Sekmeler
t_rehber, t_ai = st.tabs(["📍 Öne Çıkanlar", "🤖 Akıllı Asistan"])

with t_rehber:
    st.subheader("🍴 Favori Duraklarımız")
    st.info("🥪 **Tost:** Tostuyevski & Aşkın Tost Evi favorimizdir.")
    st.success("🍕 **Pizza:** Cunda Uno ve Küçük İtalya'yı denemelisiniz.")
    st.warning("🌊 **Plaj:** Sakinlik arıyorsanız Badavut Plajı tam size göre.")
    st.write("---")
    st.write("💡 Diğer tüm detaylı öneriler (cafe, kokteyl, tarih) için **Akıllı Asistan** sekmesine geçebilirsin!")

with t_ai:
    # Sohbet Geçmişi Başlatma
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin."}
        ]

    # Mesajları Görüntüle
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Kullanıcı Girdisi
    if prompt := st.chat_input("Dostum aklına takılanı sor..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Yanıt Üretme
        with st.chat_message("assistant"):
            try:
                # Geçmişi de içeren bir prompt yapısı
                full_context = f"{SYSTEM_PROMPT}\n\nSoru: {prompt}"
                response = model.generate_content(full_context)
                ai_response = response.text
                st.markdown(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            except Exception as e:
                st.error("Ufak bir teknik sorun oluştu, lütfen biraz sonra tekrar dene.")
