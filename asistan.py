import streamlit as st
import difflib

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "rehber"

# --- 3. BİLGİ BANKASI (Hızlı Yanıtlar) ---
BILGI_BANKASI = {
    "wifi": "📶 **Wi-Fi Bilgileri:**\nAğ Adı: Detayvalik_Villa\nŞifre: `ayvalik2026`",
    "şifre": "📶 **Wi-Fi Bilgileri:**\nAğ Adı: Detayvalik_Villa\nŞifre: `ayvalik2026`",
    "giriş": "🔑 **Giriş/Çıkış Saatleri:**\nGiriş: 14:00\nÇıkış: 11:00",
    "mangal": "🍢 **Mangal:** Bahçede mangal ekipmanımız mevcuttur.",
    "plaj": "🏖️ **Plaj:** Sarımsaklı plajına yürüyerek 5 dakikadır."
}

# --- 4. CSS TASARIM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    div[data-testid="stHorizontalBlock"] { display: flex !important; gap: 10px !important; }
    div[data-testid="stColumn"] { flex: 1 !important; width: 50% !important; }

    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 25px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1) !important;
        width: 100% !important;
        height: 150px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    div.stButton > button p {
        font-weight: 800 !important;
        font-size: 22px !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 6. 2x2 SABİT GRID ---
r1_c1, r1_c2 = st.columns(2)
with r1_c1:
    if st.button("📍\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
        st.rerun()
with r1_c2:
    if st.button("🤖\nAsistan", key="btn_asistan"):
        st.session_state.secili_sayfa = "asistan"
        st.rerun()

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

# --- 7. İÇERİK ALANI (HATA BURADAYDI, DÜZELTİLDİ) ---
sayfa = st.session_state.secili_sayfa

if sayfa == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown("""<div style="background:white; padding:20px; border-radius:15px; border-left:5px solid #2c5364;">
    💡 <b>Günün Önerisi:</b> Badavut Sahili'nde gün batımı.<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif sayfa == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    
    if prompt := st.chat_input("Sorunu yaz (Örn: ntrenr şifresi)..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Fuzzy Matching Kontrolü
        cevap_bulundu = False
        for k in prompt.lower().split():
            eslesme = difflib.get_close_matches(k, BILGI_BANKASI.keys(), n=1, cutoff=0.6)
            if eslesme:
                with st.chat_message("assistant"):
                    st.success("✅ Bilgi Bankası Yanıtı:")
                    st.write(BILGI_BANKASI[eslesme[0]])
                cevap_bulundu = True
                break
        
        if not cevap_bulundu:
            with st.chat_message("assistant"):
                st.warning("🤖 Bu soruyu Yapay Zekaya sormam gerekiyor (API Bağlantısı Bekleniyor...)")

elif sayfa == "etkinlik":
    st.subheader("🎉 Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri")

elif sayfa == "eczane":
    st.subheader("💊 Eczaneler")
    st.link_button("Nöbetçi Eczaneler", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
