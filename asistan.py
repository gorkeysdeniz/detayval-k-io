import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "🤖 Asistan"

# --- 2. CSS (BÜYÜK MENÜLER VE ŞIK ASİSTAN) ---
st.markdown("""
    <style>
    /* Menü butonlarını (Pills) devleştiriyoruz */
    button[data-baseweb="tab"] {
        padding: 12px 20px !important;
        font-size: 18px !important;
    }
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

# --- 3. MEKAN VERİSİ ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}, {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"}, {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"}, {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"}, {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"}, {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"}, {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}, {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"}, {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"}, {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}, {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"}, {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"}, {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"}, {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"}, {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"}, {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}, {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"}, {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"}, {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"}, {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"}, {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"}, {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"}, {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}, {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"}, {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"}, {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"}, {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/32"}, {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/33"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}, {"ad": "Kraft", "oz": "Craft Beer", "ln": "http://google.com/35"}, {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"}, {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "http://google.com/37"}]
}

# --- 4. ASİSTAN ZEKA FONKSİYONU ---
def asistan_cevap(soru):
    soru = soru.lower()
    if "pizza" in soru: return "Sizin için en iyi pizza mekanlarını '🍕 Pizza' sekmesinde listeledim. Favorim: Pizza Teo!"
    if "kahve" in soru: return "Ayvalık'ta kahve için birçok seçenek var. '☕ Kahve' sekmesine bakabilirsiniz. Pinos Cafe harikadır."
    if "yemek" in soru or "restoran" in soru: return "Michelin rehberindeki Ayna ve L'arancia'yı '🍽️ Yemek' sekmesinde bulabilirsiniz."
    if "taksi" in soru: return "Sarımsaklı Taksi için '🚕 Taksi' sekmesine tıklayıp doğrudan arayabilirsiniz."
    return "Ayvalık hakkında her şeyi sorabilirsiniz! Yemek, Pizza, Kahve veya Taksi gibi konularda size rehberlik edebilirim."

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
    # Sohbet geçmişini göster
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Pizza, Kahve, Taksi nerede?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        response = asistan_cevap(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

elif "Taksi" in s:
    st.markdown('<div class="venue-card"><div><h4>🚕 Sarımsaklı Taksi</h4><p>Hızlı ve güvenilir ulaşım</p></div><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif "Eczane" in s:
    st.markdown('<div class="venue-card"><div><h4>💊 Nöbetçi Eczaneler</h4><p>Güncel nöbetçi listesi</p></div><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    # Mekanları Listele
    key_map = {"🍽️ Yemek": "yemek", "🍕 Pizza": "pizza", "☕ Kahve": "kahve", "🏖️ Beach": "beach", "🍸 Kokteyl": "kokteyl", "🎉 Eğlence": "eglence"}
    k = key_map.get(s)
    if k in MEKAN_VERISI:
        for m in MEKAN_VERISI[k]:
            st.markdown(f'<div class="venue-card"><div class="venue-info"><h4>{m["ad"]}</h4><p>{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank">📍 KONUM</a></div></div>', unsafe_allow_html=True)
