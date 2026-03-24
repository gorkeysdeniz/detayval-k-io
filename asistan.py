import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. TAM VERİ SETİ (KARTLAR İÇİN) ---
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "https://maps.app.goo.gl/3A6S9j8Y9Z"},
        {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "https://maps.app.goo.gl/Z8X5C2V1B3"},
        {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "https://maps.app.goo.gl/N4M5K6L7J8"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "https://maps.app.goo.gl/D9E1F2G3H4"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "https://maps.app.goo.gl/N5M6K7L8J9"},
        {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "https://maps.app.goo.gl/C1V2B3N4M5"},
        {"ad": "Declan", "oz": "Modern Coffee", "ln": "https://maps.app.goo.gl/D7E8F9G0H1"},
        {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "https://maps.app.goo.gl/A2S3D4F5G6"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "https://maps.app.goo.gl/P1Q2W3E4R5"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "https://maps.app.goo.gl/U6Y7T8R9E0"},
        {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "https://maps.app.goo.gl/T1Y2U3I4O5"},
        {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "https://maps.app.goo.gl/K6L7M8N9P0"},
        {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "https://maps.app.goo.gl/C2V3B4N5M6"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "https://maps.app.goo.gl/R1T2Y3U4I5"},
        {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "https://maps.app.goo.gl/L6K7J8H9G0"},
        {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "https://maps.app.goo.gl/C4V5B6N7M8"},
        {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "https://maps.app.goo.gl/V1B2N3M4K5"},
        {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "https://maps.app.goo.gl/D9F0G1H2J3"},
        {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "https://maps.app.goo.gl/F4G5H6J7K8"},
        {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "https://maps.app.goo.gl/F1D2S3A4Q5"},
        {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "https://maps.app.goo.gl/K9L0M1N2B3"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi / Ödüllü", "ln": "https://maps.app.goo.gl/A1Z2X3C4V5"},
        {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi / Ödüllü", "ln": "https://maps.app.goo.gl/L9K8J7H6G5"},
        {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı / Ödüllü", "ln": "https://maps.app.goo.gl/B4N5M6K7L8"},
        {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "https://maps.app.goo.gl/R2T3Y4U5I6"},
        {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "https://maps.app.goo.gl/K1J2H3G4F5"},
        {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "https://maps.app.goo.gl/P9O8I7U6Y5"},
        {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "https://maps.app.goo.gl/A4S5D6F7G8"},
        {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "https://maps.app.goo.gl/K1M2N3B4V5"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/A1S2D3F4G5"},
        {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/K6J7H8G9F0"},
        {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/S1A2Q3W4E5"},
        {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/S9D8F7G6H5"},
        {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz / Geniş Sahil", "ln": "https://maps.app.goo.gl/S4S5S6S7S8"},
        {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz / Doğa Harikası", "ln": "https://maps.app.goo.gl/B1N2M3B4V5"},
        {"ad": "Patrica Koyu", "oz": "🆓 Ücretsiz / Sığ Deniz", "ln": "https://maps.app.goo.gl/P0O9I8U7Y6"}
    ],
    "eglence": [
        {"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "https://maps.app.goo.gl/L1K2J3H4G5"},
        {"ad": "Kraft", "oz": "Craft Beer & Mood", "ln": "https://maps.app.goo.gl/K6L7M8N9P0"},
        {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "https://maps.app.goo.gl/A1Z2X3C4V5"},
        {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "https://maps.app.goo.gl/A9S8D7F6G5"},
        {"ad": "The Public House", "oz": "Şehir Kulübü", "ln": "https://maps.app.goo.gl/T1Y2U3I4O5"}
    ]
}

# --- 3. CSS (TASARIM & KARTLAR) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }
    div.stButton > button {
        background: white !important; color: #1a202c !important;
        border: 1px solid #edf2f7 !important; border-radius: 15px !important;
        width: 100% !important; height: 95px !important; font-weight: 700 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s;
    }
    div.stButton > button:hover { transform: translateY(-3px); border-color: #2c5364 !important; }

    /* KART TASARIMI */
    .venue-card {
        background: white; padding: 15px 20px; border-radius: 18px;
        margin-bottom: 12px; border: 1px solid #e2e8f0;
        display: flex; justify-content: space-between; align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .venue-info h4 { margin: 0; color: #1a202c; font-size: 17px; }
    .venue-info p { margin: 4px 0 0 0; color: #64748b; font-size: 13px; font-weight: 500; }
    
    .venue-link a {
        background: #2c5364; color: white !important;
        padding: 8px 14px; border-radius: 10px; text-decoration: none;
        font-size: 12px; font-weight: 600; transition: 0.3s;
    }
    .venue-link a:hover { background: #1a202c; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. DASHBOARD ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Rehber & İşletmeler</p></div>', unsafe_allow_html=True)

# 4x2 BUTON GRİDİ
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🤖\nAsistan"): st.session_state.secili_sayfa = "asistan"; st.rerun()
with c2:
    if st.button("🍽️\nYemek"): st.session_state.secili_sayfa = "yemek"; st.rerun()
with c3:
    if st.button("☕\nKahve"): st.session_state.secili_sayfa = "kahve"; st.rerun()
with c4:
    if st.button("🏖️\nBeach"): st.session_state.secili_sayfa = "beach"; st.rerun()

c5, c6, c7, c8 = st.columns(4)
with c5:
    if st.button("🍸\nKokteyl"): st.session_state.secili_sayfa = "kokteyl"; st.rerun()
with c6:
    if st.button("🎉\nEğlence"): st.session_state.secili_sayfa = "eglence"; st.rerun()
with c7:
    if st.button("🚕\nTaksi"): st.session_state.secili_sayfa = "taksi"; st.rerun()
with c8:
    if st.button("💊\nEczane"): st.session_state.secili_sayfa = "eczane"; st.rerun()

st.divider()

# --- 5. KART OLUŞTURUCU FONKSİYON ---
def render_cards(key):
    if key in MEKAN_VERISI:
        for item in MEKAN_VERISI[key]:
            st.markdown(f"""
                <div class="venue-card">
                    <div class="venue-info">
                        <h4>{item['ad']}</h4>
                        <p>{item['oz']}</p>
                    </div>
                    <div class="venue-link">
                        <a href="{item['ln']}" target="_blank">📍 KONUM</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- 6. SAYFA YÖNETİMİ ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.subheader("🤖 Akıllı Asistan")
    p = st.chat_input("Sorunuzu yazın...")
    st.info("İşletmeleri yukarıdaki kategorilerden detaylı inceleyebilirsiniz.")

elif s == "yemek":
    st.markdown("### 🍽️ Restoranlar")
    render_cards("yemek")
    st.markdown("### 🍕 Pizza Önerileri")
    render_cards("pizza")

elif s == "kahve":
    st.markdown("### ☕ Kahve & Tatlı")
    render_cards("kahve")

elif s == "beach":
    st.markdown("### 🏖️ Plaj & Beachler")
    render_cards("beach")

elif s == "kokteyl":
    st.markdown("### 🍸 Kokteyl & Alkol")
    render_cards("kokteyl")

elif s == "eglence":
    st.markdown("### 🎉 Eğlence & Etkinlik")
    render_cards("eglence")

elif s == "taksi":
    st.markdown("""
        <div class="venue-card">
            <div class="venue-info">
                <h4>Sarımsaklı Taksi</h4>
                <p>7/24 Hizmet</p>
            </div>
            <div class="venue-link">
                <a href="tel:02663961010">📞 ARA: 0266 396 10 10</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif s == "eczane":
    st.markdown("""
        <div class="venue-card">
            <div class="venue-info">
                <h4>Nöbetçi Eczaneler</h4>
                <p>Güncel liste için tıklayın</p>
            </div>
            <div class="venue-link">
                <a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 LİSTEYİ AÇ</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
