import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. CSS (ÜSTTE SABİT, SAĞA KAYAN MODERN MENÜ) ---
st.markdown("""
    <style>
    /* Sayfa genel ayarları */
    .block-container { padding: 0.5rem !important; max-width: 100% !important; }
    
    /* YATAY KAYDIRILABİLİR MENÜ (Yönetim Paneli Tarzı) */
    .scroll-menu {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
        background-color: white;
        padding: 10px 5px;
        position: sticky;
        top: 0;
        z-index: 1000;
        border-bottom: 1px solid #eee;
        gap: 10px;
        -webkit-overflow-scrolling: touch; /* Mobilde yumuşak kaydırma */
    }
    
    /* Kaydırma çubuğunu gizle */
    .scroll-menu::-webkit-scrollbar { display: none; }

    /* MENÜ BUTONLARI */
    .menu-item {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-width: 75px;
        padding: 8px;
        background: #f8fafc;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        position: relative;
    }

    .menu-icon { font-size: 20px; }
    .menu-text { font-size: 11px; font-weight: 700; color: #475569; margin-top: 2px; }

    /* GERÇEK STREAMLIT BUTONUNU ÜSTE MASKELE */
    .stButton {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 10;
    }
    .stButton > button {
        width: 100% !important;
        height: 100% !important;
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 10px; border-radius: 8px; text-align: center; margin-bottom: 10px; font-size: 12px;
    }
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ÜST BAŞLIK VE YATAY MENÜ ---
st.markdown('<div class="main-header">🏡 Ayvalık Misafir Asistanı</div>', unsafe_allow_html=True)

# Yatay Menü Başlangıcı
st.markdown('<div class="scroll-menu">', unsafe_allow_html=True)

def create_tab(label, icon, target, key):
    # Bu yapı butonları yan yana dizer ve üzerlerine görünmez tık katmanı koyar
    with st.container():
        st.markdown(f'''
            <div class="menu-item">
                <div class="menu-icon">{icon}</div>
                <div class="menu-text">{label}</div>
        ''', unsafe_allow_html=True)
        if st.button("", key=key):
            st.session_state.secili_sayfa = target
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# Menü Elemanları (Yan yana dizilirler)
# Yan yana gelmeleri için columns kullanmıyoruz, CSS 'flex' hallediyor
col_list = st.columns([1,1,1,1,1,1,1,1,1]) # 9 buton için alan açtık

with col_list[0]: create_tab("Asistan", "🤖", "asistan", "m1")
with col_list[1]: create_tab("Yemek", "🍽️", "yemek", "m2")
with col_list[2]: create_tab("Pizza", "🍕", "pizza", "m3")
with col_list[3]: create_tab("Kahve", "☕", "kahve", "m4")
with col_list[4]: create_tab("Beach", "🏖️", "beach", "m5")
with col_list[5]: create_tab("Kokteyl", "🍸", "kokteyl", "m6")
with col_list[6]: create_tab("Eğlence", "🎉", "eglence", "m7")
with col_list[7]: create_tab("Taksi", "🚕", "taksi", "m8")
with col_list[8]: create_tab("Eczane", "💊", "eczane", "m9")

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# --- 4. MEKAN VERİSİ (DOKUNULMADI) ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}, {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "http://google.com/3"}, {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "http://google.com/4"}, {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "http://google.com/5"}, {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "http://google.com/6"}, {"ad": "Declan", "oz": "Modern Coffee", "ln": "http://google.com/7"}, {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "http://google.com/8"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}, {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "http://google.com/11"}, {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "http://google.com/12"}, {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "http://google.com/13"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}, {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı", "ln": "http://google.com/16"}, {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "http://google.com/17"}, {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "http://google.com/18"}, {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "http://google.com/19"}, {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "http://google.com/20"}, {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "http://google.com/21"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}, {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "http://google.com/13"}, {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "http://google.com/22"}, {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "http://google.com/23"}, {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "http://google.com/24"}, {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "http://google.com/25"}, {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "http://google.com/26"}, {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "http://google.com/27"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}, {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "http://google.com/29"}, {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "http://google.com/30"}, {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/31"}, {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/32"}, {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz Plaj", "ln": "http://google.com/33"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}, {"ad": "Kraft", "oz": "Craft Beer", "ln": "http://google.com/35"}, {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "http://google.com/36"}, {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "http://google.com/37"}]
}

# --- 5. FONKSİYONLAR (DOKUNULMADI) ---
def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div><h4 style="margin:0; font-size:14px;">{m["ad"]}</h4><p style="margin:0; font-size:11px; color:#666;">{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-size:10px; font-weight:bold;">📍 KONUM</a></div></div>', unsafe_allow_html=True)

# --- 6. SAYFA MANTIĞI ---
s = st.session_state.secili_sayfa
st.subheader(f"✨ {s.capitalize()}")

if s == "asistan":
    st.chat_input("Nereye gitmek istersiniz?")
elif s == "taksi":
    st.markdown('<div class="venue-card"><h4>🚕 Sarımsaklı Taksi</h4><div class="venue-link"><a href="tel:02663961010" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown('<div class="venue-card"><h4>💊 Nöbetçi Eczaneler</h4><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
else:
    kart_bas(s)
