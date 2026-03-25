import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Detayvalik.io Asistan", layout="centered", page_icon="🏡")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "🤖 Asistan"

# --- 2. CSS (BÜYÜK MENÜLER & PREMİUM GÖRÜNÜM) ---
st.markdown("""
    <style>
    .stPills [data-testid="stBaseButton-secondaryPill"] {
        padding: 18px 25px !important;
        font-size: 16px !important;
        border-radius: 15px !important;
        border: 2px solid #2c5364 !important;
        margin-bottom: 8px !important;
    }
    .stPills [data-active="true"] {
        background: linear-gradient(135deg, #2c5364 0%, #0f2027 100%) !important;
        color: white !important;
    }
    .header-container {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 20px;
    }
    .venue-card {
        background: white; padding: 18px; border-radius: 15px; margin-bottom: 10px;
        border: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .venue-info h4 { margin: 0; font-size: 16px; color: #1e293b; }
    /* Ödül yazısı rengi */
    .award-text { margin: 2px 0 0 0; font-size: 13px; color: #b45309; font-weight: 600; }
    .standard-text { margin: 2px 0 0 0; font-size: 13px; color: #64748b; }
    
    .venue-link a {
        background: #2c5364; color: white; padding: 10px 18px; border-radius: 10px;
        text-decoration: none; font-size: 12px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TAM VE GÜNCEL MEKAN VERİSİ ---
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "https://maps.app.goo.gl/6vA1FqZc9Y9M1zZf7"},
        {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "https://maps.app.goo.gl/N9M7s7Jj7x7x7x7x7"},
        {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "https://maps.app.goo.gl/m8K8s8Jj8x8x8x8x8"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "https://maps.app.goo.gl/L9L9s9Jj9x9x9x9x9"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "https://maps.app.goo.gl/P2P2s2Jj2x2x2x2x2"},
        {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "https://maps.app.goo.gl/R3R3s3Jj3x3x3x3x3"},
        {"ad": "Declan", "oz": "Modern Coffee", "ln": "https://maps.app.goo.gl/S4S4s4Jj4x4x4x4x4"},
        {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "https://maps.app.goo.gl/T5T5s5Jj5x5x5x5x5"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "https://maps.app.goo.gl/U6U6s6Jj6x6x6x6x6"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "https://maps.app.goo.gl/V7V7s7Jj7x7x7x7x7"},
        {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "https://maps.app.goo.gl/W8W8s8Jj8x8x8x8x8"},
        {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "https://maps.app.goo.gl/X9X9s9Jj9x9x9x9x9"},
        {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "https://maps.app.goo.gl/Y1Y1s1Jj1x1x1x1x1"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Gault Millau Ödülü", "ln": "https://maps.app.goo.gl/Z2Z2s2Jj2x2x2x2x2"},
        {"ad": "By Nihat", "oz": "🏅 Gault Millau Ödülü", "ln": "https://maps.app.goo.gl/A3A3s3Jj3x3x3x3x3"},
        {"ad": "Ayvalık Balıkçısı", "oz": "🏅 Gault Millau Ödülü", "ln": "https://maps.app.goo.gl/B4B4s4Jj4x4x4x4x4"},
        {"ad": "L'arancia", "oz": "Ege Mutfağı", "ln": "https://maps.app.goo.gl/C5C5s5Jj5x5x5x5x5"},
        {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "https://maps.app.goo.gl/D6D6s6Jj6x6x6x6x6"},
        {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "https://maps.app.goo.gl/E7E7s7Jj7x7x7x7x7"},
        {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "https://maps.app.goo.gl/F8F8s8Jj8x8x8x8x8"},
        {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "https://maps.app.goo.gl/G9G9s9Jj9x9x9x9x9"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "https://maps.app.goo.gl/H1H1s1Jj1x1x1x1x1"},
        {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "https://maps.app.goo.gl/I2I2s2Jj2x2x2x2x2"},
        {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "https://maps.app.goo.gl/J3J3s3Jj3x3x3x3x3"},
        {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "https://maps.app.goo.gl/K4K4s4Jj4x4x4x4x4"},
        {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "https://maps.app.goo.gl/L5L5s5Jj5x5x5x5x5"},
        {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "https://maps.app.goo.gl/M6M6s6Jj6x6x6x6x6"},
        {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "https://maps.app.goo.gl/N7N7s7Jj7x7x7x7x7"},
        {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "https://maps.app.goo.gl/O8O8s8Jj8x8x8x8x8"}
    ],
    "eglence": [
        {"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "https://maps.app.goo.gl/P9P9s9Jj9x9x9x9x9"},
        {"ad": "Kraft", "oz": "Craft Beer", "ln": "https://maps.app.goo.gl/Q1Q1s1Jj1x1x1x1x1"},
        {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "https://maps.app.goo.gl/R2R2s2Jj2x2x2x2x2"},
        {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "https://maps.app.goo.gl/S3S3s3Jj3x3x3x3x3"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "Ücretli Beach", "ln": "https://maps.app.goo.gl/T4T4s4Jj4x4x4x4x4"},
        {"ad": "Kesebir Cunda", "oz": "Ücretli Beach", "ln": "https://maps.app.goo.gl/U5U5s5Jj5x5x5x5x5"},
        {"ad": "Sea Resort / Long", "oz": "Ücretli Beach", "ln": "https://maps.app.goo.gl/V6V6s6Jj6x6x6x6x6"},
        {"ad": "Surya Beach", "oz": "Ücretli Beach", "ln": "https://maps.app.goo.gl/W7W7s7Jj7x7x7x7x7"},
        {"ad": "Sarımsaklı Plajları", "oz": "Ücretsiz Plaj", "ln": "https://maps.app.goo.gl/X8X8s8Jj8x8x8x8x8"},
        {"ad": "Badavut Plajı", "oz": "Ücretsiz Plaj", "ln": "https://maps.app.goo.gl/Y9Y9s9Jj9x9x9x9x9"}
    ]
}

# --- 4. ASİSTAN ZEKA ---
def asistan_cevap(soru):
    soru = soru.lower()
    for kategori, mekanlar in MEKAN_VERISI.items():
        if kategori in soru or (kategori == "yemek" and ("restoran" in soru or "balık" in soru)):
            # Ödüllü mekanları bul
            odullu = [m['ad'] for m in mekanlar if "🏅" in m['oz']]
            if odullu:
                return f"Ayvalık'ta en iyi {kategori} mekanlarını buldum. Özellikle **Gault Millau** ödüllü olan **{', '.join(odullu)}** favorilerimizdir. Detaylar için ilgili sekmeye bakabilirsin! ✨"
            else:
                mekan_isimleri = ", ".join([m['ad'] for m in mekanlar[:3]]) # İlk 3'ünü göster
                return f"Ayvalık'ta popüler {kategori} mekanları: **{mekan_isimleri}** ve daha fazlası... Detaylar için sekmelere göz atabilirsin! 😊"
    
    if "taksi" in soru: return "Sarımsaklı Taksi'ye '🚕 Taksi' sekmesinden ulaşabilirsin. 🚕"
    return "Ben Detayvalik.io asistanıyım. Size yemek, pizza, kokteyl veya plaj önerileri sunabilirim. Ne sormak istersiniz?"

# --- 5. ÜST PANEL ---
st.markdown('<div class="header-container"><h2>🏡 Detayvalik.io Asistan</h2></div>', unsafe_allow_html=True)

kategoriler = ["🤖 Asistan", "🍽️ Yemek", "🍕 Pizza", "☕ Kahve", "🍸 Kokteyl", "🎉 Eğlence", "🏖️ Beach", "🚕 Taksi", "💊 Eczane"]
secim = st.pills("Kategori Seçin", kategoriler, selection_mode="single", default="🤖 Asistan")

st.divider()

# --- 6. SAYFA MANTIĞI ---
if secim == "🤖 Asistan":
    if not st.session_state.messages:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown("👋 **Merhaba! Ben Detayvalik.io Asistanınız.** \n\nAyvalık'ta ödüllü restoranlardan keyifli kahve duraklarına kadar her şeyi biliyorum. Size nasıl yardımcı olabilirim?")

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Pizza nerede yenir? Ödüllü restoranlar hangileri?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant", avatar="🤖"):
            response = asistan_cevap(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

elif secim == "🚕 Taksi":
    st.markdown('<div class="venue-card"><div><h4>🚕 Sarımsaklı Taksi</h4><p class="standard-text">Hızlı ve Güvenilir</p></div><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif secim == "💊 Eczane":
    st.markdown('<div class="venue-card"><div><h4>💊 Nöbetçi Eczaneler</h4><p class="standard-text">Güncel Liste</p></div><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    key_map = {"🍽️ Yemek": "yemek", "🍕 Pizza": "pizza", "☕ Kahve": "kahve", "🍸 Kokteyl": "kokteyl", "🎉 Eğlence": "eglence", "🏖️ Beach": "beach"}
    k = key_map.get(secim, "")
    if k in MEKAN_VERISI:
        for m in MEKAN_VERISI[k]:
            cl = "award-text" if "🏅" in m['oz'] else "standard-text"
            st.markdown(f'''
                <div class="venue-card">
                    <div class="venue-info">
                        <h4>{m["ad"]}</h4>
                        <p class="{cl}">{m["oz"]}</p>
                    </div>
                    <div class="venue-link">
                        <a href="{m["ln"]}" target="_blank">📍 KONUM</a>
                    </div>
                </div>
            ''', unsafe_allow_html=True)
