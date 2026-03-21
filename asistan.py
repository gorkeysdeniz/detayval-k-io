import streamlit as st
import google.generativeai as genai
from datetime import datetime
import random

# --- 1. YAPILANDIRMA VE HATA YÖNETİMİ ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        if "model" not in st.session_state:
            st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("⚠️ Gemini API Key 'secrets.toml' dosyasında bulunamadı!")
except Exception as e:
    st.error(f"⚠️ Bağlantı Hatası: {e}")

st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. GELİŞMİŞ GÖRSEL TASARIM (CSS Beta 1.2 Güncellemesi) ---
# BURAYA DİKKAT: Eski sekmeleri (Orijinal Menü) gizleyen ve yeni kartları tıklanabilir gösteren CSS.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f0f2f6; }
    
    /* Eski Streamlit sekmelerini (Orijinal Menü) gizle */
    .stTabs [data-baseweb="tab-border"] { display: none !important; }
    .stTabs [data-baseweb="tab"] { display: none !important; }
    .stTabs [aria-selected="true"] { display: none !important; }
    
    /* Ana Başlık */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 30px 20px; border-radius: 25px;
        text-align: center; margin-bottom: 25px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        position: relative;
    }
    
    /* Beta İbaresi */
    .beta-badge {
        position: absolute; top: 10px; right: 10px;
        background-color: rgba(255, 255, 255, 0.2);
        color: white; padding: 4px 10px; border-radius: 20px;
        font-size: 11px; font-weight: 600;
    }
    
    /* Kare Menü Kartları */
    .menu-container {
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-bottom: 25px;
    }
    .menu-card {
        background: white; padding: 25px 15px; border-radius: 20px;
        text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: all 0.3s ease; border: 1px solid #eee;
    }
    .menu-card:hover {
        transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-color: #2c5364;
    }
    .menu-icon { font-size: 40px; margin-bottom: 10px; display: block; }
    .menu-title { font-weight: 800; color: #2c3e50; font-size: 16px; }
    .menu-sub { font-size: 11px; color: #7f8c8d; margin-top: 5px; }

    /* Bilgi Kartları (Eski tasarımdan) */
    .info-card {
        background: white; padding: 18px; border-radius: 15px;
        border-left: 5px solid #4F6F52; margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03); color: #333;
    }
    
    /* Sekme İçeriklerinin Duruşu */
    .stTabs [data-baseweb="tab-panel"] { border: none !important; padding: 0 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VERİ VE SOHBET MANTIĞI (Aynı kalıyor) ---
BILGI_BANKASI = {
    "yemek": {"anahtarlar": ["yemek", "restoran", "pizza"], "cevap": "🍕 Pizza Teos veya Tino.\n🥪 Tostuyevski."},
    "tost": {"anahtarlar": ["tost", "tostçu"], "cevap": "Ayvalık'ta Tostuyevski efsanedir!"},
    "plaj": {"anahtarlar": ["plaj", "deniz"], "cevap": "🏖️ Badavut veya Ortunç Koyu."},
}

def yanıt_uret(soru):
    soru_low = soru.lower()
    for kategori, icerik in BILGI_BANKASI.items():
        if any(anahtar in soru_low for anahtar in icerik["anahtarlar"]): return icerik["cevap"]
    try:
        sys_msg = "Sen Detayvalık Villa asistanı samimi bir Ayvalıklısın. Kısa cevap ver."
        response = st.session_state.model.generate_content(f"{sys_msg}\n\nSoru: {soru}")
        return response.text
    except: return "Dostum şu an dalgınım ama rehber sekmelerime bakabilirsin!"

# --- 4. ARAYÜZ BAŞLANGIÇ & MENÜ MANTIĞI ---
# Session State ile sayfa kontrolü
if "active_tab_index" not in st.session_state:
    st.session_state.active_tab_index = 0

# Ana Başlık ve Beta İbaresi
st.markdown('<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. GÖRSEL KARE MENÜ (GİYDİRME) ---
# BURAYA DİKKAT: Kartları sadece HTML ile değil, Streamlit butonları ile sarmaladık.
col1, col2 = st.columns(2)

with col1:
    # Rehber Kartı
    st.markdown('<div class="menu-card"><span class="menu-icon">📍</span><span class="menu-title">Rehber</span><span class="menu-sub">Lezzet & Plajlar</span></div>', unsafe_allow_html=True)
    if st.button("Rehbere Git", key="b_rehber", use_container_width=True):
        st.session_state.active_tab_index = 0

    # Etkinlik Kartı
    st.markdown('<div class="menu-card"><span class="menu-icon">🎉</span><span class="menu-title">Etkinlik</span><span class="menu-sub">Konser & Ajanda</span></div>', unsafe_allow_html=True)
    if st.button("Etkinliklere Bak", key="b_etkinlik", use_container_width=True):
        st.session_state.active_tab_index = 2

with col2:
    # Asistan Kartı
    st.markdown('<div class="menu-card"><span class="menu-icon">🤖</span><span class="menu-title">Asistan</span><span class="menu-sub">Yapay Zeka Sohbet</span></div>', unsafe_allow_html=True)
    if st.button("Asistanla Konuş", key="b_asistan", use_container_width=True):
        st.session_state.active_tab_index = 1

    # Eczane Kartı
    st.markdown('<div class="menu-card"><span class="menu-icon">💊</span><span class="menu-title">Eczane</span><span class="menu-sub">Nöbetçi Listesi</span></div>', unsafe_allow_html=True)
    if st.button("Eczaneyi Ara", key="b_eczane", use_container_width=True):
        st.session_state.active_tab_index = 3

st.divider() # Kare Menü ile içerik arasına ince bir çizgi

# --- 6. İÇERİK SEKMELERİ (GİZLİ AMA ÇALIŞIYOR) ---
# active_tab_index'e göre sekme içeriğini manuel kontrol edeceğiz.
tabs = st.tabs(["📍 Rehber", "🤖 Asistan", "🎉 Etkinlik", "💊 Eczane"])

# REHBER İÇERİĞİ
with tabs[0]:
    if st.session_state.active_tab_index == 0:
        st.markdown(f"""<div class="info-card">💡 <b>Günün Önerisi:</b><br>{random.choice(["Badavut'ta gün batımı!", "Tostuyevski'de karışık!", "Kaktüs Cunda'da kahve!"])}</div>""", unsafe_allow_html=True)
        st.markdown("""<div class="info-card" style="border-left-color: #2c5364;">🌐 <b>Wi-Fi Bilgileri:</b><br>Ağ: <b>Detayvalik_Villa</b> | Şifre: <b>ayvalik2026</b></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="info-card" style="border-left-color: #a04747;">📜 <b>Konaklama Kurallarımız:</b><br>• 🤫 Gece 00:00'dan sonra sessizlik rica olunur.</div>""", unsafe_allow_html=True)

# ASİSTAN İÇERİĞİ
with tabs[1]:
    if st.session_state.active_tab_index == 1:
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Ayvalık hakkında ne bilmek istersin?"}]
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
        if prompt := st.chat_input("Nereye gidelim?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            with st.chat_message("assistant"):
                cevap = yanıt_uret(prompt)
                st.markdown(cevap)
                st.session_state.messages.append({"role": "assistant", "content": cevap})

# ETKİNLİK İÇERİĞİ
with tabs[2]:
    if st.session_state.active_tab_index == 2:
        st.markdown("""<div class="info-card">🎤 <b>Teoman Konseri</b><br>🗓 24 Mart 2026</div>""", unsafe_allow_html=True)
        st.markdown("""<div class="info-card">🎸 <b>Pinhani</b><br>🗓 27 Mart 2026</div>""", unsafe_allow_html=True)

# ECZANE İÇERİĞİ
with tabs[3]:
    if st.session_state.active_tab_index == 3:
        st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
