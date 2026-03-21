import streamlit as st
import google.generativeai as genai
import random

# --- 1. YAPILANDIRMA ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        if "model" not in st.session_state:
            st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. CSS: 2x2 IZGARA VE TIKLANABİLİR KARTLAR ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 30px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px; position: relative;
    }
    
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    /* 2x2 Izgara Yapısı */
    .menu-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    /* Kart Tasarımı */
    .menu-card {
        background: white;
        padding: 20px 10px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #eee;
        text-decoration: none !important;
        display: block;
        transition: transform 0.2s;
    }
    .menu-card:active { transform: scale(0.95); background-color: #f0f0f0; }
    
    .menu-icon { font-size: 30px; display: block; margin-bottom: 5px; }
    .menu-title { font-weight: 700; color: #2c3e50; font-size: 14px; display: block; }
    .menu-sub { font-size: 9px; color: #95a5a6; display: block; }

    /* Streamlit bileşenlerini temizle */
    .stTabs [data-baseweb="tab-list"] { display: none !important; }
    div[data-testid="stVerticalBlock"] > div { border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TIKLAMA MANTIĞI (Query Parametresi ile) ---
# URL'deki parametreye göre sekmeyi belirle
query_params = st.query_params
active_tab = query_params.get("tab", "rehber")

# --- 4. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 KARE MENÜ (TIKLANABİLİR) ---
# Her kart bir <a> linki içerir ve URL'ye ?tab=... ekler
st.markdown(f"""
    <div class="menu-grid">
        <a href="/?tab=rehber" target="_self" class="menu-card">
            <span class="menu-icon">📍</span>
            <span class="menu-title">Rehber</span>
            <span class="menu-sub">Lezzet & Plajlar</span>
        </a>
        <a href="/?tab=asistan" target="_self" class="menu-card">
            <span class="menu-icon">🤖</span>
            <span class="menu-title">Asistan</span>
            <span class="menu-sub">Yapay Zeka Sohbet</span>
        </a>
        <a href="/?tab=etkinlik" target="_self" class="menu-card">
            <span class="menu-icon">🎉</span>
            <span class="menu-title">Etkinlik</span>
            <span class="menu-sub">Konser & Ajanda</span>
        </a>
        <a href="/?tab=eczane" target="_self" class="menu-card">
            <span class="menu-icon">💊</span>
            <span class="menu-title">Eczane</span>
            <span class="menu-sub">Nöbetçi Listesi</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. İÇERİK ALANI (Tıklanan Karta Göre Değişir) ---
if active_tab == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown(f"""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> {random.choice(["Badavut Gün Batımı", "Tostuyevski Tost", "Pinos Kahve"])}<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif active_tab == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    if "msgs" not in st.session_state: st.session_state.msgs = [{"role":"assistant","content":"Selam! Ayvalık hakkında ne bilmek istersin?"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p := st.chat_input("Sor bakalım..."):
        st.session_state.msgs.append({"role":"user","content":p})
        st.rerun()

elif active_tab == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("24 Mart: Teoman Konseri | 27 Mart: Pinhani")

elif active_tab == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
