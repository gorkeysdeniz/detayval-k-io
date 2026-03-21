import streamlit as st

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 3. CSS: DEV BUTONLAR VE SABİT 2x2 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    /* Mobilde 2x2'yi zorla ve kolonları genişlet */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important; /* Aradaki boşluğu biraz daralttık ki butonlara yer kalsın */
    }
    div[data-testid="stColumn"] {
        flex: 1 !important;
        width: 50% !important;
        min-width: 48% !important;
    }

    /* Heybetli Buton Tasarımı */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08) !important;
        width: 100% !important;
        height: 180px !important; /* BOYUTU BURADAN BÜYÜTTÜK */
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0px !important;
    }
    
    div.stButton > button:active { transform: scale(0.98) !important; }
    
    /* Emoji ve Metin Boyutu */
    div.stButton > button p {
        font-weight: 800 !important;
        font-size: 20px !important; /* Yazı fontunu büyüttük */
        line-height: 1.6 !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. BÜYÜTÜLMÜŞ 2x2 GRID ---
# Üst Sıra
c1, c2 = st.columns(2)
with c1:
    if st.button("📍\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
        st.rerun()
with c2:
    if st.button("🤖\nAsistan", key="btn_asistan"):
        st.session_state.secili_sayfa = "asistan"
        st.rerun()

# Alt Sıra
c3, c4 = st.columns(2)
with c3:
    if st.button("🎉\nEtkinlik", key="btn_etkinlik"):
        st.session_state.secili_sayfa = "etkinlik"
        st.rerun()
with c4:
    if st.button("💊\nEczane", key="btn_eczane"):
        st.session_state.secili_sayfa = "eczane"
        st.rerun()

st.divider()

# --- 6. İÇERİK ALANI ---
sayfa = st.session_state.secili_sayfa

if sayfa == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown("""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364;">
    💡 <b>Günün Önerisi:</b> Badavut'ta gün batımı.<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif sayfa == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    st.chat_message("assistant").write("Selam! Ayvalık hakkında ne bilmek istersin?")
    st.chat_input("Sorunu buraya yaz...")

elif sayfa == "etkinlik":
    st.subheader("🎉 Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri")

elif sayfa == "eczane":
    st.subheader("💊 Eczaneler")
    st.link_button("Nöbetçi Eczaneler", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
