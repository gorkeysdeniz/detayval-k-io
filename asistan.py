import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. CSS (KESİN ÇÖZÜM: GRID & BUTTON OVERRIDE) ---
st.markdown("""
    <style>
    /* Sayfayı ekrana sabitle, sağa kaymayı engelle */
    .block-container { padding: 1rem 0.5rem !important; max-width: 100% !important; }
    html, body, [data-testid="stAppViewContainer"] { overflow-x: hidden !important; }

    /* PINTEREST GRID YAPISI */
    /* Streamlit'in kendi butonlarını bu grid içine sokacağız */
    .button-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
        width: 100%;
        margin-bottom: 20px;
    }

    /* STREAMLIT BUTONLARINI ÖZELLEŞTİR */
    div.stButton > button {
        width: 100% !important;
        height: 100px !important;
        border-radius: 15px !important;
        background-color: white !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 5px !important;
        transition: all 0.2s ease;
    }

    div.stButton > button:active {
        transform: scale(0.95);
        border-color: #2c5364 !important;
    }

    /* Buton içindeki metin ve emojiyi alt alta getir */
    div.stButton p {
        font-size: 13px !important;
        font-weight: 800 !important;
        line-height: 1.2 !important;
        white-space: pre-line !important; /* \n karakterini algılar */
    }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;
    }
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# --- 4. 3'LÜ GRID (st.columns KULLANMADAN) ---
# Container kullanarak butonları yan yana hapsediyoruz
with st.container():
    st.markdown('<div class="button-grid">', unsafe_allow_html=True)
    
    # Her butonu kendi sütununa değil, ardı ardına koyuyoruz; CSS Grid onları 3'lü dizecek
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1,1,1,1,1,1,1,1,1])
    # NOT: st.columns(9) yapıyoruz ama CSS ile bunları 3x3'e zorluyoruz
    
    with col1:
        if st.button("🤖\nAsistan", key="b1"): st.session_state.secili_sayfa = "asistan"
    with col2:
        if st.button("🍽️\nYemek", key="b2"): st.session_state.secili_sayfa = "yemek"
    with col3:
        if st.button("🍕\nPizza", key="b3"): st.session_state.secili_sayfa = "pizza"
    with col4:
        if st.button("☕\nKahve", key="b4"): st.session_state.secili_sayfa = "kahve"
    with col5:
        if st.button("🏖️\nBeach", key="b5"): st.session_state.secili_sayfa = "beach"
    with col6:
        if st.button("🍸\nKokteyl", key="b6"): st.session_state.secili_sayfa = "kokteyl"
    with col7:
        if st.button("🎉\nEğlence", key="b7"): st.session_state.secili_sayfa = "eglence"
    with col8:
        if st.button("🚕\nTaksi", key="b8"): st.session_state.secili_sayfa = "taksi"
    with col9:
        if st.button("💊\nEczane", key="b9"): st.session_state.secili_sayfa = "eczane"
    
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- 5. MEKAN VERİSİ (DOKUNULMADI) ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}, {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"}, {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"}, {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"}, {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"}, {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"}, {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}, {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"}, {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"}, {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}, {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"}, {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"}, {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"}, {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"}, {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"}, {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}, {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"}, {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"}, {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"}, {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"}, {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"}, {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"}, {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}, {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"}, {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"}, {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"}, {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/32"}, {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/33"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}, {"ad": "Kraft", "oz": "Craft Beer", "ln": "http://google.com/35"}, {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"}, {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "http://google.com/37"}]
}

def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div><h4 style="margin:0; font-size:14px;">{m["ad"]}</h4><p style="margin:0; font-size:11px; color:#666;">{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-size:10px; font-weight:bold;">📍 KONUM</a></div></div>', unsafe_allow_html=True)

# --- 6. SAYFA MANTIĞI ---
s = st.session_state.secili_sayfa
if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    u_in = st.chat_input("Mesajınızı yazın...")
    if u_in:
        # Chat mantığı buraya...
        pass
elif s == "taksi":
    st.markdown('<div class="venue-card"><h4>🚕 Sarımsaklı Taksi</h4><a href="tel:02663961010" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">📞 ARA</a></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown('<div class="venue-card"><h4>💊 Nöbetçi Eczaneler</h4><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">🔍 GÖR</a></div>', unsafe_allow_html=True)
else:
    kart_bas(s)
