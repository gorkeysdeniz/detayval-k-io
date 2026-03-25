import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "🤖 Asistan"

# --- 2. CSS (BÜYÜK MENÜLER VE ŞIK TASARIM) ---
st.markdown("""
    <style>
    /* Pills (Menü) Boyutlandırma */
    .stPills [data-testid="stBaseButton-secondaryPill"] {
        padding: 12px 20px !important;
        font-size: 16px !important;
        border-radius: 25px !important;
        border: 1px solid #2c5364 !important;
    }
    /* Aktif seçeneği belirginleştir */
    .stPills [data-active="true"] {
        background-color: #2c5364 !important;
        color: white !important;
    }
    
    .header-container {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 20px;
    }
    .venue-card {
        background: white; padding: 15px; border-radius: 15px; margin-bottom: 10px;
        border: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .venue-info h4 { margin: 0; font-size: 16px; color: #1e293b; }
    .venue-info p { margin: 2px 0 0 0; font-size: 13px; color: #64748b; }
    .venue-link a {
        background: #2c5364; color: white; padding: 10px 18px; border-radius: 10px;
        text-decoration: none; font-size: 12px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MEKAN VERİSİ (LİNK HATALARI GİDERİLDİ) ---
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pino's Coffee", "oz": "Butik Kahve", "ln": "https://maps.app.goo.gl/9mS18H3L8S3mU5G2A"},
        {"ad": "Crow Coffee", "oz": "3. Nesil Kavurma", "ln": "https://maps.app.goo.gl/YV9XqS9K8jU2zX6v7"},
        {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "https://maps.app.goo.gl/z2P3xR8yT5W9mB5n8"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "https://maps.app.goo.gl/r6H7L9n8M5B2vX6z9"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "https://maps.app.goo.gl/b5V7X9M2L4k8mN1z2"},
        {"ad": "Melin Kahve", "oz": "Keyifli Durak", "ln": "https://maps.app.goo.gl/v3N8X9M1L4k2mP5z6"},
        {"ad": "Declan Coffee", "oz": "Modern Coffee", "ln": "https://maps.app.goo.gl/m4N8X9L1K4m2P7z8"},
        {"ad": "AIMA Cafe", "oz": "Müzik & Cafe", "ln": "https://maps.app.goo.gl/x2M8N9L1K4m5P6z9"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "https://maps.app.goo.gl/v2M8N9L1K4m5P6z8"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "https://maps.app.goo.gl/m2N8X9L1K4m5P6z9"},
        {"ad": "Tino Ristorante", "oz": "Gurme Lezzetler", "ln": "https://maps.app.goo.gl/b2M8N9L1K4m5P6z7"},
        {"ad": "Küçük İtalya", "oz": "Napoliten Stil", "ln": "https://maps.app.goo.gl/x2N8M9L1K4m5P6z1"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "Michelin Rehberi", "ln": "https://maps.app.goo.gl/v2N8M9L1K4m5P6z2"},
        {"ad": "L'arancia", "oz": "Michelin Rehberi", "ln": "https://maps.app.goo.gl/m2N8X9L1K4m5P6z3"},
        {"ad": "By Nihat", "oz": "Efsanevi Balıkçı", "ln": "https://maps.app.goo.gl/b2M8N9L1K4m5P6z4"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "Premium Beach", "ln": "https://maps.app.goo.gl/x2N8M9L1K4m5P6z5"},
        {"ad": "Sarımsaklı Plajı", "oz": "Halk Plajı", "ln": "https://maps.app.goo.gl/v2N8M9L1K4m5P6z6"}
    ]
}

# --- 4. ASİSTAN ZEKA ---
def asistan_cevap(soru):
    soru = soru.lower()
    if "pizza" in soru: return "Ayvalık'ta pizza için en iyi yerler: Pizza Teo ve Uno Cunda. Detaylar için '🍕 Pizza' sekmesine bakabilirsin."
    if "taksi" in soru: return "Sarımsaklı Taksi'ye '🚕 Taksi' sekmesinden tek tıkla ulaşabilirsin."
    if "yemek" in soru or "restoran" in soru: return "Özel bir akşam yemeği için Ayna veya L'arancia'yı öneririm. '🍽️ Yemek' sekmesine göz at!"
    return "SAYEM Misafir Asistanı burada! Pizza, kahve veya plaj seçenekleri hakkında bilgi alabilirsin."

# --- 5. ARAYÜZ ---
st.markdown('<div class="header-container"><h2>🏡 Ayvalık Misafir Asistanı</h2></div>', unsafe_allow_html=True)

kategoriler = ["🤖 Asistan", "🍽️ Yemek", "🍕 Pizza", "☕ Kahve", "🏖️ Beach", "🚕 Taksi", "💊 Eczane"]
secim = st.pills("Kategori Seçin", kategoriler, selection_mode="single", default="🤖 Asistan")

if secim:
    st.session_state.secili_sayfa = secim

st.divider()

# --- 6. SAYFA İÇERİKLERİ ---
s = st.session_state.secili_sayfa

if "Asistan" in s:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Size nasıl yardımcı olabilirim?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        response = asistan_cevap(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

elif "Taksi" in s:
    st.markdown('<div class="venue-card"><div><h4>🚕 Sarımsaklı Taksi</h4><p>Hızlı ve Güvenilir</p></div><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif "Eczane" in s:
    st.markdown('<div class="venue-card"><div><h4>💊 Nöbetçi Eczaneler</h4><p>Güncel Liste</p></div><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    key_map = {"🍽️ Yemek": "yemek", "🍕 Pizza": "pizza", "☕ Kahve": "kahve", "🏖️ Beach": "beach"}
    k = key_map.get(s)
    if k in MEKAN_VERISI:
        for m in MEKAN_VERISI[k]:
            st.markdown(f'<div class="venue-card"><div class="venue-info"><h4>{m["ad"]}</h4><p>{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank">📍 KONUM</a></div></div>', unsafe_allow_html=True)
