import streamlit as st
import random

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE (Sayfa Takibi) ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 3. CSS: SABİT 2x2 DÜZEN VE BUTON TASARIMI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 25px;
    }

    /* 2x2 Yerleşimi Sağlayan Kap (Flexbox) */
    .menu-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        margin-bottom: 20px;
    }

    /* Her bir butonun alanı (Genişliği %48 yaparak yan yana 2 tane sığdırıyoruz) */
    .menu-container {
        width: 48%; 
        min-width: 140px;
    }

    /* Streamlit Butonlarını Karta Dönüştür */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
        width: 100% !important;
        height: 120px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.2s ease !important;
    }
    
    div.stButton > button:active {
        transform: scale(0.95) !important;
        background-color: #f8f9fa !important;
    }

    div.stButton > button p {
        font-weight: 700 !important;
        font-size: 15px !important;
        white-space: pre-wrap !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. SABİT 2x2 BUTON MENÜSÜ ---
# HTML Wrapper kullanarak butonları hizalıyoruz
st.markdown('<div class="menu-wrapper">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("📍\n\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
        st.rerun()
    
    if st.button("🎉\n\nEtkinlik", key="btn_etkinlik"):
        st.session_state.secili_sayfa = "etkinlik"
        st.rerun()

with col2:
    if st.button("🤖\n\nAsistan", key="btn_asistan"):
        st.session_state.secili_sayfa = "asistan"
        st.rerun()
    
    if st.button("💊\n\nEczane", key="btn_eczane"):
        st.session_state.secili_sayfa = "eczane"
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- 6. İÇERİK ALANI (Anında Geçiş) ---
sayfa = st.session_state.secili_sayfa

if sayfa == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown("""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> Badavut Sahili'nde yürüyüş.<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif sayfa == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    st.chat_message("assistant").write("Selam dostum! Ayvalık hakkında ne bilmek istersin?")
    st.chat_input("Sorunu buraya yaz...")

elif sayfa == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif sayfa == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
