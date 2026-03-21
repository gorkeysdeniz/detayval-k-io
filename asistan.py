import streamlit as st
import random

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. CSS: 2x2 GRID & ŞIK TASARIM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px; position: relative;
    }
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    /* 2x2 Sabit Izgara */
    .menu-container {
        display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px;
    }
    
    /* Gerçek Butonları Kart Gibi Giydir */
    div.stButton > button {
        background-color: white !important; color: #2c3e50 !important;
        border: 1px solid #eee !important; border-radius: 15px !important;
        padding: 25px 10px !important; height: 110px !important; width: 100% !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05) !important;
        display: flex !important; flex-direction: column !important;
        align-items: center !important; justify-content: center !important;
    }
    div.stButton > button:active { transform: scale(0.95) !important; background-color: #f0f2f6 !important; }
    div.stButton > button p { font-weight: 700 !important; font-size: 15px !important; line-height: 1.2 !important; }

    /* Orijinal sekmeleri gizle ama işlevini koru */
    .stTabs [data-baseweb="tab-list"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = 0

# --- 4. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 BUTON DÜZENİ (ANINDA TEPKİ) ---
col1, col2 = st.columns(2)

with col1:
    if st.button("📍\nRehber", key="btn_rehber"):
        st.session_state.active_tab = 0
        st.rerun()
    if st.button("🎉\nEtkinlik", key="btn_etkinlik"):
        st.session_state.active_tab = 2
        st.rerun()

with col2:
    if st.button("🤖\nAsistan", key="btn_asistan"):
        st.session_state.active_tab = 1
        st.rerun()
    if st.button("💊\nEczane", key="btn_eczane"):
        st.session_state.active_tab = 3
        st.rerun()

st.divider()

# --- 6. İÇERİK ALANI (TABS MANTIĞI AMA GİZLİ) ---
# st.tabs kullanarak içeriği önceden yüklüyoruz, bu hız kazandırır.
tabs = st.tabs(["Rehber", "Asistan", "Etkinlik", "Eczane"])

# Seçili sekmeyi Session State'e göre göster
current_tab = tabs[st.session_state.active_tab]

with tabs[0]:
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown("""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364;">
    💡 <b>Günün Önerisi:</b> Badavut Gün Batımı!<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

with tabs[1]:
    st.subheader("🤖 Detayvalık AI Asistan")
    st.chat_message("assistant").write("Selam! Ayvalık hakkında ne bilmek istersin?")
    st.chat_input("Sorunu buraya yaz...")

with tabs[2]:
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman | 🎸 27 Mart: Pinhani")

with tabs[3]:
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
