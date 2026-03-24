import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. DURUM TAKİBİ ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 3. BİLGİ BANKASI (Genişletilmiş Mekan Listesi) ---
BILGI_BANKASI = {
    "wifi": "📶 **Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "şifre": "📶 **Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "giriş": "🔑 **Giriş:** 14:00 | **Çıkış:** 11:00",
    "mangal": "🍢 **Mangal:** Bahçede serbesttir. Lütfen kullandıktan sonra temiz bırakınız.",
    "kahve": "☕ **Kahve Önerisi:** Yeniçarohori (Küçükköy) sokaklarındaki butik kafeleri mutlaka deneyin. Sanatla iç içe harika bir atmosferi var.",
    "gün batımı": "🌅 **Gün Batımı:** Şeytan Sofrası'nın kalabalığına girmek yerine Yeniçarohori'de kahve eşliğinde veya Badavut'un en ucundaki kayalıklarda batırmanızı öneririz.",
    "balık": "🐟 **Restoran:** Cunda'nın kalabalığından kaçmak isterseniz Sarımsaklı'daki yerel balıkçıları tercih edebilirsiniz.",
    "plaj": "🏖️ **Plajlar:** Sarımsaklı (Halk plajı), Badavut (Sakin), Ortunç (Mavi Bayrak). **Gizli Öneri:** Badavut'un en ucundaki bakir koy.",
    "taksi": "🚕 **Sarımsaklı Taksi:** 0266 396 10 10",
    "kokteyl": "🍸 **Gece:** Cunda sahil şeridindeki kokteyl barlar akşamları oldukça keyiflidir."
}

# --- 4. CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    .stApp { background-color: #f4f7f9; font-family: 'Inter', sans-serif; }
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white !important; padding: 35px 20px; border-radius: 25px;
        text-align: center; margin-bottom: 25px; box-shadow: 0 12px 30px rgba(0,0,0,0.2);
    }
    .main-header h1 { font-weight: 800; font-size: 30px; margin: 0; color: white !important; }
    div[data-testid="stHorizontalBlock"] { gap: 10px !important; margin-bottom: 10px !important; }
    div.stButton > button {
        background: white !important; color: #1a2a3a !important;
        border: 1px solid #eee !important; border-radius: 18px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
        width: 100% !important; height: 100px !important; transition: all 0.3s ease !important;
    }
    div.stButton > button:hover { transform: translateY(-3px) !important; border-color: #2c5364 !important; }
    .content-box { background: white; padding: 25px; border-radius: 20px; border-left: 5px solid #2c5364; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }
    </style>
    """, unsafe_allow_html=True)

# --- 5. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Mekanlar, Lezzetler ve Gizli Rotalar</p></div>', unsafe_allow_html=True)

# --- 6. 4x2 GRİD ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🤖\nAsistan", key="m1"): st.session_state.secili_sayfa = "asistan"; st.rerun()
with c2:
    if st.button("🍽️\nYemek", key="m2"): st.session_state.secili_sayfa = "yemek"; st.rerun()
with c3:
    if st.button("☕\nKahve", key="m3"): st.session_state.secili_sayfa = "kahve"; st.rerun()
with c4:
    if st.button("🏖️\nBeach", key="m4"): st.session_state.secili_sayfa = "beach"; st.rerun()

c5, c6, c7, c8 = st.columns(4)
with c5:
    if st.button("🍸\nKokteyl", key="m5"): st.session_state.secili_sayfa = "kokteyl"; st.rerun()
with c6:
    if st.button("💊\nEczane", key="m6"): st.session_state.secili_sayfa = "eczane"; st.rerun()
with c7:
    if st.button("🚕\nTaksi", key="m7"): st.session_state.secili_sayfa = "taksi"; st.rerun()
with c8:
    if st.button("📜\nKurallar", key="m8"): st.session_state.secili_sayfa = "kurallar"; st.rerun()

st.divider()

# --- 7. SAYFA İÇERİKLERİ ---
sayfa = st.session_state.secili_sayfa

if sayfa == "asistan":
    st.markdown("### 🤖 Sorun, Cevaplayayım")
    prompt = st.chat_input("Örn: nerede kahve içilir?...")
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
            with st.chat_message("assistant"): st.info("🤖 Bu sorunuzu hemen not aldım, yapay zekaya danışıyorum...")

elif sayfa == "yemek":
    st.markdown('<div class="content-box"><h3>🍽️ Restoran Önerileri</h3>Sarımsaklı\'daki yerel balıkçılar taze ve lezzetlidir. Cunda kalabalığından uzak, huzurlu bir akşam yemeği için idealdir.</div>', unsafe_allow_html=True)

elif sayfa == "kahve":
    st.markdown('<div class="content-box"><h3>☕ Kahve & Sanat</h3>Yeniçarohori (Küçükköy) sokaklarını mutlaka keşfedin. Tarihi atmosferde sanat galerileri arasında kahve içmek Ayvalık\'ın en iyi deneyimlerinden biridir.</div>', unsafe_allow_html=True)

elif sayfa == "beach":
    st.markdown('<div class="content-box"><h3>🏖️ Plaj ve Deniz</h3><b>Sarımsaklı:</b> En yakın nokta.<br><b>Badavut:</b> Daha sakin.<br><b>Gizli Koy:</b> Badavut\'un en ucunda, doğa ile baş başa kalabileceğiniz sessiz bir koy bulunur.</div>', unsafe_allow_html=True)

elif sayfa == "kokteyl":
    st.markdown('<div class="content-box"><h3>🍸 Gece Hayatı & Kokteyl</h3>Cunda Adası sahil şeridinde ve arka sokaklarında çok şık kokteyl barlar mevcut. Akşam yürüyüşü sonrası harika bir durak.</div>', unsafe_allow_html=True)
