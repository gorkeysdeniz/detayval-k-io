import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. YENİ NESİL GRID UI SİSTEMİ (CSS) ---
st.markdown("""
    <style>
    /* Streamlit'in standart boşluklarını temizle */
    .block-container { padding: 1rem 0.5rem !important; max-width: 100% !important; }
    [data-testid="stHeader"] {display: none;}
    
    /* PINTEREST GRID YAPISI */
    .p-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* Kesin yan yana 3 tane */
        gap: 8px;
        padding: 5px;
        width: 100%;
        box-sizing: border-box;
    }

    /* CUSTOM BUTON TASARIMI */
    .p-btn {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        height: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
        text-decoration: none;
        color: #1e293b;
    }

    .p-btn:active { transform: scale(0.95); background: #f8fafc; border-color: #2c5364; }
    .p-icon { font-size: 28px; margin-bottom: 5px; }
    .p-text { font-size: 13px; font-weight: 700; line-height: 1.2; }

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

# --- 3. PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# --- 4. HTML TABANLI BUTON SİSTEMİ ---
# Streamlit butonları yerine HTML Linkleri kullanıyoruz (Sayfa yenilemeden session_state tetikler)
# 'p' parametresi ile hızlı geçiş sağlıyoruz
if "p" in st.query_params:
    st.session_state.secili_sayfa = st.query_params["p"]

st.markdown("""
    <div class="p-grid">
        <a href="?p=asistan" target="_self" class="p-btn"><div class="p-icon">🤖</div><div class="p-text">Asistan</div></a>
        <a href="?p=yemek" target="_self" class="p-btn"><div class="p-icon">🍽️</div><div class="p-text">Yemek</div></a>
        <a href="?p=pizza" target="_self" class="p-btn"><div class="p-icon">🍕</div><div class="p-text">Pizza</div></a>
        <a href="?p=kahve" target="_self" class="p-btn"><div class="p-icon">☕</div><div class="p-text">Kahve</div></a>
        <a href="?p=beach" target="_self" class="p-btn"><div class="p-icon">🏖️</div><div class="p-text">Beach</div></a>
        <a href="?p=kokteyl" target="_self" class="p-btn"><div class="p-icon">🍸</div><div class="p-text">Kokteyl</div></a>
        <a href="?p=eglence" target="_self" class="p-btn"><div class="p-icon">🎉</div><div class="p-text">Eğlence</div></a>
        <a href="?p=taksi" target="_self" class="p-btn"><div class="p-icon">🚕</div><div class="p-text">Taksi</div></a>
        <a href="?p=eczane" target="_self" class="p-btn"><div class="p-icon">💊</div><div class="p-text">Eczane</div></a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 5. İÇERİĞİ KORUYAN VERİ SETİ ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}, {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"}, {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"}, {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"}, {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"}, {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"}, {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}, {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"}, {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"}, {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}, {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"}, {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"}, {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"}, {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"}, {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"}, {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}, {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"}, {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"}, {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"}, {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"}, {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"}, {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"}, {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}, {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"}, {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"}, {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"}, {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/32"}, {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/33"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}, {"ad": "Kraft", "oz": "Craft Beer", "ln": "http://google.com/35"}, {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"}, {"ad": "Aksi Pub", "oz": "Pub Küül", "ln": "http://google.com/37"}]
}

def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div><h4 style="margin:0; font-size:14px;">{m["ad"]}</h4><p style="margin:0; font-size:11px; color:#666;">{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-size:10px; font-weight:bold;">📍 KONUM</a></div></div>', unsafe_allow_html=True)

# --- 6. SAYFA İÇERİKLERİ ---
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
    st.markdown("##### 🚕 Taksi")
    st.markdown('<div class="venue-card"><h4>Sarımsaklı Taksi</h4><div class="venue-link"><a href="tel:02663961010" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown("##### 💊 Eczane")
    st.markdown('<div class="venue-card"><h4>Nöbetçi Eczaneler</h4><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    st.markdown(f"##### ✨ {s.capitalize()} Önerileri")
    kart_bas(s)
