import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta
import random

# --- 1. YAPILANDIRMA (Hata Yönetimi Geliştirildi) ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        if "model" not in st.session_state:
            st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("⚠️ Gemini API Key 'secrets.toml' dosyasında bulunamadı!")
except Exception as e:
    st.error(f"⚠️ Bağlantı Hatası: {e}")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. MODERN TASARIM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white;
        padding: 40px 20px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .info-card {
        background: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #4F6F52;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        color: #333;
    }

    .stTabs [data-baseweb="tab"] {
        height: 60px;
        font-size: 18px !important;
        font-weight: 600;
        color: #2c5364;
    }
    .stTabs [aria-selected="true"] { color: #4F6F52 !important; border-bottom: 3px solid #4F6F52 !important; }

    .stChatMessage { border-radius: 20px !important; border: none !important; background-color: #f8f9fa !important; padding: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BİLGİ BANKASI ---
BILGI_BANKASI = {
    "yemek": {
        "anahtarlar": ["yemek", "ne yiyelim", "acıktım", "restoran", "mutfak", "lezzet", "açım"],
        "cevap": "Dostum Ayvalık'ta aç kalman imkansız! \n\n🍕 **Pizza:** Cunda Uno veya Küçük İtalya.\n🥪 **Tost:** Tostuyevski (Favorim).\n🍰 **Tatlı:** Nona Cunda.\n🍝 **Akşam:** Pizza Teos veya Tino Pizza."
    },
    "tost": {
        "anahtarlar": ["tost", "tostçu", "tostuyevski", "aşkın"],
        "cevap": "Ayvalık'ta tost denince akla gelen ilk yer **Tostuyevski**! Ayrıca **Aşkın Tost Evi** ve **Tadım Tost Evi** de efsanedir."
    },
    "cafe": {
        "anahtarlar": ["cafe", "kahve", "tatlı", "kafe", "coffee", "pinos", "nona", "crew"],
        "cevap": "Kahve molası için favorilerim: \n\n☕ **Pinos Cafe:** Villaya çok yakın.\n🧁 **Nona Cunda:** Tatlıları harika.\n⚡ **Crew Coffee:** Modern kahve.\n🌵 **Kaktüs Cunda:** En sevdiğim!"
    },
    "plaj": {
        "anahtarlar": ["plaj", "deniz", "beach", "yüzme", "badavut", "sarımsaklı"],
        "cevap": "🏖️ **Ücretsiz:** Badavut (Favorim!), Sarımsaklı ve Ortunç Koyu. \n💎 **Ücretli:** Ayvalık Sea Long, Ajlan, Kesebir ve Scala Beach."
    }
}

# --- 4. AKILLI CEVAP MOTORU (HİBRİT GÜNCELLEME) ---
def yanıt_uret(soru):
    soru_low = soru.lower()
    
    # Adım 1: Bilgi Bankası Taraması
    for kategori, icerik in BILGI_BANKASI.items():
        if any(anahtar in soru_low for anahtar in icerik["anahtarlar"]):
            return icerik["cevap"]
            
    # Adım 2: Gemini ile Sosyal Zeka ve Genel Bilgi
    try:
        sys_msg = """
        Sen Detayvalık Villa'nın dijital asistanısın. Samimi, neşeli ve gerçek bir Ayvalıklı gibi konuşursun.
        - Misafir selam verirse sıcak bir karşılama yap (Selam dostum, hoş geldin vb.).
        - Eğer rehberde olmayan bir yer sorulursa Gemini bilgilerini kullan ama üslubun hep samimi kalsın.
        - Cevapların kısa, öz ve tatil modunda olsun.
        - Villanın sahibi 'dostun' gibi davran.
        """
        response = st.session_state.model.generate_content(f"{sys_msg}\n\nMisafir: {soru}")
        return response.text
    except:
        # Adım 3: Akıllı Geri Çekilme (Fallback)
        return ("Selam dostum! Şu an kısa süreli bir bağlantı sorunu yaşıyorum ama ben buradayım. "
                "İstersen sana Ayvalık'ın efsane **tostçularını**, en güzel **plajlarını** veya akşam yemeği için **restoran** önerilerimi anlatabilirim. "
                "Neyle başlayalım?")

# --- ANA EKRAN ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p style="opacity: 0.8;">Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_etkinlik, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "🎉 Etkinlik", "💊 Eczane"])

# --- SEKME 1: REHBER ---
with t_rehber:
    st.markdown(f"""<div class="info-card">💡 <b>Günün Önerisi:</b><br>{random.choice(["Badavut'ta gün batımını izlemeden dönme!", "Tostuyevski'de karışık tost denemelisin.", "Kaktüs Cunda'da kahve molası ver."])}</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="info-card" style="border-left-color: #2c5364;">🌐 <b>Wi-Fi Bilgileri:</b><br>Ağ Adı: <b>Detayvalik_Villa</b><br>Şifre: <b>ayvalik2026</b></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="info-card" style="border-left-color: #a04747;">📜 <b>Konaklama Kurallarımız:</b><br>
    • 🤫 <b>Gece 00:00'dan sonra</b> dış alanlarda gürültü yapılmaması rica olunur.<br>
    • ❄️ <b>Evden çıkarken</b> klimaların kapatılması rica olunur.<br>
    • 🚭 <b>Kapalı alanlarda</b> sigara içilmesi kesinlikle yasaktır.<br>
    • 🔑 Giriş ve çıkış saatleri için asistana danışabilirsiniz.</div>""", unsafe_allow_html=True)

# --- SEKME 2: ASİSTAN (GELİŞMİŞ SOHBET) ---
with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Detayvalık'a hoş geldin. Ayvalık'ın tadını çıkarman için sana nasıl yardımcı olabilirim?"}]
    
    # Sohbet Geçmişini Görüntüle
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Kullanıcı Girişi
    if prompt := st.chat_input("Nereye gidelim dostum?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            cevap = yanıt_uret(prompt)
            st.markdown(cevap)
            st.session_state.messages.append({"role": "assistant", "content": cevap})

# --- SEKME 3: ETKİNLİKLER ---
with t_etkinlik:
    st.subheader("📅 Yaklaşan Etkinlikler")
    st.markdown("""<div class="info-card">🎤 <b>Teoman Konseri</b><br>🗓 24 Mart 2026</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="info-card">🎸 <b>Pinhani</b><br>🗓 27 Mart 2026</div>""", unsafe_allow_html=True)

# --- SEKME 4: ECZANE ---
with t_eczane:
    st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
