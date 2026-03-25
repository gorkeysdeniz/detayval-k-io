import streamlit as st
import requests  # Bu kütüphane Streamlit'te hazır gelir, ekleme yapmana gerek yok.
import json


# --- 1. AYARLAR ---
st.set_page_config(page_title="Detayvalik.io Asistan", layout="centered", page_icon="🏡")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "🤖 Asistan"

# --- 2. CSS (DEĞİŞMEDİ - DEV BUTONLAR & PREMİUM GÖRÜNÜM) ---
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
    .award-text { margin: 2px 0 0 0; font-size: 13px; color: #b45309; font-weight: 600; }
    .standard-text { margin: 2px 0 0 0; font-size: 13px; color: #64748b; }
    
    .venue-link a {
        background: #2c5364; color: white; padding: 10px 18px; border-radius: 10px;
        text-decoration: none; font-size: 12px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MEKAN VERİSİ (LİNKLER DÜZELTİLDİ) ---
# Link yapısı: https://www.google.com/maps/search/?api=1&query=Mekan+Adı+Ayvalık
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "https://www.google.com/maps/search/?api=1&query=Pinos+Cafe+Ayvalık"},
        {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "https://www.google.com/maps/search/?api=1&query=Crow+Coffee+Ayvalık"},
        {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "https://www.google.com/maps/search/?api=1&query=Ivy+Ayvalık"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "https://www.google.com/maps/search/?api=1&query=Daisy+Küçükköy"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "https://www.google.com/maps/search/?api=1&query=Nona+Cunda"},
        {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "https://www.google.com/maps/search/?api=1&query=Cafe+Melin+Cunda"},
        {"ad": "Declan", "oz": "Modern Coffee", "ln": "https://www.google.com/maps/search/?api=1&query=Declan+Coffee+Ayvalık"},
        {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "https://www.google.com/maps/search/?api=1&query=AIMA+Ayvalık"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "https://www.google.com/maps/search/?api=1&query=Pizza+Teo+Ayvalık"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "https://www.google.com/maps/search/?api=1&query=Uno+Cunda"},
        {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "https://www.google.com/maps/search/?api=1&query=Tino+Ristorante+Ayvalık"},
        {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "https://www.google.com/maps/search/?api=1&query=Küçük+İtalya+Ayvalık"},
        {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "https://www.google.com/maps/search/?api=1&query=Cunda+Luna"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Gault Millau Ödülü", "ln": "https://www.google.com/maps/search/?api=1&query=Ayna+Cunda"},
        {"ad": "By Nihat", "oz": "🏅 Gault Millau Ödülü", "ln": "https://www.google.com/maps/search/?api=1&query=By+Nihat+Cunda"},
        {"ad": "Ayvalık Balıkçısı", "oz": "🏅 Gault Millau Ödülü", "ln": "https://www.google.com/maps/search/?api=1&query=Ayvalık+Balıkçısı"},
        {"ad": "L'arancia", "oz": "Ege Mutfağı", "ln": "https://www.google.com/maps/search/?api=1&query=Larancia+Cunda"},
        {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "https://www.google.com/maps/search/?api=1&query=Ritüel+1873+Cunda"},
        {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "https://www.google.com/maps/search/?api=1&query=Köşebaşı+Ayvalık"},
        {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "https://www.google.com/maps/search/?api=1&query=Papazın+Evi+Ayvalık"},
        {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "https://www.google.com/maps/search/?api=1&query=Karina+Ayvalık"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "https://www.google.com/maps/search/?api=1&query=Ritüel+1873+Cunda"},
        {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "https://www.google.com/maps/search/?api=1&query=Cunda+Luna"},
        {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "https://www.google.com/maps/search/?api=1&query=Ciello+Cunda"},
        {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "https://www.google.com/maps/search/?api=1&query=Vino+Şarap+Evi+Cunda"},
        {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "https://www.google.com/maps/search/?api=1&query=De+Jong+Cocktails+Cunda"},
        {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "https://www.google.com/maps/search/?api=1&query=Cunda+Frenk"},
        {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "https://www.google.com/maps/search/?api=1&query=Felicita+Küçükköy"},
        {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "https://www.google.com/maps/search/?api=1&query=Cunda+Kaktüs"}
    ],
    "eglence": [
        {"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "https://www.google.com/maps/search/?api=1&query=La+Fuga+Cunda"},
        {"ad": "Kraft", "oz": "Craft Beer", "ln": "https://www.google.com/maps/search/?api=1&query=Kraft+Ayvalık"},
        {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "https://www.google.com/maps/search/?api=1&query=Afişe+Sahne+Ayvalık"},
        {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "https://www.google.com/maps/search/?api=1&query=Aksi+Pub+Ayvalık"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "Ücretli Beach", "ln": "https://www.google.com/maps/search/?api=1&query=Ajlan+Eos+Beach"},
        {"ad": "Kesebir Cunda", "oz": "Ücretli Beach", "ln": "https://www.google.com/maps/search/?api=1&query=Kesebir+Beach+Cunda"},
        {"ad": "Sea Resort / Long", "oz": "Ücretli Beach", "ln": "https://www.google.com/maps/search/?api=1&query=Sea+Resort+Sarımsaklı"},
        {"ad": "Surya Beach", "oz": "Ücretli Beach", "ln": "https://www.google.com/maps/search/?api=1&query=Surya+Beach+Sarımsaklı"},
        {"ad": "Sarımsaklı Plajları", "oz": "Ücretsiz Plaj", "ln": "https://www.google.com/maps/search/?api=1&query=Sarımsaklı+Plajı"},
        {"ad": "Badavut Plajı", "oz": "Ücretsiz Plaj", "ln": "https://www.google.com/maps/search/?api=1&query=Badavut+Plajı"}
    ]
}

# ... (Diğer kısımlar aynı kalsın, 4. Bölümü şununla değiştir) ...

# --- 4. HİBRİT ASİSTAN ZEKA (GEMINI 2.5 FLASH GÜNCEL) ---
def asistan_cevap(soru):
    soru_lower = soru.lower()
    
    # KADEME 1: LOKAL VERİ (Senin listendeki mekanlar)
    for kategori, mekanlar in MEKAN_VERISI.items():
        if kategori in soru_lower:
            isimler = [m['ad'] for m in mekanlar[:3]]
            return f"Detayvalik.io rehberinden seçtiklerim: **{', '.join(isimler)}** 😊"

    # KADEME 2: GEMINI 2.5 FLASH (API Bağlantısı)
    # st.secrets içinde GEMINI_API_KEY tanımlı olmalıdır.
    api_key = st.secrets["GEMINI_API_KEY"]
    
    # Google AI Studio'daki en güncel endpoint: v1beta ve gemini-2.5-flash
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": f"Sen bir Ayvalık rehberisin. Elindeki liste şudur: {MEKAN_VERISI}. Bu listede olmayan yerleri de (örneğin kahvaltı mekanları, tostçular, gezilecek yerler) genel bilgilerinle yanıtla. Soru: {soru}. Çok kısa ve samimi cevap ver."}]
        }]
    }

    try:
        # Zaman aşımını 15 saniye yaptık ki AI düşünürken kopmasın
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=15)
        result = response.json()
        
        if "candidates" in result:
            # Başarılı yanıt
            return result["candidates"][0]["content"]["parts"][0]["text"]
        elif "error" in result:
            # Hata mesajını doğrudan ekrana basıyoruz ki sorunu görelim
            return f"🚨 Gemini 2.5 Hatası: {result['error']['message']}"
        else:
            return "Şu an cevap hazırlayamadım, tekrar dener misin? ✨"
            
    except Exception as e:
        # Bağlantı veya kütüphane hatası olursa:
        return f"🚨 Bağlantı Hatası: {str(e)}"
# --- 5. ARAYÜZ ---
st.markdown('<div class="header-container"><h2>🏡 Detayvalik.io Asistan</h2></div>', unsafe_allow_html=True)

kategoriler = ["🤖 Asistan", "🍽️ Yemek", "🍕 Pizza", "☕ Kahve", "🍸 Kokteyl", "🎉 Eğlence", "🏖️ Beach", "🚕 Taksi", "💊 Eczane"]
secim = st.pills("Kategori Seçin", kategoriler, selection_mode="single", default="🤖 Asistan")

st.divider()

# --- 6. SAYFA MANTIĞI ---
if secim == "🤖 Asistan":
    if not st.session_state.messages:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown("👋 **Merhaba! Ben Detayvalik.io Asistanınız.** \n\nAyvalık'ta ödüllü lezzet duraklarından en iyi plajlara kadar size rehberlik edebilirim. Ne sormak istersiniz?")

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Nerede pizza yenir?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant", avatar="🤖"):
            response = asistan_cevap(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

elif secim == "🚕 Taksi":
    st.markdown('<div class="venue-card"><div><h4>🚕 Sarımsaklı Taksi</h4><p class="standard-text">7/24 Hızlı Ulaşım</p></div><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
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
