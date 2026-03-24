import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. DURUM TAKİBİ ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 3. BİLGİ BANKASI ---
BILGI_BANKASI = {
    "wifi": "📶 **Kablosuz Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "şifre": "📶 **Kablosuz Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "giriş": "🔑 **Giriş Saati:** 14:00  \n🚪 **Çıkış Saati:** 11:00",
    "mangal": "🍢 **Mangal Keyfi:** Bahçede mangal ekipmanımız hazırdır. Lütfen kullanımdan sonra söndüğünden emin olun.",
    "plaj": "🏖️ **Deniz & Plaj:** Sarımsaklı plajı yürüyerek sadece 5 dakika mesafededir.",
    "taksi": "🚕 **Ulaşım:** Sarımsaklı Taksi: 0266 396 10 10",
    "kurallar": "📜 **Ev Düzeni:** Komşularımızı rahatsız etmemek adına 23:00'den sonra müzik sesini kısmanızı rica ederiz."
}

# --- 4. CSS (DÜZELTİLMİŞ VE EKSİKSİZ) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .stApp { background-color: #f4f7f9; font-family: 'Inter', sans-serif; }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white !important;
        padding: 35px 20px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
    }
    .main-header h1 { font-weight: 800; font-size: 30px; margin: 0; color: white !important; }
    .main-header p { font-weight: 400; font-size: 15px; opacity: 0.85; color: white !important; margin-top: 10px; }

    div[data-testid="stHorizontalBlock"] { gap: 10px !important; margin-bottom: 10px !important; }

    div.stButton > button {
        background: white !important;
        color: #1a2a3a !important;
        border: 1px solid #eee !important;
        border-radius: 18px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
        width: 100% !important;
        height: 100px !important; 
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
        border-color: #2c5364 !important;
    }

    div.stButton > button p {
        font-weight: 700 !important;
        font-size: 15px !important;
    }

    .content-box {
        background: white;
        padding: 20px;
        border-radius: 20px;
        border-left: 5px solid #2c5364;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Konaklama Rehberi</p></div>', unsafe_allow_html=True)

# --- 6. GRİD ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🤖\nAsistan", key="m1"): 
        st.session_state.secili_sayfa = "asistan"
        st.rerun()
with c2:
    if st.button("📍\nRehber", key="m2"): 
        st.session_state.secili_sayfa = "rehber"
        st.rerun()
with c3:
    if st.button("🏖️\nPlajlar", key="m3"): 
        st.session_state.secili_sayfa = "plajlar"
        st.rerun()
with c4:
    if st.button("🍽️\nYemek", key="m4"): 
        st.session_state.secili_sayfa = "yemek"
        st.rerun()

c5, c6, c7, c8 = st.columns(4)
with c5:
    if st.button("🎉\nEtkinlik", key="m5"): 
        st.session_state.secili_sayfa = "etkinlik"
        st.rerun()
with c6:
    if st.button("💊\nEczane", key="m6"): 
        st.session_state.secili_sayfa = "eczane"
        st.rerun()
with c7:
    if st.button("🚕\nTaksi", key="m7"): 
        st.session_state.secili_sayfa = "taksi"
        st.rerun()
with c8:
    if st.button("📜\nKurallar", key="m8"): 
        st.session_state.secili_sayfa = "kurallar"
        st.rerun()

st.divider()

# --- 7. SAYFA İÇERİKLERİ ---
sayfa = st.session_state.secili_sayfa

if sayfa == "asistan":
    st.markdown("### 🤖 Size Nasıl Yardımcı Olabilirim?")
    prompt = st.chat_input("Sorunuzu yazın...")
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
            with st.chat_message("assistant"): st.info("🤖 Bu konuyu hemen yapay zekaya iletiyorum...")

elif sayfa == "rehber":
    st.markdown('<div class="content-box"><h3>📍 Keşif Rehberi</h3>Cunda Adası ve Şeytan Sofrası listenizde olmalı.</div>', unsafe_allow_html=True)

elif sayfa == "plajlar":
    st.markdown('<div class="content-box"><h3>🏖️ Plaj Önerileri</h3>Sarımsaklı ve Badavut Koyu en popüler noktalar.</div>', unsafe_allow_html=True)

elif sayfa == "taksi":
    st.markdown('<div class="content-box"><h3>🚕 Ulaşım</h3><b>Sarımsaklı Taksi:</b> 0266 396 10 10</div>', unsafe_allow_html=True)

elif sayfa == "kurallar":
    st.markdown('<div class="content-box"><h3>📜 Ev Kuralları</h3>Check-out saati 11:00\'dir. İyi tatiller!</div>', unsafe_allow_html=True)
