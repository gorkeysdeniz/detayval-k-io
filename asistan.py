import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta
import random

# --- 1. YAPILANDIRMA ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Model tanımlamasını bir kez yapıyoruz
        if "model" not in st.session_state:
            st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("API Key Eksik!")
except:
    st.error("Bağlantı Hatası!")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. VERİ TABANI ---
BILGI_BANKASI = {
    "yemek": {
        "anahtarlar": ["yemek", "ne yiyelim", "acıktım", "restoran", "mutfak", "lezzet", "açım"],
        "cevap": "Dostum Ayvalık'ta aç kalman imkansız! \n\n• **Tost:** Tostuyevski (Favorim).\n• **Pizza:** Cunda Uno veya Küçük İtalya.\n• **Tatlı:** Nona Cunda.\n• **Akşam:** Pizza Teos veya Tino Pizza."
    },
    "tost": {
        "anahtarlar": ["tost", "tostçu", "tostuyevski", "aşkın"],
        "cevap": "Ayvalık'ta tost denince akla gelen ilk yer **Tostuyevski**! Ayrıca **Aşkın Tost Evi** de efsanedir."
    },
    "cafe": {
        "anahtarlar": ["cafe", "kahve", "tatlı", "kafe", "coffee", "pinos", "nona", "crew"],
        "cevap": "Kahve molası için favorilerim: \n\n• **Pinos Cafe:** Villaya çok yakın.\n• **Nona Cunda:** Tatlıları harika.\n• **Crew Coffee:** Modern kahve.\n• **Kaktüs Cunda:** En sevdiğim!"
    },
    "plaj": {
        "anahtarlar": ["plaj", "deniz", "beach", "yüzme", "badavut", "sarımsaklı"],
        "cevap": "**Ücretsiz:** Badavut (Favorim!), Sarımsaklı ve Ortunç Koyu. \n**Ücretli:** Ayvalık Sea Long, Ajlan, Kesebir ve Scala Beach."
    }
}

# --- 3. TASARIM ---
st.markdown("""<style>
    .main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab"] { height: 70px; font-size: 18px !important; font-weight: bold; }
</style>""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_etkinlik, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "🎉 Etkinlik", "💊 Eczane"])

# --- 4. AKILLI CEVAP MOTORU ---
def yanıt_uret(soru):
    soru_low = soru.lower()
    for kategori, icerik in BILGI_BANKASI.items():
        if any(anahtar in soru_low for anahtar in icerik["anahtarlar"]):
            return icerik["cevap"]
    try:
        sys_msg = "Sen Detayvalık Villa asistanı samimi bir Ayvalıklısın. Kısa ve öz cevap ver."
        response = st.session_state.model.generate_content(f"{sys_msg}\n\nSoru: {soru}")
        return response.text
    except:
        return "Dostum şu an biraz dalgınım, tekrar sorar mısın?"

# --- SEKMELER ---
with t_rehber:
    st.info("💡 **Günün Önerisi:** Badavut'ta gün batımını izlemeden dönme!")

with t_ai:
    # 1. Mesaj hafızasını başlat
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Hoş geldin. Ayvalık hakkında ne bilmek istersin?"}]
    
    # 2. MESAJLARI GÖSTEREN SABİT KONTEYNER (KAYMAYI ÖNLER)
    chat_container = st.container()
    
    # 3. KULLANICI GİRİŞİ (HER ZAMAN EN ALTTA)
    if prompt := st.chat_input("Sor bakalım..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        # AI Yanıtını Üret
        cevap = yanıt_uret(prompt)
        st.session_state.messages.append({"role": "assistant", "content": cevap})

    # 4. KONTEYNER İÇİNDE TÜM MESAJLARI ÇİZDİR
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

with t_etkinlik:
    st.subheader("📅 Yaklaşan Konserler")
    st.write("24.03.2026 - Teoman")
    st.write("27.03.2026 - Pinhani")

with t_eczane:
    st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
