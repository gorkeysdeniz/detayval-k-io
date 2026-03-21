import streamlit as st

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 3. CSS: MAKSİMUM DOLGULUK VE 2x2 SABİTLEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    /* Mobilde 2x2 Düzenini ve Genişliğini Zorla */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 10px !important;
        padding: 0px !important;
    }
    div[data-testid="stColumn"] {
        flex: 1 !important;
        width: 50% !important;
        min-width: 48% !important;
    }

    /* BUTONLARI TAM KUTU YAPMA */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 25px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1) !important;
        width: 100% !important;
        height: 180px !important; /* Yükseklik dengelendi */
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0px !important; /* İç boşluğu sıfırlayıp metne yer açtık */
    }
    
    div.stButton > button:active { transform: scale(0.96) !important; }
    
    /* Emoji ve Yazıyı Devleştir */
    div.stButton > button p {
        font-weight: 800 !important;
        font-size: 24px !important; /* YAZILAR İYİCE BÜYÜDÜ */
        line-height: 1.2 !important;
        margin: 0 !important;
        padding-top: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 SABİT GRID ---
# İlk Satır: Rehber ve Asistan
r1_c1, r1_c2 = st.columns(2)
with r1_c1:
    if st.button("📍\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
        st.rerun()
with r1_c2:
    if st.button("🤖\nAsistan", key="btn_asistan"):
        st.session_state.secili_sayfa = "asistan"
        st.rerun()

# İkinci Satır: Etkinlik ve Eczane
r2_c1, r2_c2 = st.columns(2)
with r2_c1:
    if st.button("🎉\nEtkinlik", key="btn_etkinlik"):
        st.session_state.secili_sayfa = "etkinlik"
        st.rerun()
with r2_c2:
    if st.button("💊\nEczane", key="btn_eczane"):
        st.session_state.secili_sayfa = "eczane"
        st.rerun()

st.divider()

# --- 6. İÇERİK ALANI ---
sayfa = st.session_state.secili_sayfa

if sayfa == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown("""<div style="background:white; padding:20px; border-radius:15px; border-left:5px solid #2c5364;">
    💡 <b>Günün Önerisi:</b> Badavut Sahili'nde gün batımı.<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif sayfa == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    st.chat_message("assistant").write("Selam! Ayvalık hakkında ne bilmek istersin?")
    st.chat_input("Sorunu yaz dostum...")

elif sayfa == "etkinlik":
    st.subheader("🎉 Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri")

elif sayfa == "eczane":
    st.subheader("💊 Eczaneler")
    st.link_button("Nöbetçi Eczaneler", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
