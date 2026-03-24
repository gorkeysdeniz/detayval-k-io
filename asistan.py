import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. VERİ SETİ (KATEGORİLER VE İŞLETMELER) ---
# (Veri setini kısalttım, öncekiyle aynı şekilde tüm listenizi buraya ekleyebilirsiniz)
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "https://maps.google.com/?q=Pinos+Cafe+Ayvalik"},
        {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "https://maps.google.com/?q=Crow+Coffee+Ayvalik"},
        {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "https://maps.google.com/?q=Ivy+Ayvalik"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "https://maps.google.com/?q=Daisy+Kucukkoy"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "https://maps.google.com/?q=Nona+Cunda"},
        {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "https://maps.google.com/?q=Cafe+Melin"},
        {"ad": "Declan", "oz": "Modern Coffee", "ln": "https://maps.google.com/?q=Declan+Ayvalik"},
        {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "https://maps.google.com/?q=AIMA+Ayvalik"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "https://maps.google.com/?q=Pizza+Teo+Ayvalik"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "https://maps.google.com/?q=Uno+Cunda"},
        {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "https://maps.google.com/?q=Tino+Ristorante+Ayvalik"},
        {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "https://maps.google.com/?q=Kucuk+İtalya+Ayvalik"},
        {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "https://maps.google.com/?q=Cunda+Luna"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi / Ödüllü", "ln": "https://maps.google.com/?q=Ayna+Cunda"},
        {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi / Ödüllü", "ln": "https://maps.google.com/?q=Larancia+Cunda"},
        {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı / Ödüllü", "ln": "https://maps.google.com/?q=By+Nihat+Cunda"},
        {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "https://maps.google.com/?q=Rituel+1873+Cunda"},
        {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "https://maps.google.com/?q=Kosebasi+Ayvalik"},
        {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "https://maps.google.com/?q=Papazin+Evi+Ayvalik"},
        {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "https://maps.google.com/?q=Ayvalik+Balikcisi"},
        {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "https://maps.google.com/?q=Karina+Ayvalik"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "https://maps.google.com/?q=Rituel+1873+Cunda"},
        {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "https://maps.google.com/?q=Cunda+Luna"},
        {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "https://maps.google.com/?q=Ciello+Cunda"},
        {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "https://maps.google.com/?q=Vino+Sarap+Evi+Cunda"},
        {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "https://maps.google.com/?q=De+Jong+Cunda"},
        {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "https://maps.google.com/?q=Cunda+Frenk"},
        {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "https://maps.google.com/?q=Felicita+Kucukkoy"},
        {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "https://maps.google.com/?q=Cunda+Kaktus"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "https://maps.google.com/?q=Ajlan+Eos+Beach"},
        {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "https://maps.google.com/?q=Kesebir+Beach+Cunda"},
        {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "https://maps.google.com/?q=Sea+Resort+Ayvalik"},
        {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "https://maps.google.com/?q=Surya+Beach+Ayvalik"},
        {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz / Geniş Sahil", "ln": "https://maps.google.com/?q=Sarimsakli+Plajlari"},
        {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz / Doğa Harikası", "ln": "https://maps.google.com/?q=Badavut+Plaji"}
    ],
    "eglence": [
        {"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "https://maps.google.com/?q=La+Fuga+Cunda"},
        {"ad": "Kraft", "oz": "Craft Beer & Mood", "ln": "https://maps.google.com/?q=Kraft+Ayvalik"},
        {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "https://maps.google.com/?q=Afise+Sahne+Ayvalik"},
        {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "https://maps.google.com/?q=Aksi+Pub+Ayvalik"},
        {"ad": "The Public House", "oz": "Şehir Kulübü", "ln": "https://maps.google.com/?q=The+Public+House+Ayvalik"}
    ]
}

# --- 3. CSS (ZORLANMIŞ 4x2 GRİD & KARTLAR) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px; border-radius: 20px; text-align: center; margin-bottom: 25px;
    }
    
    /* BUTON GRİD SİSTEMİ (Masaüstü ve Mobilde 4 kolon zorlar) */
    .button-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-bottom: 20px;
    }

    /* Streamlit Butonlarını Stilize Etme */
    div.stButton > button {
        background: white !important;
        color: #1a202c !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        width: 100% !important;
        height: 85px !important;
        font-weight: 700 !important;
        font-size: 13px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02) !important;
        white-space: pre-wrap !important; /* Alt satıra geçebilmesi için */
    }
    div.stButton > button:hover { border-color: #2c5364 !important; transform: translateY(-2px); transition: 0.2s; }

    /* İşletme Kartları */
    .venue-card {
        background: white; padding: 15px; border-radius: 15px;
        margin-bottom: 12px; border: 1px solid #e2e8f0;
        display: flex; justify-content: space-between; align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .venue-info h4 { margin: 0; color: #1a202c; font-size: 16px; }
    .venue-info p { margin: 3px 0 0 0; color: #64748b; font-size: 12px; }
    .venue-link a {
        background: #2c5364; color: white !important;
        padding: 8px 14px; border-radius: 8px; text-decoration: none;
        font-size: 11px; font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. DASHBOARD ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Misafir Dashboard</p></div>', unsafe_allow_html=True)

# --- 4x2 MANUEL BUTON TASARIMI ---
# Streamlit kolonları yerine doğrudan yan yana dizilim için:
col_top = st.columns(4)
with col_top[0]:
    if st.button("🤖\nAsistan", key="btn1"): st.session_state.secili_sayfa = "asistan"
with col_top[1]:
    if st.button("🍽️\nYemek", key="btn2"): st.session_state.secili_sayfa = "yemek"
with col_top[2]:
    if st.button("☕\nKahve", key="btn3"): st.session_state.secili_sayfa = "kahve"
with col_top[3]:
    if st.button("🏖️\nBeach", key="btn4"): st.session_state.secili_sayfa = "beach"

col_bot = st.columns(4)
with col_bot[0]:
    if st.button("🍸\nKokteyl", key="btn5"): st.session_state.secili_sayfa = "kokteyl"
with col_bot[1]:
    if st.button("🎉\nEğlence", key="btn6"): st.session_state.secili_sayfa = "eglence"
with col_bot[2]:
    if st.button("🚕\nTaksi", key="btn7"): st.session_state.secili_sayfa = "taksi"
with col_bot[3]:
    if st.button("💊\nEczane", key="btn8"): st.session_state.secili_sayfa = "eczane"

st.divider()

# --- 5. FONKSİYONLAR ---
def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f"""
                <div class="venue-card">
                    <div class="venue-info">
                        <h4>{m['ad']}</h4>
                        <p>{m['oz']}</p>
                    </div>
                    <div class="venue-link">
                        <a href="{m['ln']}" target="_blank">📍 KONUM</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- 6. SAYFA İÇERİKLERİ ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.markdown("### 🤖 Size Nasıl Yardımcı Olabilirim?")
    user_input = st.chat_input("Örn: pizza, kahve, yemek...")
    
    if user_input:
        with st.chat_message("user"): st.write(user_input)
        input_low = user_input.lower()
        found = False
        
        # Akıllı Tarama: Cümle içinde anahtar kelime arar
        for key in MEKAN_VERISI.keys():
            if key in input_low:
                with st.chat_message("assistant"):
                    st.success(f"İşte **{key.upper()}** kategorisindeki önerilerim:")
                    kart_bas(key)
                found = True
                break
        
        if not found:
            with st.chat_message("assistant"):
                st.write("🤖 Aradığınızı tam anlayamadım ama yukarıdaki butonlardan tüm listeyi görebilirsiniz.")

elif s == "yemek":
    st.markdown("### 🍽️ Restoranlar")
    kart_bas("yemek")
    st.markdown("### 🍕 Pizza")
    kart_bas("pizza")

elif s == "kahve":
    st.markdown("### ☕ Kahve & Tatlı")
    kart_bas("kahve")

elif s == "beach":
    st.markdown("### 🏖️ Beach & Plajlar")
    kart_bas("beach")

elif s == "kokteyl":
    st.markdown("### 🍸 Kokteyl & Alkol")
    kart_bas("kokteyl")

elif s == "eglence":
    st.markdown("### 🎉 Eğlence")
    kart_bas("eglence")

elif s == "taksi":
    st.markdown("### 🚕 Taksi")
    st.markdown('<div class="venue-card"><h4>Sarımsaklı Taksi</h4><a href="tel:02663961010" style="color:#2c5364; font-weight:bold;">📞 0266 396 10 10</a></div>', unsafe_allow_html=True)

elif s == "eczane":
    st.markdown("### 💊 Eczane")
    st.markdown('<div class="venue-card"><h4>Nöbetçi Eczaneler</h4><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank" style="color:#2c5364; font-weight:bold;">🔍 Listeyi Gör</a></div>', unsafe_allow_html=True)
