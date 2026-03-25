import streamlit as st
import time

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Misafir Asistanı", layout="centered", page_icon="🏡")

# Mesaj geçmişini ve seçim durumunu kontrol et
if "messages" not in st.session_state:
    st.session_state.messages = []
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "🤖 Asistan"

# --- 2. CSS (DEV MENÜLER VE ASİSTAN BALONLARI) ---
st.markdown("""
    <style>
    /* 1. MENÜLERİ (PILLS) DEVLEŞTİRME */
    .stPills [data-testid="stBaseButton-secondaryPill"] {
        padding: 20px 30px !important; /* Çok daha büyük tıklama alanı */
        font-size: 18px !important;    /* Okunabilir büyük font */
        border-radius: 15px !important;
        border: 2px solid #2c5364 !important;
        background-color: white !important;
        margin: 5px !important;
    }
    
    /* Seçili olan butonu vurgula */
    .stPills [data-active="true"] {
        background: linear-gradient(135deg, #2c5364 0%, #0f2027 100%) !important;
        color: white !important;
    }

    /* 2. ASİSTAN KARŞILAMA VE MESAJ TASARIMI */
    .header-container {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 30px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    /* 3. MEKAN KARTLARI */
    .venue-card {
        background: #ffffff; padding: 20px; border-radius: 20px; margin-bottom: 12px;
        border: 1px solid #f1f5f9; display: flex; justify-content: space-between; align-items: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .venue-info h4 { margin: 0; font-size: 18px; color: #1e293b; }
    .venue-info p { margin: 4px 0 0 0; font-size: 14px; color: #64748b; }
    
    .venue-link a {
        background: #2c5364; color: white; padding: 12px 20px; border-radius: 12px;
        text-decoration: none; font-size: 13px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TAM VERİ SETİ (EĞLENCE VE KOKTEYL DAHİL) ---
MEKAN_VERISI = {
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "https://maps.google.com/?q=Ayna+Cunda"},
        {"ad": "L'arancia Cunda", "oz": "🏅 Michelin Rehberi", "ln": "https://maps.google.com/?q=Larancia+Cunda"},
        {"ad": "By Nihat", "oz": "🐟 Efsanevi Balıkçı", "ln": "https://maps.google.com/?q=By+Nihat+Cunda"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "🍕 Odun Ateşi", "ln": "https://maps.google.com/?q=Pizza+Teo+Ayvalik"},
        {"ad": "Uno Cunda", "oz": "🇮🇹 İtalyan Klasiği", "ln": "https://maps.google.com/?q=Uno+Cunda"}
    ],
    "kahve": [
        {"ad": "Pino's Coffee", "oz": "☕ Butik Kahve", "ln": "https://maps.google.com/?q=Pinos+Coffee+Ayvalik"},
        {"ad": "Daisy Küçükköy", "oz": "🎨 Sanat & Kahve", "ln": "https://maps.google.com/?q=Daisy+Kucukkoy"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "🍸 İmza Kokteyller", "ln": "https://maps.google.com/?q=Rituel+1873+Cunda"},
        {"ad": "Cunda Luna", "oz": "🌙 Alkol & Atmosfer", "ln": "https://maps.google.com/?q=Cunda+Luna"},
        {"ad": "Ciello Cunda", "oz": "🌆 Roof Bar Keyfi", "ln": "https://maps.google.com/?q=Ciello+Cunda"}
    ],
    "eglence": [
        {"ad": "La Fuga Cunda", "oz": "🎵 Canlı Müzik & Dans", "ln": "https://maps.google.com/?q=La+Fuga+Cunda"},
        {"ad": "Afişe Sahne", "oz": "🎤 Performans Sanatları", "ln": "https://maps.google.com/?q=Afise+Sahne+Ayvalik"},
        {"ad": "Kraft Ayvalık", "oz": "🍺 Craft Beer & Müzik", "ln": "https://maps.google.com/?q=Kraft+Ayvalik"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "🏖️ Premium Beach", "ln": "https://maps.google.com/?q=Ajlan+Eos+Beach"},
        {"ad": "Surya Beach", "oz": "☀️ Modern Plaj", "ln": "https://maps.google.com/?q=Surya+Beach"}
    ]
}

# --- 4. ASİSTAN CEVAP MEKANİZMASI ---
def asistan_cevap(soru):
    soru = soru.lower()
    if "pizza" in soru: return "Ayvalık'ta pizza denince akla gelen ilk yerler Pizza Teo ve Uno'dur. Pizza sekmesinden hemen bakabilirsiniz! 🍕"
    if "kokteyl" in soru or "alkol" in soru: return "Akşam keyfi için Ritüel 1873 veya Ciello harika kokteyller sunar. 🍸"
    if "eğlence" in soru or "müzik" in soru: return "Geceyi hareketlendirmek isterseniz La Fuga veya Afişe Sahne tam size göre! 🎵"
    if "taksi" in soru: return "Ulaşım için '🚕 Taksi' sekmesine tıklayıp Sarımsaklı Taksi'yi anında arayabilirsiniz. 🚕"
    return "Ayvalık hakkında her şeyi bana sorabilirsiniz. Size mekan önerebilir veya konum paylaşabilirim. 😊"

# --- 5. ÜST PANEL ---
st.markdown('<div class="header-container"><h2>🏡 Ayvalık Misafir Asistanı</h2></div>', unsafe_allow_html=True)

# Kategori Menüsü (BÜYÜK)
kategoriler = ["🤖 Asistan", "🍽️ Yemek", "🍕 Pizza", "☕ Kahve", "🍸 Kokteyl", "🎉 Eğlence", "🏖️ Beach", "🚕 Taksi", "💊 Eczane"]
secim = st.pills("Kategori Seçin", kategoriler, selection_mode="single", default="🤖 Asistan")

st.divider()

# --- 6. SAYFA İÇERİKLERİ ---
if secim == "🤖 Asistan":
    # Karşılama Balonu (Eğer henüz mesaj yoksa)
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown("👋 **Merhaba! Ben SAYEM Misafir Asistanınız.** \n\nAyvalık'ta ne yapmak istersiniz? Size en iyi kokteyl barlarını, pizza mekanlarını veya plajları önerebilirim. Buyurun, sizi dinliyorum...")

    # Mesaj Geçmişini Göster
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Pizza, Kokteyl, Taksi nerede?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            full_response = asistan_cevap(prompt)
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

elif secim == "🚕 Taksi":
    st.markdown('<div class="venue-card"><div><h4>🚕 Sarımsaklı Taksi</h4><p>Hızlı Ulaşım</p></div><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
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
