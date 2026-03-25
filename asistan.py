import streamlit as st
import time

# --- 1. AYARLAR ---
st.set_page_config(page_title="Detayvalik.io Asistan", layout="centered", page_icon="🏡")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "🤖 Asistan"

# --- 2. CSS (BÜYÜK MENÜLER & MODERN ASİSTAN) ---
st.markdown("""
    <style>
    /* Menü Butonlarını (Pills) Devleştiriyoruz */
    .stPills [data-testid="stBaseButton-secondaryPill"] {
        padding: 18px 28px !important;
        font-size: 18px !important;
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
    
    .venue-link a {
        background: #2c5364; color: white; padding: 10px 18px; border-radius: 10px;
        text-decoration: none; font-size: 12px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MEKAN VERİSİ ---
MEKAN_VERISI = {
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "https://maps.google.com/?q=Ayna+Cunda"},
        {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "https://maps.google.com/?q=L'arancia+Cunda"},
        {"ad": "By Nihat", "oz": "🐟 Efsanevi Balıkçı", "ln": "https://maps.google.com/?q=By+Nihat+Cunda"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "🍕 Odun Ateşi", "ln": "https://maps.google.com/?q=Pizza+Teo+Ayvalik"},
        {"ad": "Uno Cunda", "oz": "🇮🇹 İtalyan Klasiği", "ln": "https://maps.google.com/?q=Uno+Cunda"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "🍸 İmza Kokteyller", "ln": "https://maps.google.com/?q=Rituel+1873+Cunda"},
        {"ad": "Ciello Cunda", "oz": "🌆 Roof Bar", "ln": "https://maps.google.com/?q=Ciello+Cunda"}
    ],
    "eglence": [
        {"ad": "La Fuga Cunda", "oz": "🎵 Canlı Müzik", "ln": "https://maps.google.com/?q=La+Fuga+Cunda"},
        {"ad": "Afişe Sahne", "oz": "🎭 Performans", "ln": "https://maps.google.com/?q=Afise+Sahne+Ayvalik"}
    ],
    "kahve": [
        {"ad": "Pino's Coffee", "oz": "☕ Butik Kahve", "ln": "https://maps.google.com/?q=Pinos+Coffee+Ayvalik"},
        {"ad": "Daisy Küçükköy", "oz": "🎨 Sanat & Kahve", "ln": "https://maps.google.com/?q=Daisy+Kucukkoy"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "🏖️ Premium Beach", "ln": "https://maps.google.com/?q=Ajlan+Eos+Beach"},
        {"ad": "Surya Beach", "oz": "☀️ Modern Plaj", "ln": "https://maps.google.com/?q=Surya+Beach"}
    ]
}

# --- 4. ASİSTAN ZEKA (VERİYE GÖRE CEVAP VERİR) ---
def asistan_cevap(soru):
    soru = soru.lower()
    # Veri setinde eşleşme ara
    for kategori, mekanlar in MEKAN_VERISI.items():
        if kategori in soru:
            mekan_isimleri = ", ".join([m['ad'] for m in mekanlar])
            return f"Ayvalık'ta en iyi **{kategori}** seçenekleri şunlardır: **{mekan_isimleri}**. Detaylar ve konumlar için ilgili sekmeye göz atabilirsiniz! ✨"
    
    if "taksi" in soru: return "Sarımsaklı Taksi'ye '🚕 Taksi' sekmesinden ulaşabilir, tek tuşla arayabilirsiniz. 🚕"
    if "selam" in soru or "merhaba" in soru: return "Merhaba! Ben Detayvalik.io asistanıyım. Size yemek, pizza, kokteyl veya plaj önerileri sunabilirim. Ne aramıştınız?"
    
    return "Aradığınız konuda size en iyi mekanları önerebilirim. Yemek, Pizza, Kokteyl, Eğlence veya Beach seçeneklerinden birini sormak ister misiniz? 😊"

# --- 5. ARAYÜZ ---
st.markdown('<div class="header-container"><h2>🏡 Detayvalik.io Asistan</h2></div>', unsafe_allow_html=True)

kategoriler = ["🤖 Asistan", "🍽️ Yemek", "🍕 Pizza", "☕ Kahve", "🍸 Kokteyl", "🎉 Eğlence", "🏖️ Beach", "🚕 Taksi", "💊 Eczane"]
secim = st.pills("Kategori Seçin", kategoriler, selection_mode="single", default="🤖 Asistan")

st.divider()

# --- 6. SAYFA MANTIĞI ---
if secim == "🤖 Asistan":
    # Karşılama Balonu (Asistan Kimliğini Belli Eder)
    if not st.session_state.messages:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown("👋 **Merhaba! Ben Detayvalik.io Asistanınız.** \n\nAyvalık'ta harika bir gün geçirmeniz için buradayım. Size en iyi kokteyl barlarını, lezzetli pizzacıları veya akşam eğlencesi için canlı müzik mekanlarını önerebilirim. Ne sormak istersiniz?")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Pizza nerede yenir? Kokteyl için nereye gidilir?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant", avatar="🤖"):
            response = asistan_cevap(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

elif secim == "🚕 Taksi":
    st.markdown('<div class="venue-card"><div><h4>🚕 Sarımsaklı Taksi</h4><p>Hızlı ve Güvenilir</p></div><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif secim == "💊 Eczane":
    st.markdown('<div class="venue-card"><div><h4>💊 Nöbetçi Eczaneler</h4><p>Güncel Liste</p></div><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    key_map = {"🍽️ Yemek": "yemek", "🍕 Pizza": "pizza", "☕ Kahve": "kahve", "🍸 Kokteyl": "kokteyl", "🎉 Eğlence": "eglence", "🏖️ Beach": "beach"}
    k = key_map.get(secim, "")
    if k in MEKAN_VERISI:
        for m in MEKAN_VERISI[k]:
            st.markdown(f'''
                <div class="venue-card">
                    <div class="venue-info">
                        <h4>{m["ad"]}</h4>
                        <p>{m["oz"]}</p>
                    </div>
                    <div class="venue-link">
                        <a href="{m["ln"]}" target="_blank">📍 KONUM</a>
                    </div>
                </div>
            ''', unsafe_allow_html=True)
