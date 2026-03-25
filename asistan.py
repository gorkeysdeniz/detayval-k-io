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
    .stPills [data-testid="stBaseButton-secondaryPill"] {
        padding: 15px 25px !important;
        font-size: 16px !important;
        border-radius: 30px !important;
        border: 1px solid #2c5364 !important;
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

# --- 3. GÜNCEL MEKAN VERİSİ (GERÇEK KONUMLAR) ---
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pino's Coffee & Cakes", "oz": "Butik Kahve & Tatlı", "ln": "https://www.google.com/maps/search/?api=1&query=Pino's+Coffee+Ayvalik"},
        {"ad": "Crow Coffee Roastery", "oz": "3. Nesil Kavurma", "ln": "https://www.google.com/maps/search/?api=1&query=Crow+Coffee+Roastery+Ayvalik"},
        {"ad": "Ivy Ayvalik Coffee", "oz": "Huzurlu Bahçe", "ln": "https://www.google.com/maps/search/?api=1&query=Ivy+Ayvalik+Coffee"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "https://www.google.com/maps/search/?api=1&query=Daisy+Kucukkoy"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "https://www.google.com/maps/search/?api=1&query=Nona+Cunda"},
        {"ad": "Melin Kahve/Cafe", "oz": "Keyifli Durak", "ln": "https://www.google.com/maps/search/?api=1&query=Melin+Cafe+Ayvalik"},
        {"ad": "Declan Coffee", "oz": "Modern Coffee", "ln": "https://www.google.com/maps/search/?api=1&query=Declan+Coffee+Ayvalik"},
        {"ad": "AIMA Cafe", "oz": "Müzik Akademisi Cafe", "ln": "https://www.google.com/maps/search/?api=1&query=AIMA+Cafe+Ayvalik"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "https://www.google.com/maps/search/?api=1&query=Pizza+Teo+Ayvalik"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "https://www.google.com/maps/search/?api=1&query=Uno+Cunda"},
        {"ad": "Tino Ristorante", "oz": "Gurme Pizza", "ln": "https://www.google.com/maps/search/?api=1&query=Tino+Ristorante+Ayvalik"},
        {"ad": "Küçük İtalya", "oz": "Napoliten Stil", "ln": "https://www.google.com/maps/search/?api=1&query=Kucuk+İtalya+Ayvalik"},
        {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "https://www.google.com/maps/search/?api=1&query=Cunda+Luna"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "https://www.google.com/maps/search/?api=1&query=Ayna+Cunda"},
        {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "https://www.google.com/maps/search/?api=1&query=Larancia+Cunda"},
        {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "https://www.google.com/maps/search/?api=1&query=By+Nihat+Cunda"},
        {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "https://www.google.com/maps/search/?api=1&query=Rituel+1873+Cunda"},
        {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "https://www.google.com/maps/search/?api=1&query=Kosbasi+Ayvalik"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "💎 Premium Beach", "ln": "https://www.google.com/maps/search/?api=1&query=Ajlan+Eos+Beach"},
        {"ad": "Surya Beach", "oz": "💎 Modern Beach", "ln": "https://www.google.com/maps/search/?api=1&query=Surya+Beach+Ayvalik"},
        {"ad": "Sarımsaklı Plajı", "oz": "🆓 Halk Plajı", "ln": "https://www.google.com/maps/search/?api=1&query=Sarimsakli+Plaji"},
        {"ad": "Badavut Plajı", "oz": "🆓 Doğa Harikası", "ln": "https://www.google.com/maps/search/?api=1&query=Badavut+Plaji"}
    ]
}

# --- 4. ASİSTAN ZEKA ---
def asistan_cevap(soru):
    soru = soru.lower()
    if "pizza" in soru: return "Ayvalık'ta en iyi pizzalar için '🍕 Pizza' sekmesine bakabilirsiniz. Pizza Teo ve Uno Cunda en popülerleridir."
    if "taksi" in soru: return "'🚕 Taksi' sekmesine tıklayarak Sarımsaklı Taksi'yi tek tuşla arayabilirsiniz."
    if "yemek" in soru or "restoran" in soru: return "Gastronomi turu için '🍽️ Yemek' sekmesindeki Michelin listesine göz atın!"
    return "SAYEM Misafir Asistanı olarak size nasıl yardımcı olabilirim? Pizza, kahve veya plaj seçeneklerini sorabilirsiniz."

# --- 5. ARAYÜZ ---
st.markdown('<div class="header-container"><h2>🏡 Ayvalık Misafir Asistanı</h2></div>', unsafe_allow_html=True)

kategoriler = ["🤖 Asistan", "🍽️ Yemek", "🍕 Pizza", "☕ Kahve", "🏖️ Beach", "🍸 Kokteyl", "🎉 Eğlence", "🚕 Taksi", "💊 Eczane"]
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
    st.markdown('<div class="venue-card"><div><h4>🚕 Sarımsaklı Taksi</h4><p>Hızlı Ulaşım</p></div><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif "Eczane" in s:
    st.markdown('<div class="venue-card"><div><h4>💊 Nöbetçi Eczaneler</h4><p>Güncel Liste</p></div><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    key_map = {"🍽️ Yemek": "yemek", "🍕 Pizza": "pizza", "☕ Kahve": "kahve", "🏖️ Beach": "beach", "🍸 Kokteyl": "kokteyl", "🎉 Eğlence": "eglence"}
    k = key_map.get(s)
    if k in MEKAN_VERISI:
        for m in MEKAN_VERISI[k]:
            st.markdown(f'<div class="venue-card"><div class="venue-info"><h4>{m["ad"]}</h4><p>{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank">📍 KONUM</a></div></div>', unsafe_allow_html=True)
