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

# --- 2. GELİŞMİŞ CSS (Görünmez Butonlar & Temizlik) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    /* Orijinal menüleri tamamen gizle */
    .stTabs [data-baseweb="tab-list"] { display: none !important; }
    
    /* Ana Başlık */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 30px 20px; border-radius: 25px;
        text-align: center; margin-bottom: 25px; position: relative;
    }
    
    .beta-badge {
        position: absolute; top: 10px; right: 15px;
        background: rgba(255,255,255,0.2); padding: 2px 8px;
        border-radius: 10px; font-size: 10px;
    }
    
    /* Kare Menü Tasarımı */
    .menu-card {
        background: white; padding: 30px 10px; border-radius: 20px;
        text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border: 1px solid #eee; margin-bottom: -45px; /* Butonun üzerine binmesi için */
    }
    .menu-icon { font-size: 35px; display: block; margin-bottom: 5px; }
    .menu-title { font-weight: 700; color: #2c3e50; font-size: 15px; }
    .menu-sub { font-size: 10px; color: #95a5a6; display: block; }

    /* Butonları Görünmez Yapma (Kartın üzerine yayma) */
    .stButton>button {
        height: 120px !important;
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        width: 100% !important;
        z-index: 10;
        position: relative;
    }
    .stButton>button:hover { background-color: rgba(0,0,0,0.02) !important; }

    .info-card {
        background: white; padding: 15px; border-radius: 15px;
        border-left: 5px solid #2c5364; margin-top: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "📍 Rehber"

def change_tab(name):
    st.session_state.active_tab = name

# --- 4. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. TIKLANABİLİR KARE MENÜ (Görünmez Butonlarla) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="menu-card"><span class="menu-icon">📍</span><span class="menu-title">Rehber</span><span class="menu-sub">Lezzet & Plajlar</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_rehber"):
        st.session_state.active_tab = "📍 Rehber"
        st.rerun()

    st.markdown('<div class="menu-card"><span class="menu-icon">🎉</span><span class="menu-title">Etkinlik</span><span class="menu-sub">Konser & Ajanda</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_etkinlik"):
        st.session_state.active_tab = "🎉 Etkinlik"
        st.rerun()

with col2:
    st.markdown('<div class="menu-card"><span class="menu-icon">🤖</span><span class="menu-title">Asistan</span><span class="menu-sub">Yapay Zeka Sohbet</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_asistan"):
        st.session_state.active_tab = "🤖 Asistan"
        st.rerun()

    st.markdown('<div class="menu-card"><span class="menu-icon">💊</span><span class="menu-title">Eczane</span><span class="menu-sub">Nöbetçi Listesi</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_eczane"):
        st.session_state.active_tab = "💊 Eczane"
        st.rerun()

st.divider()

# --- 6. İÇERİK MANTIĞI ---
if st.session_state.active_tab == "📍 Rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown(f"""<div class="info-card">💡 <b>Günün Önerisi:</b> {random.choice(["Badavut Gün Batımı", "Tostuyevski Tost", "Pinos Kahve"])}</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="info-card">🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026</div>""", unsafe_allow_html=True)

elif st.session_state.active_tab == "🤖 Asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    if "msgs" not in st.session_state: st.session_state.msgs = [{"role":"assistant","content":"Selam! Nereye gidelim?"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p := st.chat_input("Sor bakalım..."):
        st.session_state.msgs.append({"role":"user","content":p})
        with st.chat_message("user"): st.markdown(p)
        # Basit yanıt mekanizması
        res = "Harika fikir! Ayvalık'ta bunu yapmak çok keyifli olacaktır." 
        st.session_state.msgs.append({"role":"assistant","content":res})
        st.rerun()

elif st.session_state.active_tab == "🎉 Etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("24 Mart: Teoman Konseri | 27 Mart: Pinhani")

elif st.session_state.active_tab == "💊 Eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
