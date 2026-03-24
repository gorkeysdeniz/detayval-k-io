import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. CSS (HIZLI VE YAN YANA DİZİLİM) ---
st.markdown("""
    <style>
    /* Sayfa ve Blok Ayarları */
    .block-container { padding: 1rem 0.5rem !important; }
    
    /* MOBİLDE YAN YANA 4'LÜ DİZİLİMİ ZORLAYAN SİHİRLİ DEĞNEK */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 4px !important;
        width: 100% !important;
    }
    
    div[data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    /* BUTONLARI MOBİL UYGULAMA İKONU GİBİ YAP */
    div.stButton > button {
        width: 100% !important;
        height: 65px !important;
        padding: 0px !important;
        font-size: 10px !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        background-color: white !important;
        border: 1px solid #e2e8f0 !important;
        display: flex !important;
        flex-direction: column !important;
        line-height: 1.2 !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
        transition: all 0.2s ease;
    }
    
    /* Aktif sayfa butonunu belirginleştir */
    div.stButton > button:focus {
        border-color: #2c5364 !important;
        background-color: #f1f5f9 !important;
    }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 15px; text-align: center; margin-bottom: 15px;
    }

    /* Mekan Kartları */
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Hızlı Erişim Paneli</p></div>', unsafe_allow_html=True)

# İÇERİĞİ BOZMADAN ULTRA HIZLI BUTONLAR
# (st.columns kullanıyoruz ama yukarıdaki CSS sayesinde yan yana kalıyorlar)

row1 = st.columns(4)
with row1[0]:
    if st.button("🤖\nAsistan", key="nb1"): st.session_state.secili_sayfa = "asistan"
with row1[1]:
    if st.button("🍽️\nYemek", key="nb2"): st.session_state.secili_sayfa = "yemek"
with row1[2]:
    if st.button("☕\nKahve", key="nb3"): st.session_state.secili_sayfa = "kahve"
with row1[3]:
    if st.button("🏖️\nBeach", key="nb4"): st.session_state.secili_sayfa = "beach"

row2 = st.columns(4)
with row2[0]:
    if st.button("🍸\nKokteyl", key="nb5"): st.session_state.secili_sayfa = "kokteyl"
with row2[1]:
    if st.button("🎉\nEğlence", key="nb6"): st.session_state.secili_sayfa = "eglence"
with row2[2]:
    if st.button("🚕\nTaksi", key="nb7"): st.session_state.secili_sayfa = "taksi"
with row2[3]:
    if st.button("💊\nEczane", key="nb8"): st.session_state.secili_sayfa = "eczane"

st.divider()

# --- 4. VERİ SETİ VE FONKSİYONLAR ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}]
    # ... diğer veriler buraya eklenebilir
}

def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div><h4>{m["ad"]}</h4><p>{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:6px 10px; border-radius:6px; text-decoration:none; font-size:10px;">📍 KONUM</a></div></div>', unsafe_allow_html=True)

# --- 5. SAYFA GEÇİŞLERİ (ANLIK ÇALIŞIR) ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    u_in = st.chat_input("Yemek, kahve, beach...")
    # Asistan mantığı buraya...

elif s == "yemek":
    st.markdown("##### 🍽️ Yemek Önerileri")
    kart_bas("yemek")

elif s == "kahve":
    st.markdown("##### ☕ Kahve & Tatlı")
    kart_bas("kahve")

elif s == "beach":
    st.markdown("##### 🏖️ Beach & Plaj")
    kart_bas("beach")

elif s == "taksi":
    st.markdown('<div class="venue-card"><h4>Sarımsaklı Taksi</h4><a href="tel:02663961010" style="color:#2c5364; font-weight:bold;">📞 ARA: 0266 396 10 10</a></div>', unsafe_allow_html=True)
