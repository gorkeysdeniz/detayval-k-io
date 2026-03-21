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

# --- 2. CSS: TIKLANABİLİR KATMAN TASARIMI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 30px 10px; border-radius: 20px; text-align: center; margin-bottom: 25px; position: relative;
    }
    
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    /* Buton ve Kartı Birleştiren Kutu */
    .nav-box {
        position: relative;
        height: 120px;
        margin-bottom: 15px;
    }

    /* Görsel Kart (Altta Kalacak) */
    .menu-card {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: white; border-radius: 15px; text-align: center;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #eee;
        z-index: 1;
    }
    
    .menu-icon { font-size: 30px; display: block; }
    .menu-title { font-weight: 700; color: #2c3e50; font-size: 14px; margin-top: 5px; }
    .menu-sub { font-size: 9px; color: #95a5a6; }

    /* Görünmez Buton (Üstte Kalacak ve Tıklanacak) */
    .stButton > button {
        position: absolute; top: 0; left: 0; width: 100% !important; height: 120px !important;
        background: transparent !important; color: transparent !important;
        border: none !important; z-index: 2; cursor: pointer;
    }
    .stButton > button:hover { background: rgba(0,0,0,0.02) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "rehber"

# --- 4. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 TIKLANABİLİR MENÜ ---
col1, col2 = st.columns(2)

with col1:
    # REHBER KARTI
    st.markdown('<div class="nav-box"><div class="menu-card"><span class="menu-icon">📍</span><span class="menu-title">Rehber</span><span class="menu-sub">Lezzet & Plajlar</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_rehber"):
        st.session_state.active_tab = "rehber"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # ETKİNLİK KARTI
    st.markdown('<div class="nav-box"><div class="menu-card"><span class="menu-icon">🎉</span><span class="menu-title">Etkinlik</span><span class="menu-sub">Konser & Ajanda</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_etkinlik"):
        st.session_state.active_tab = "etkinlik"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # ASİSTAN KARTI
    st.markdown('<div class="nav-box"><div class="menu-card"><span class="menu-icon">🤖</span><span class="menu-title">Asistan</span><span class="menu-sub">Yapay Zeka Sohbet</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_asistan"):
        st.session_state.active_tab = "asistan"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # ECZANE KARTI
    st.markdown('<div class="nav-box"><div class="menu-card"><span class="menu-icon">💊</span><span class="menu-title">Eczane</span><span class="menu-sub">Nöbetçi Listesi</span></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_eczane"):
        st.session_state.active_tab = "eczane"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- 6. İÇERİK ALANI ---
tab = st.session_state.active_tab

if tab == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown(f"""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> {random.choice(["Badavut Gün Batımı", "Tostuyevski Tost", "Pinos Kahve"])}<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif tab == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    if "messages" not in st.session_state: st.session_state.messages = [{"role":"assistant","content":"Selam dostum! Ayvalık hakkında sorun varsa buradayım."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p := st.chat_input("Nereye gidelim?"):
        st.session_state.messages.append({"role":"user","content":p})
        st.rerun()

elif tab == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif tab == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
