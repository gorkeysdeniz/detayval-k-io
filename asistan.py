import streamlit as st
import random

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. CSS: 2x2 SABİT GRID & BUTONLAR ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 25px;
    }
    
    /* Butonları Kare Karta Dönüştüren CSS */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
        width: 100% !important;
        height: 140px !important;
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
        font-size: 16px !important;
        margin-top: 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE (Gizle-Göster Mantığı) ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 4. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 BUTON MENÜSÜ ---
col1, col2 = st.columns(2)

with col1:
    if st.button("📍\n\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
        st.rerun() # Sadece içeriği yenilemek için
    
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

st.divider()

# --- 6. İÇERİK ALANI (Gizle / Göster Komutu) ---

if st.session_state.secili_sayfa == "rehber":
    with st.container():
        st.subheader("📍 Ayvalık Rehberi")
        st.markdown("""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
        💡 <b>Günün Önerisi:</b> Badavut Sahili<br><br>
        🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
        </div>""", unsafe_allow_html=True)

elif st.session_state.secili_sayfa == "asistan":
    with st.container():
        st.subheader("🤖 Detayvalık AI Asistan")
        st.info("Sohbet ekranı buraya gelecek...")

elif st.session_state.secili_sayfa == "etkinlik":
    with st.container():
        st.subheader("🎉 Yaklaşan Etkinlikler")
        st.info("🎤 24 Mart: Teoman | 🎸 27 Mart: Pinhani")

elif st.session_state.secili_sayfa == "eczane":
    with st.container():
        st.subheader("💊 Nöbetçi Eczaneler")
        st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
