import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. VERİ SETİ ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}, {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"}, {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"}, {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"}, {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"}, {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"}, {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}, {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"}, {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"}, {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}, {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"}, {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"}, {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"}, {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"}, {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"}, {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}, {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"}, {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"}, {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"}, {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"}, {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"}, {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"}, {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}, {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"}, {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"}, {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"}, {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz / Geniş Sahil", "ln": "http://google.com/32"}, {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz / Doğa Harikası", "ln": "http://google.com/33"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}, {"ad": "Kraft", "oz": "Craft Beer & Mood", "ln": "http://google.com/35"}, {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"}, {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "http://google.com/37"}, {"ad": "The Public House", "oz": "Şehir Kulübü", "ln": "http://google.com/38"}]
}

# --- 3. CSS (KESİN ÇÖZÜM: TAŞMAYI ENGELLEYEN VE HER ŞEYİ SIĞDIRAN YAPI) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    
    /* 1. Sayfa daraltma - Kenar boşluklarını sıfıra yakın yaptık */
    .block-container {
        padding: 0.5rem 0.5rem !important;
    }

    /* 2. Dashboard Başlığı */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;
    }
    .main-header h1 { font-size: 22px !important; margin: 0; }
    .main-header p { font-size: 12px !important; margin: 0; opacity: 0.8; }

    /* 3. MOBİLDE KOLONLARI YAN YANA TUTAN ASIL GÜÇ */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; /* Alt satıra geçmeyi KESİN olarak engeller */
        width: 100% !important;
        gap: 4px !important;
        margin-bottom: 5px !important;
    }

    [data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important; /* Streamlit'in mobildeki minimum genişlik kuralını ezer */
        width: 25% !important;
    }

    /* 4. Butonları İncecik ve Kompakt Hale Getirme */
    div.stButton > button {
        background: white !important;
        color: #1e293b !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        width: 100% !important;
        height: 60px !important; /* Dikeyde yer kazanmak için kısalttık */
        padding: 0px !important;
        font-size: 9px !important; /* Mobilde taşmaması için küçük font */
        font-weight: 800 !important;
        line-height: 1 !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
    }

    /* 5. Mekan Kartları */
    .venue-card {
        background: white; padding: 10px; border-radius: 10px;
        margin-bottom: 8px; border: 1px solid #e2e8f0;
        display: flex; justify-content: space-between; align-items: center;
    }
    .venue-info h4 { margin: 0; font-size: 13px; color: #0f172a; }
    .venue-info p { margin: 1px 0 0 0; font-size: 10px; color: #64748b; }
    .venue-link a {
        background: #2c5364; color: white !important;
        padding: 5px 8px; border-radius: 4px; text-decoration: none; font-size: 9px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Misafir Dashboard</p></div>', unsafe_allow_html=True)

# 4x2 BUTON GRİDİ (Streamlit columns kullanarak ama CSS ile yan yana zorlayarak)
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("🤖\nAsistan", key="b1"): st.session_state.secili_sayfa = "asistan"
with c2: 
    if st.button("🍽️\nYemek", key="b2"): st.session_state.secili_sayfa = "yemek"
with c3: 
    if st.button("☕\nKahve", key="b3"): st.session_state.secili_sayfa = "kahve"
with c4: 
    if st.button("🏖️\nBeach", key="b4"): st.session_state.secili_sayfa = "beach"

c5, c6, c7, c8 = st.columns(4)
with c5: 
    if st.button("🍸\nKokteyl", key="b5"): st.session_state.secili_sayfa = "kokteyl"
with c6: 
    if st.button("🎉\nEğlence", key="b6"): st.session_state.secili_sayfa = "eglence"
with c7: 
    if st.button("🚕\nTaksi", key="b7"): st.session_state.secili_sayfa = "taksi"
with c8: 
    if st.button("💊\nEczane", key="b8"): st.session_state.secili_sayfa = "eczane"

st.divider()

# --- 5. FONKSİYONLAR ---
def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div class="venue-info"><h4>{m["ad"]}</h4><p>{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank">📍 KONUM</a></div></div>', unsafe_allow_html=True)

# --- 6. SAYFA İÇERİKLERİ ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    u_in = st.chat_input("Mesajınızı yazın...")
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
            with st.chat_message("assistant"): st.write("Anlayamadım, lütfen yukarıdaki kategorileri kullanın.")

elif s == "yemek":
    st.markdown("##### 🍽️ Restoranlar & Pizza")
    kart_bas("yemek")
    kart_bas("pizza")

elif s == "kahve":
    st.markdown("##### ☕ Kahve & Tatlı")
    kart_bas("kahve")

elif s == "beach":
    st.markdown("##### 🏖️ Beach & Plajlar")
    kart_bas("beach")

elif s == "kokteyl":
    st.markdown("##### 🍸 Kokteyl & Alkol")
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
