import streamlit as st

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 3. CSS: MİLİMETRİK HİZALAMA VE FULL GENİŞLİK ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    /* Konteynırı daraltıp her şeyi içine hapsediyoruz ki sağa sola kaymasın */
    .block-container {
        padding-top: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 500px !important; /* Mobil için ideal genişlik sabitleyici */
    }

    /* Üst Başlık - Genişlik %100 */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 15px; border-radius: 20px; text-align: center; 
        margin-bottom: 20px; width: 100%; box-sizing: border-box;
    }

    /* Kolonları ve Butonları Hizala */
    div[data-testid="stHorizontalBlock"] {
        gap: 10px !important;
        margin: 0px !important;
        padding: 0px !important;
        width: 100% !important;
    }

    div[data-testid="stColumn"] {
        padding: 0px !important;
        margin: 0px !important;
    }

    /* Buton Tasarımı */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 22px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08) !important;
        width: 100% !important;
        height: 160px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.2s ease !important;
    }
    
    div.stButton > button p {
        font-weight: 800 !important;
        font-size: 22px !important;
        line-height: 1.2 !important;
    }

    /* Çizgiyi de hizalayalım */
    hr { margin-top: 1rem !important; margin-bottom: 1rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL (Hizalanmış) ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık</h1><p>Ayvalık Tatil Rehberiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 HİZALANMIŞ GRID ---
# Satır 1
c1, c2 = st.columns(2)
with c1:
    if st.button("📍\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
        st.rerun()
with c2:
    if st.button("🤖\nAsistan", key="btn_asistan"):
        st.session_state.secili_sayfa = "asistan"
        st.rerun()

# Satır 2
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

# --- 6. İÇERİK ---
sayfa = st.session_state.secili_sayfa
if sayfa == "rehber":
    st.info("📍 Rehber içeriği burada görünecek.")
elif sayfa == "asistan":
    st.chat_message("assistant").write("Selam! Ayvalık hakkında ne bilmek istersin?")
    st.chat_input("Buraya yaz...")
# ... (Diğerleri aynı şekilde devam eder)
