import streamlit as st
import difflib

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı 1.3", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE (Sayfa Takibi) ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan" # İlk açılış sayfası

# --- 3. BİLGİ BANKASI ---
BILGI_BANKASI = {
    "wifi": "📶 **Wi-Fi:** Detayvalik_Villa | **Şifre:** `ayvalik2026`",
    "şifre": "📶 **Wi-Fi:** Detayvalik_Villa | **Şifre:** `ayvalik2026`",
    "giriş": "🔑 **Giriş:** 14:00 | **Çıkış:** 11:00",
    "mangal": "🍢 **Mangal:** Bahçede serbesttir. Lütfen kullandıktan sonra temiz bırakınız.",
    "plaj": "🏖️ **Plaj:** Sarımsaklı plajına yürüyerek 5 dakikadır."
}

# --- 4. CSS (LÜKS TASARIM & 2x2 SABİT GRID) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    /* 2x2 Grid Yapısı Zorlaması */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 10px !important;
    }
    div[data-testid="stColumn"] {
        flex: 1 !important;
        width: 50% !important;
    }

    /* BUTONLARIN ŞIK KART TASARIMI */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
        width: 100% !important;
        height: 140px !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1) !important;
        border-color: #2c5364 !important;
    }

    div.stButton > button p {
        font-weight: 800 !important;
        font-size: 20px !important;
        line-height: 1.2 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Asistanı</h1><p>Premium Misafir Deneyimi</p></div>', unsafe_allow_html=True)

# --- 6. 2x2 ŞIK BUTON GRİDİ ---
# Satır 1
c1, c2 = st.columns(2)
with c1:
    if st.button("🤖\nAsistan", key="btn_asistan"):
        st.session_state.secili_sayfa = "asistan"
        st.rerun()
with c2:
    if st.button("📍\nRehber", key="btn_rehber"):
        st.session_state.secili_sayfa = "rehber"
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

# --- 7. İÇERİK ALANI ---
sayfa = st.session_state.secili_sayfa

if sayfa == "asistan":
    st.subheader("🤖 Akıllı Asistan")
    if prompt := st.chat_input("Sorunuzu buraya yazın (Örn: wifi şifresi)"):
        with st.chat_message("user"): st.write(prompt)
        
        # Fuzzy Matching (Token Harcamayan Kısım)
        bulundu = False
        for anahtar in BILGI_BANKASI.keys():
            if anahtar in prompt.lower(): # Basit kontrol veya difflib eklenebilir
                with st.chat_message("assistant"):
                    st.success("✅ Bilgi Bankasından Yanıt:")
                    st.write(BILGI_BANKASI[anahtar])
                bulundu = True
                break
        
        if not bulundu:
            with st.chat_message("assistant"):
                st.info("🤖 Bu soruyu yapay zekaya aktarıyorum... (API Bağlantısı Bekleniyor)")

elif sayfa == "rehber":
