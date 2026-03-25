import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

# Tıklamaları yakalamak için Query Parametresi (Hızlı geçiş için)
if "p" in st.query_params:
    st.session_state.secili_sayfa = st.query_params["p"]

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. VERİ SETİ (TAM LİSTE - HİÇBİRİ EKSİK DEĞİL) ---
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"},
        {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"},
        {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"},
        {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"},
        {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"},
        {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"},
        {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"},
        {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"},
        {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"},
        {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"},
        {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"},
        {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"},
        {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"},
        {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"},
        {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"},
        {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"},
        {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"},
        {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"},
        {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"},
        {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"},
        {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"},
        {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"},
        {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"},
        {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"},
        {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"},
        {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"},
        {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/32"},
        {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/33"}
    ],
    "eglence": [
        {"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"},
        {"ad": "Kraft", "oz": "Craft Beer", "ln": "http://google.com/35"},
        {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"},
        {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "http://google.com/37"}
    ]
}

# --- 3. CSS (PINTEREST TARZI GRID MENÜ) ---
st.markdown("""
    <style>
    .block-container { padding: 1rem 0.5rem !important; }
    
    .menu-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        background: white;
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .menu-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 15px 5px;
        text-decoration: none;
        color: #444;
        font-size: 10px;
        font-weight: 600;
        border: 0.5px solid #f9f9f9;
        transition: background 0.2s;
        height: 80px;
    }

    .menu-item:active { background: #f0f2f6; }
    .menu-item span { font-size: 24px; margin-bottom: 5px; }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;
    }
    
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANEL ÜST ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Misafir Rehberi</p></div>', unsafe_allow_html=True)

# --- 5. GRID MENÜ ---
st.markdown("""
    <div class="menu-grid">
        <a href="?p=asistan" class="menu-item" target="_self"><span>🤖</span>Asistan</a>
        <a href="?p=yemek" class="menu-item" target="_self"><span>🍽️</span>Yemek</a>
        <a href="?p=kahve" class="menu-item" target="_self"><span>☕</span>Kahve</a>
        <a href="?p=beach" class="menu-item" target="_self"><span>🏖️</span>Beach</a>
        <a href="?p=kokteyl" class="menu-item" target="_self"><span>🍸</span>Kokteyl</a>
        <a href="?p=eglence" class="menu-item" target="_self"><span>🎉</span>Eğlence</a>
        <a href="?p=taksi" class="menu-item" target="_self"><span>🚕</span>Taksi</a>
        <a href="?p=eczane" class="menu-item" target="_self"><span>💊</span>Eczane</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. FONKSİYONLAR ---
def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'''
                <div class="venue-card">
                    <div><h4 style="margin:0; font-size:14px;">{m["ad"]}</h4><p style="margin:0; font-size:11px; color:#666;">{m["oz"]}</p></div>
                    <a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:6px 10px; border-radius:6px; text-decoration:none; font-size:10px; font-weight:bold;">📍 KONUM</a>
                </div>
            ''', unsafe_allow_html=True)

# --- 7. SAYFA İÇERİKLERİ ---
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
    st.markdown("##### 🏖️ Beach & Plajlar")
    kart_bas("beach")
elif s == "kokteyl":
    st.markdown("##### 🍸 Kokteyl & Bar")
    kart_bas("kokteyl")
elif s == "eglence":
    st.markdown("##### 🎉 Eğlence")
    kart_bas("eglence")
elif s == "taksi":
    st.markdown("##### 🚕 Taksi")
    st.markdown('<div class="venue-card"><h4>Sarımsaklı Taksi</h4><a href="tel:02663961010" style="color:#2c5364; font-weight:bold; text-decoration:none;">📞 ARA: 0266 396 10 10</a></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown("##### 💊 Nöbetçi Eczaneler")
    st.markdown('<a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank" style="display:block; text-align:center; background:#2c5364; color:white; padding:10px; border-radius:8px; text-decoration:none;">LİSTEYİ GÖR</a>', unsafe_allow_html=True)
