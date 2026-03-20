import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta
import random

# --- 1. YAPILANDIRMA ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("API Key Eksik!")
except:
    st.error("Bağlantı Hatası!")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. VERİ TABANI (Öncelikli Bilgiler) ---
BILGI_BANKASI = {
    "yemek": {
        "anahtarlar": ["yemek", "ne yiyelim", "acıktım", "restoran", "mutfak", "lezzet"],
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

# --- 3. TASARIM (BÜYÜK MENÜLER) ---
st.markdown("""<style>
    .main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab"] { height: 70px; font-size: 18px !important; font-weight: bold; }
</style>""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_etkinlik, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "🎉 Etkinlik", "💊 Eczane"])

# --- 4. AKILLI CEVAP MOTORU ---
def yanıt_uret(soru):
    soru_low = soru.lower()
    
    # ADIM 1: Önce Bilgi Bankasında ara (Hızlı ve Kota Dostu)
    for kategori, icerik in BILGI_BANKASI.items():
        if any(anahtar in soru_low for anahtar in icerik["anahtarlar"]):
            return icerik["cevap"]
    
    # ADIM 2: Eğer listede yoksa AI'ya sor (Zekice cevaplar için)
    try:
        sys_msg = "Sen Detayvalık Villa asistanı samimi bir Ayvalıklısın. Soru senin bilmediğin bir şeyse kibarca 'bilmiyorum' demek yerine genel bir cevap ver."
        response = model.generate_content(f"{sys_msg}\n\nSoru: {soru}")
        return response.text
    except:
        return "Dostum şu an biraz dalgınım, tekrar sorar mısın?"

# --- SEKMELER ---
with t_rehber:
    st.info("💡 **Günün Önerisi:** Badavut'ta gün batımını izlemeden dönme!")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Hoş geldin. Ayvalık hakkında ne bilmek istersin?"}]
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("Sor bakalım..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        cevap = yanıt_uret(prompt)
        
        with st.chat_message("assistant"): st.markdown(cevap)
        st.session_state.messages.append({"role": "assistant", "content": cevap})

with t_etkinlik:
    st.subheader("📅 Yaklaşan Konserler")
    # Dinamik etkinlik kodun buraya gelecek (v3.7'deki gibi)
    st.write("24.03.2026 - Teoman")
    st.write("27.03.2026 - Pinhani")

with t_eczane:
    st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
