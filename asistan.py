import streamlit as st

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 3. CSS: GERÇEK 2x2 GRID (ST.COLUMNS KULLANMADAN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    /* BURASI SİHİRLİ NOKTA: Gerçek 2x2 Izgara */
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr; /* Her zaman 2 sütun */
        gap: 12px;
        margin-bottom: 20px;
    }

    /* Görünmez Buton Katmanı */
    .stButton > button {
        height: 140px !important;
        width: 100% !important;
        border-radius: 20px !important;
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08) !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        display: flex !important;
        flex-direction: column !important;
        transition: all 0.2s !important;
    }
    
    .stButton > button:active { transform: scale(0.95) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 BUTON DÜZENİ (GRID İÇİNDE) ---
# Grid konteynerini başlatıyoruz
st.markdown('<div class="grid-container">', unsafe_allow_html=True)

# Streamlit her butonu kendi div'ine koyduğu için grid otomatik çalışacaktır.
# Ancak Streamlit'in butonları alt alta koymasını engellemek için grid-container içine doğrudan butonları basıyoruz.
c1, c2, c3, c4 = st.columns([1,1,1,1]) # Bu sadece boşluk ayarı için, CSS ile ezeceğiz.

# Ama daha garanti bir yol: Butonları tek tek sütunlara koyup o sütunları CSS ile yan yana kilitlemek.
grid_col1, grid_col2 = st.columns(2)

with grid_col1:
    if st.button("📍\n\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
        st.rerun()
    if st.button("🎉\n\nEtkinlik", key="btn_etkinlik"):
        st.session_state.secili_sayfa = "etkinlik"
        st.rerun()

with grid_col2:
    if st.button("🤖\n\nAsistan", key="btn_asistan"):
        st.session_state.secili_sayfa = "asistan"
        st.rerun()
    if st.button("💊\n\nEczane", key="btn_eczane"):
        st.session_state.secili_sayfa = "eczane"
        st.rerun()

# CSS ile st.columns'un mobilde kırılmasını engelleme (Nihai Darbe)
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important; /* Yan yana kal */
        flex-wrap: nowrap !important; /* Alt satıra geçme */
        gap: 10px !important;
    }
    [data-testid="stColumn"] {
        flex: 1 !important;
        min-width: 45% !important; /* Genişliği koru */
    }
    </style>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. İÇERİK ALANI ---
sayfa = st.session_state.secili_sayfa

if sayfa == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.info("💡 Badavut'ta gün batımını kaçırma! | Wi-Fi: Detayvalik_Villa")

elif sayfa == "asistan":
    st.subheader("🤖 AI Asistan")
    st.chat_input("Sorunu yaz dostum...")

elif sayfa == "etkinlik":
    st.subheader("🎉 Etkinlikler")
    st.success("Bu hafta: Cunda'da açık hava sineması var!")

elif sayfa == "eczane":
    st.subheader("💊 Eczaneler")
    st.link_button("Nöbetçi Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
