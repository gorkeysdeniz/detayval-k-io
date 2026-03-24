import streamlit as st
import difflib

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Pro Dashboard", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 3. BİLGİ BANKASI ---
BILGI_BANKASI = {
    "wifi": "📶 **Wi-Fi:** Detayvalik_Villa | **Şifre:** `ayvalik2026`",
    "şifre": "📶 **Wi-Fi:** Detayvalik_Villa | **Şifre:** `ayvalik2026`",
    "giriş": "🔑 **Giriş:** 14:00 | **Çıkış:** 11:00",
    "mangal": "🍢 **Mangal:** Bahçede serbesttir. Lütfen temiz bırakınız.",
    "plaj": "🏖️ **Plaj:** Sarımsaklı plajına yürüyerek 5 dakikadır.",
    "taksi": "🚕 **Sarımsaklı Taksi:** 0266 XXX XX XX"
}

# --- 4. CSS (PREMIUM BAŞLIK GERİ GELDİ & RENKLİ GRİD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    /* 🌟 EFSANEVİ BAŞLIK KARTI GERİ GELDİ (image_1.png'deki gibi gradyan) */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white !important; 
        padding: 30px 15px; 
        border-radius: 20px; 
        text-align: center; 
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15); /* Hafif derinlik */
    }
    .main-header h1, .main-header p {
        color: white !important; /* Yazıların beyaz kalmasını zorla */
        margin: 0;
    }

    /* Grid Konteyner */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important; 
        gap: 8px !important; 
        margin-bottom: 8px !important;
    }

    /* Sütunlar Eşit */
    div[data-testid="stColumn"] {
        padding: 0px !important;
        flex: 1 1 0% !important; 
        min-width: 0 !important;
    }

    /* BUTONLARIN YENİ "BEYAZ KART" TASARIMI (image_2.png'deki gibi) */
    div.stButton > button {
        background-color: white !important; /* Saf beyaz kart */
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
        width: 100% !important;
        height: 90px !important; 
        transition: all 0.2s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
        border-color: #2c5364 !important; /* Başlık gradyanıyla uyumlu hover rengi */
    }

    /* Emoji ve Yazı (image_2.png'deki gibi bold ve okunaklı) */
    div.stButton > button p {
        font-weight: 700 !important;
        font-size: 15px !important; 
        margin: 0 !important;
        padding: 0 !important;
        white-space: pre-line !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. ÜST PANEL (BAŞLIK İÇERİĞİ) ---
st.markdown('<div class="main-header"><h1>🏠 Detayvalık Dashboard</h1><p>Her Şey Elinizin Altında | Premium Deneyim</p></div>', unsafe_allow_html=True)

# --- 6. 4x2 GENİŞLETİLMİŞ GRİD ---
# (Yemek ikonu image_2.png'deki gibi daha estetik)
# (Kalan kodda bir değişiklik yok, içerik bloklarını kullanmaya devam edebilirsin)

# --- 7. İÇERİK ALANI ---
sayfa = st.session_state.secili_sayfa

if sayfa == "asistan":
    st.subheader("🤖 Akıllı Asistan")
    prompt = st.chat_input("Sorunuzu buraya yazın...")
    if prompt:
        with st.chat_message("user"): st.write(prompt)
        bulundu = False
        for k in prompt.lower().split():
            eslesme = difflib.get_close_matches(k, BILGI_BANKASI.keys(), n=1, cutoff=0.6)
            if eslesme:
                with st.chat_message("assistant"): st.success(BILGI_BANKASI[eslesme[0]])
                bulundu = True
                break
        if not bulundu:
            with st.chat_message("assistant"): st.info("🤖 AI sorgulanıyor...")

elif sayfa == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.write("Cunda Adası ve Şeytan Sofrası mutlaka görülmeli.")

elif sayfa == "plajlar":
    st.subheader("🏖️ En İyi Plajlar")
    st.write("1. Sarımsaklı Plajı\n2. Badavut Koyu\n3. Ortunç Koyu")

elif sayfa == "yemek":
    st.subheader("🍽️ Restoran Önerileri")
    st.write("Ayvalık Tostu ve Papalina balığını denemelisiniz.")

elif sayfa == "taksi":
    st.subheader("🚕 Ulaşım")
    st.info("📱 Sarımsaklı Taksi: 0266 XXX XX XX")

elif sayfa == "kurallar":
    st.subheader("📜 Ev Kuralları")
    st.write("- Havuz kullanımı 20:00'de sona erer.\n- Gürültü yasağı 23:00'den sonradır.")

elif sayfa == "etkinlik":
    st.subheader("🎉 Etkinlikler")
    st.write("🎤 24 Mart: Teoman Konseri (Bugün!)")

elif sayfa == "eczane":
    st.subheader("💊 Eczaneler")
    st.link_button("Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
