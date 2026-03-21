import streamlit as st

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 3. CSS: DEVASA BUTONLAR VE MOBİL SABİTLEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    /* Mobilde 2x2 düzenini zorla (Sıra bozulmasını engeller) */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 12px !important;
    }
    div[data-testid="stColumn"] {
        flex: 1 !important;
        width: 50% !important;
        min-width: 45% !important;
    }

    /* BUTONLARI BÜYÜTME VE DOLGUNLAŞTIRMA */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 25px !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
        width: 100% !important;
        height: 200px !important; /* YÜKSEKLİK ARTIRILDI */
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 20px !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:active { transform: scale(0.95) !important; box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important; }
    
    /* İçerik Fontları */
    div.stButton > button p {
        font-weight: 800 !important;
        font-size: 22px !important; /* YAZILAR BÜYÜTÜLDÜ */
        line-height: 1.8 !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 GRID DÜZENİ ---
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
    st.markdown("""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> Badavut Sahili'nde gün batımı.<br><br>
    🌐 <b>Wi-Fi Adı:</b> Detayvalik_Villa<br>
    🔑 <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif sayfa == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    st.chat_message("assistant").write("Selam! Ayvalık hakkında ne bilmek istersin? Restoran önerileri mi, plajlar mı yoksa ev kuralları mı?")
    st.chat_input("Sorunu buraya yaz...")

elif sayfa == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif sayfa == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
