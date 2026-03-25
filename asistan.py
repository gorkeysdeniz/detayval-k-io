import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

# URL parametrelerini bıraktık, Session State ile devam ediyoruz
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. CSS (BÜYÜK VE SIĞAN YAPI) ---
# Hem masaüstünde hem mobilde sığması için hesaplamayı optimize ettim.
# Font ve buton boyutlarını büyüttüm. Kenar boşluklarını daralttım.
st.markdown("""
    <style>
    /* 1. Sayfa Kenar Boşluklarını Sıfırla (Büyük butonlar için yer açar) */
    .block-container {
        padding-left: 0.6rem !important;
        padding-right: 0.6rem !important;
        padding-top: 1.5rem !important;
    }

    /* 2. Yatay Bloğu Yan Yana Sığmaya Zorla */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: stretch !important;
        width: 100% !important;
        gap: 6px !important;
        margin-bottom: 8px !important;
    }

    /* 3. Kolon Genişliğini Hesapla (%25 - gap) */
    [data-testid="column"] {
        flex: 1 1 calc(25% - 6px) !important;
        min-width: calc(25% - 6px) !important;
        width: calc(25% - 6px) !important;
    }

    /* 4. BUTON TASARIMI VE BOYUTLARI */
    div.stButton > button {
        width: 100% !important;
        height: 95px !important; /* Yüksekliği artırdım, daha büyük görünsün */
        padding: 4px !important; /* İç boşluğu azalttım, metinlere yer kalsın */
        border-radius: 15px !important; /* Daha yuvarlak köşeler */
        
        /* Font ve Metin Ayarları */
        font-weight: 800 !important;
        font-size: 13px !important; /* Mobilde taşmayı önlemek için 13px en güvenlisi */
        line-height: 1.1 !important;
        
        /* Metni Dikeyde Ortala */
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        word-wrap: break-word !important;
        white-space: pre-wrap !important;
    }

    /* Emojilerin boyutunu biraz küçülterek metne yer kazanalım (Pinterest gibi) */
    div.stButton > button p {
        margin-top: -8px !important;
    }
    
    /* 5. Mekan Kartları */
    .venue-card {
        background: white !important; padding: 12px !important; border-radius: 12px !important; margin-bottom: 8px !important;
        border: 1px solid #e2e8f0 !important; display: flex !important; justify-content: space-between !important; align-items: center !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DASHBOARD ÜST PANEL ---
# Başlık kısmını koruyoruz
st.markdown('<div class="main-header" style="background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%); color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;"><h1 style="font-size:24px; margin:0;">🏡 Ayvalık Asistanı</h1><p style="font-size:12px; margin:0; opacity:0.8;">Premium Misafir Dashboard</p></div>', unsafe_allow_html=True)

# --- 4. HIZLI VE BÜYÜK BUTONLAR (TEK SATIRDA) ---
# St.columns kullanıyoruz ama CSS sayesinde yan yana kalıyorlar.
# URL parametrelerini attık, tıklayınca takılmadan sayfa değişir.

col_top = st.columns(4)
with col_top[0]:
    if st.button("🤖\nAsistan", key="nb1"): st.session_state.secili_sayfa = "asistan"
with col_top[1]:
    if st.button("🍽️\nYemek", key="nb2"): st.session_state.secili_sayfa = "yemek"
with col_top[2]:
    if st.button("☕\nKahve", key="nb3"): st.session_state.secili_sayfa = "kahve"
with col_top[3]:
    if st.button("🏖️\nBeach", key="nb4"): st.session_state.secili_sayfa = "beach"

col_bot = st.columns(4)
with col_bot[0]:
    if st.button("🍸\nKokteyl", key="nb5"): st.session_state.secili_sayfa = "kokteyl"
with col_bot[1]:
    if st.button("🎉\nEğlence", key="nb6"): st.session_state.secili_sayfa = "eglence"
with col_bot[2]:
    if st.button("🚕\nTaksi", key="nb7"): st.session_state.secili_sayfa = "taksi"
with col_bot[3]:
    if st.button("💊\nEczane", key="nb8"): st.session_state.secili_sayfa = "eczane"

st.divider()

# --- 5. İÇERİĞİ KORUYAN VERİ SETİ ---
# (Öncekiyle aynı şekilde tüm listenizi buraya ekleyebilirsiniz)
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}, {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"}, {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"}, {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"}, {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"}, {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"}, {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}, {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"}, {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"}, {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}, {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"}, {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"}, {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"}, {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"}, {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"}, {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}, {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"}, {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"}, {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"}, {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"}, {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"}, {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"}, {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}, {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"}, {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"}, {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"}, {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz Sahil", "ln": "http://google.com/32"}, {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz Sahil", "ln": "http://google.com/33"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}, {"ad": "Kraft", "oz": "Craft Beer", "ln": "http://google.com/35"}, {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"}, {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "http://google.com/37"}]
}

def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div><h4 style="margin:0; font-size:14px;">{m["ad"]}</h4><p style="margin:0; font-size:11px; color:#666;">{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:6px 10px; border-radius:6px; text-decoration:none; font-size:10px; font-weight:bold;">📍 KONUM</a></div></div>', unsafe_allow_html=True)

# --- 6. İÇERİĞİ KORUYAN SAYFA MANTIĞI ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    u_in = st.chat_input("Pizza, Taksi, Kahve...")
    if u_in:
        with st.chat_message("user"): st.write(u_in)
        low = u_in.lower()
        found = False
        for k in MEKAN_VERISI.keys():
            if k in low:
                with st.chat_message("assistant"):
                    st.success(f"İşte **{k.upper()}** önerileri:")
                    kart_bas(k)
                found = True
                break
        if not found:
            with st.chat_message("assistant"): st.write("Lütfen yukarıdaki menüleri kullanın.")

elif s == "yemek":
    st.markdown("##### 🍽️ Yemek & Pizza")
    kart_bas("yemek")
    kart_bas("pizza")
elif s == "kahve":
    st.markdown("##### ☕ Kahve & Tatlı")
    kart_bas("kahve")
elif s == "beach":
    st.markdown("##### 🏖️ Beach & Plaj")
    kart_bas("beach")
elif s == "kokteyl":
    st.markdown("##### 🍸 Kokteyl & Bar")
    kart_bas("kokteyl")
elif s == "eglence":
    st.markdown("##### 🎉 Eğlence")
    kart_bas("eglence")
elif s == "taksi":
    st.markdown("##### 🚕 Taksi")
    st.markdown('<div class="venue-card"><h4>Sarımsaklı Taksi</h4><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown("##### 💊 Eczane")
    st.markdown('<div class="venue-card"><h4>Nöbetçi Eczaneler</h4><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
