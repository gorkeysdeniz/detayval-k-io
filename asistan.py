import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. CSS (KESİN ÇÖZÜM: TRANSPARENT OVERLAY & GRID) ---
st.markdown("""
    <style>
    /* Sayfa genel ayarları */
    .block-container { padding: 1rem 0.5rem !important; max-width: 100% !important; }
    html, body, [data-testid="stAppViewContainer"] { overflow-x: hidden !important; }

    /* Pinterest Grid Yapısı */
    .p-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        width: 100%;
        margin-bottom: 20px;
    }

    /* Görsel Kutular */
    .p-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        height: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        position: relative;
    }
    .p-icon { font-size: 26px; margin-bottom: 2px; }
    .p-text { font-size: 13px; font-weight: 700; color: #1e293b; }

    /* GÖRÜNMEZ BUTON KATMANI (Sihirli Kısım) */
    /* Streamlit butonunu tamamen şeffaf yapıp kutunun üzerine yayıyoruz */
    .stButton {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 10;
    }
    .stButton > button {
        width: 100% !important;
        height: 100px !important;
        background: transparent !important;
        color: transparent !important; /* btn_1 yazılarını gizler */
        border: none !important;
        box-shadow: none !important;
    }
    .stButton > button:hover { background: rgba(0,0,0,0.03) !important; }
    .stButton > button:active { background: rgba(0,0,0,0.07) !important; }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;
    }
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANEL BAŞLIĞI ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# --- 4. BUTON GRİD SİSTEMİ ---
# İçeriğine dokunmadan, butonları bu grid yapısına oturtuyoruz.
st.markdown('<div class="p-grid">', unsafe_allow_html=True)

def menu_item(label, icon, target, key):
    # Bu yapı görsel kutu ile görünmez butonu üst üste bindirir
    with st.container():
        st.markdown(f'<div class="p-box"><div class="p-icon">{icon}</div><div class="p-text">{label}</div>', unsafe_allow_html=True)
        if st.button("", key=key): # Boş etiketli buton tamamen şeffaftır
            st.session_state.secili_sayfa = target
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# Grid elemanlarını st.columns ile yan yana diziyoruz
c1, c2, c3 = st.columns(3)
with c1: menu_item("Asistan", "🤖", "asistan", "b1")
with c2: menu_item("Yemek", "🍽️", "yemek", "b2")
with c3: menu_item("Pizza", "🍕", "pizza", "b3")

c4, c5, c6 = st.columns(3)
with c4: menu_item("Kahve", "☕", "kahve", "b4")
with c5: menu_item("Beach", "🏖️", "beach", "b5")
with c6: menu_item("Kokteyl", "🍸", "kokteyl", "b6")

c7, c8, c9 = st.columns(3)
with c7: menu_item("Eğlence", "🎉", "eglence", "b7")
with c8: menu_item("Taksi", "🚕", "taksi", "b8")
with c9: menu_item("Eczane", "💊", "eczane", "b9")

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# --- 5. MEKAN VERİSİ (DOKUNULMADI) ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}, {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"}, {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"}, {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"}, {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"}, {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"}, {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}, {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"}, {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"}, {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}, {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"}, {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"}, {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"}, {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"}, {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"}, {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}, {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"}, {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"}, {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"}, {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"}, {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"}, {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"}, {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}, {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"}, {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"}, {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"}, {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/32"}, {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/33"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}, {"ad": "Kraft", "oz": "Craft Beer", "ln": "http://google.com/35"}, {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"}, {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "http://google.com/37"}]
}

# --- 6. FONKSİYONLAR (DOKUNULMADI) ---
def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'''
                <div class="venue-card">
                    <div>
                        <h4 style="margin:0; font-size:14px;">{m["ad"]}</h4>
                        <p style="margin:0; font-size:11px; color:#666;">{m["oz"]}</p>
                    </div>
                    <div class="venue-link">
                        <a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-size:10px; font-weight:bold;">📍 KONUM</a>
                    </div>
                </div>
            ''', unsafe_allow_html=True)

# --- 7. SAYFA MANTIĞI ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    u_in = st.chat_input("Pizza, Kahve, Plaj...")
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
elif s == "taksi":
    st.markdown('<div class="venue-card"><h4>🚕 Sarımsaklı Taksi</h4><div class="venue-link"><a href="tel:02663961010" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown('<div class="venue-card"><h4>💊 Nöbetçi Eczaneler</h4><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    st.markdown(f"##### ✨ {s.capitalize()} Önerileri")
    kart_bas(s)
