import streamlit as st
import google.generativeai as genai
from datetime import datetime
import random

# --- 1. YAPILANDIRMA ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        if "model" not in st.session_state:
            st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. GELİŞMİŞ GÖRSEL TASARIM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f0f2f6; }
    
    /* Ana Başlık */
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white; padding: 30px 20px; border-radius: 25px;
        text-align: center; margin-bottom: 25px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    /* Kare Menü Kartları */
    .menu-container {
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-bottom: 25px;
    }
    .menu-card {
        background: white; padding: 25px 15px; border-radius: 20px;
        text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: all 0.3s ease; border: 1px solid #eee; cursor: pointer;
    }
    .menu-card:hover {
        transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-color: #2a5298;
    }
    .menu-icon { font-size: 40px; margin-bottom: 10px; display: block; }
    .menu-title { font-weight: 800; color: #2c3e50; font-size: 16px; }
    .menu-sub { font-size: 11px; color: #7f8c8d; margin-top: 5px; }

    /* Bilgi Kartları */
    .info-card {
        background: white; padding: 18px; border-radius: 15px;
        border-left: 5px solid #2a5298; margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    /* Sekme Tasarımı */
    .stTabs [data-baseweb="tab"] { height: 50px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VERİ VE MANTIK ---
BILGI_BANKASI = {
    "yemek": {"anahtarlar": ["yemek", "ne yiyelim", "acıktım", "restoran", "pizza"], "cevap": "🍕 **Pizza:** Cunda Uno.\n🥪 **Tost:** Tostuyevski.\n🍝 **Akşam:** Pizza Teos veya Tino."},
    "tost": {"anahtarlar": ["tost", "tostçu"], "cevap": "Ayvalık'ta tost denince **Tostuyevski** tek geçer!"},
    "plaj": {"anahtarlar": ["plaj", "deniz", "beach"], "cevap": "🏖️ **Öneri:** Badavut Koyu veya Ortunç Koyu."},
}

def yanıt_uret(soru):
    soru_low = soru.lower()
    for kategori, icerik in BILGI_BANKASI.items():
        if any(anahtar in soru_low for anahtar in icerik["anahtarlar"]): return icerik["cevap"]
    try:
        sys_msg = "Sen Detayvalık Villa asistanı samimi bir Ayvalıklısın. Kısa cevap ver."
        response = st.session_state.model.generate_content(f"{sys_msg}\n\nSoru: {soru}")
        return response.text
    except:
        return "Selam dostum! Şu an biraz yoğunum, rehber sekmelerime göz atabilirsin!"

# --- 4. ARAYÜZ BAŞLANGIÇ ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Rehberi</h1><p>Ayvalık Tatilini Güzelleştirelim</p></div>', unsafe_allow_html=True)

# --- 5. GÖRSEL KARE MENÜ (GİYDİRME) ---
# Session State ile sayfa kontrolü
if "active_tab" not in st.session_state:
    st.session_state.active_tab = 0

st.markdown("""
    <div class="menu-container">
        <div class="menu-card">
            <span class="menu-icon">📍</span>
            <span class="menu-title">Rehber</span>
            <span class="menu-sub">Lezzet & Plajlar</span>
        </div>
        <div class="menu-card">
            <span class="menu-icon">🤖</span>
            <span class="menu-title">Asistan</span>
            <span class="menu-sub">Yapay Zeka Sohbet</span>
        </div>
        <div class="menu-card">
            <span class="menu-icon">🎉</span>
            <span class="menu-title">Etkinlik</span>
            <span class="menu-sub">Konser & Ajanda</span>
        </div>
        <div class="menu-card">
            <span class="menu-icon">💊</span>
            <span class="menu-title">Eczane</span>
            <span class="menu-sub">Nöbetçi Listesi</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 6. İÇERİK SEKMELERİ ---
t_rehber, t_ai, t_etkinlik, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "🎉 Etkinlik", "💊 Eczane"])

with t_rehber:
    st.markdown(f"""<div class="info-card">💡 <b>Günün Önerisi:</b><br>{random.choice(["Badavut'ta gün batımı!", "Tostuyevski'de karışık!", "Kaktüs Cunda'da kahve!"])}</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="info-card" style="border-left-color: #2c3e50;">🌐 <b>Wi-Fi:</b><br>Ağ: <b>Detayvalik_Villa</b> | Şifre: <b>ayvalik2026</b></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="info-card" style="border-left-color: #e67e22;">📜 <b>Kural:</b> Gece 00:00'dan sonra sessizlik rica olunur.</div>""", unsafe_allow_html=True)

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Ayvalık hakkında sorun varsa buradayım."}]
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
    if prompt := st.chat_input("Nereye gidelim?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            cevap = yanıt_uret(prompt)
            st.markdown(cevap)
            st.session_state.messages.append({"role": "assistant", "content": cevap})

with t_etkinlik:
    st.markdown("""<div class="info-card">🎤 <b>Teoman</b><br>🗓 24 Mart 2026</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="info-card">🎸 <b>Pinhani</b><br>🗓 27 Mart 2026</div>""", unsafe_allow_html=True)

with t_eczane:
    st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
