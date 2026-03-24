import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

# Session State başlatma (Hata almamak için)
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. TÜM VERİ SETİ ---
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "https://maps.app.goo.gl/Ayvalik1"},
        {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "https://maps.app.goo.gl/Ayvalik2"},
        {"ad": "Ivy Ayvalık", "oz": "Huzurlu Bahçe", "ln": "https://maps.app.goo.gl/Ayvalik3"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "https://maps.app.goo.gl/Ayvalik4"},
        {"ad": "Nona Cunda", "oz": "Cunda Esintisi", "ln": "https://maps.app.goo.gl/Ayvalik5"},
        {"ad": "Cafe Melin", "oz": "Keyifli Durak", "ln": "https://maps.app.goo.gl/Ayvalik6"},
        {"ad": "Declan", "oz": "Modern Coffee", "ln": "https://maps.app.goo.gl/Ayvalik7"},
        {"ad": "AIMA", "oz": "Akademik Lezzet", "ln": "https://maps.app.goo.gl/Ayvalik8"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "https://maps.app.goo.gl/Ayvalik9"},
        {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "https://maps.app.goo.gl/Ayvalik10"},
        {"ad": "Tino Ristorante", "oz": "Pizzeria", "ln": "https://maps.app.goo.gl/Ayvalik11"},
        {"ad": "Küçük İtalya", "oz": "Napoliten", "ln": "https://maps.app.goo.gl/Ayvalik12"},
        {"ad": "Cunda Luna", "oz": "Bahçe & Pizza", "ln": "https://maps.app.goo.gl/Ayvalik13"}
    ],
    "yemek": [
        {"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi / Ödüllü", "ln": "https://maps.app.goo.gl/Ayvalik14"},
        {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi / Ödüllü", "ln": "https://maps.app.goo.gl/Ayvalik15"},
        {"ad": "By Nihat", "oz": "🏅 Efsanevi Balıkçı / Ödüllü", "ln": "https://maps.app.goo.gl/Ayvalik16"},
        {"ad": "Ritüel 1873", "oz": "Modern Ege Mutfağı", "ln": "https://maps.app.goo.gl/Ayvalik17"},
        {"ad": "Köşebaşı", "oz": "Kebap & Ocakbaşı", "ln": "https://maps.app.goo.gl/Ayvalik18"},
        {"ad": "Papaz'ın Evi", "oz": "Tarihi Doku", "ln": "https://maps.app.goo.gl/Ayvalik19"},
        {"ad": "Ayvalık Balıkçısı", "oz": "Taze Lezzetler", "ln": "https://maps.app.goo.gl/Ayvalik20"},
        {"ad": "Karina Ayvalık", "oz": "Deniz Kenarı", "ln": "https://maps.app.goo.gl/Ayvalik21"}
    ],
    "kokteyl": [
        {"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "https://maps.app.goo.gl/Ayvalik22"},
        {"ad": "Cunda Luna", "oz": "Alkol & Müzik", "ln": "https://maps.app.goo.gl/Ayvalik23"},
        {"ad": "Ciello Cunda", "oz": "Roof Bar", "ln": "https://maps.app.goo.gl/Ayvalik24"},
        {"ad": "Vino Şarap Evi", "oz": "Şarap & Meze", "ln": "https://maps.app.goo.gl/Ayvalik25"},
        {"ad": "De Jong Cocktails", "oz": "Craft Cocktails", "ln": "https://maps.app.goo.gl/Ayvalik26"},
        {"ad": "Cunda Frenk", "oz": "Trend Mekan", "ln": "https://maps.app.goo.gl/Ayvalik27"},
        {"ad": "Felicita Küçükköy", "oz": "Bohem Atmosfer", "ln": "https://maps.app.goo.gl/Ayvalik28"},
        {"ad": "Cunda Kaktüs", "oz": "Gece Eğlencesi", "ln": "https://maps.app.goo.gl/Ayvalik29"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/Ayvalik30"},
        {"ad": "Kesebir Cunda", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/Ayvalik31"},
        {"ad": "Sea Resort / Long", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/Ayvalik32"},
        {"ad": "Surya Beach", "oz": "💎 Ücretli Beach", "ln": "https://maps.app.goo.gl/Ayvalik33"},
        {"ad": "Sarımsaklı Plajları", "oz": "🆓 Ücretsiz / Geniş Sahil", "ln": "https://maps.app.goo.gl/Ayvalik34"},
        {"ad": "Badavut Plajı", "oz": "🆓 Ücretsiz / Doğa Harikası", "ln": "https://maps.app.goo.gl/Ayvalik35"}
    ],
    "eglence": [
        {"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "https://maps.app.goo.gl/Ayvalik36"},
        {"ad": "Kraft", "oz": "Craft Beer & Mood", "ln": "https://maps.app.goo.gl/Ayvalik37"},
        {"ad": "Afişe Sahne", "oz": "Canlı Performans", "ln": "https://maps.app.goo.gl/Ayvalik38"},
        {"ad": "Aksi Pub", "oz": "Pub Kültürü", "ln": "https://maps.app.goo.gl/Ayvalik39"},
        {"ad": "The Public House", "oz": "Şehir Kulübü", "ln": "https://maps.app.goo.gl/Ayvalik40"}
    ],
    "villa": [
        {"ad": "Wi-Fi Bilgisi", "oz": "Ağ: Detayvalik_Villa | Şifre: ayvalik2026", "ln": "#"},
        {"ad": "Giriş/Çıkış", "oz": "Giriş: 14:00 - Çıkış: 11:00", "ln": "#"}
    ]
}

# --- 3. CSS (4x2 DÜZEN VE KARTLAR) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }
    
    /* Butonların yan yana düzgün durması için */
    div.stButton > button {
        background: white !important; color: #1a202c !important;
        border: 1px solid #e2e8f0 !important; border-radius: 12px !important;
        width: 100% !important; height: 90px !important; font-weight: 700 !important;
        font-size: 14px !important; transition: 0.3s;
    }
    div.stButton > button:hover { border-color: #2c5364 !important; transform: translateY(-2px); }

    /* Kart Tasarımı */
    .venue-card {
        background: white; padding: 15px; border-radius: 15px;
        margin-bottom: 10px; border: 1px solid #e2e8f0;
        display: flex; justify-content: space-between; align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .venue-info h4 { margin: 0; color: #1a202c; font-size: 16px; }
    .venue-info p { margin: 3px 0 0 0; color: #64748b; font-size: 12px; }
    .venue-link a {
        background: #2c5364; color: white !important;
        padding: 6px 12px; border-radius: 8px; text-decoration: none;
        font-size: 11px; font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. DASHBOARD (ÜST PANEL) ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Misafir Rehberi</p></div>', unsafe_allow_html=True)

# 4 ÜST - 4 ALT DÜZENİ
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🤖\nAsistan"): st.session_state.secili_sayfa = "asistan"; st.rerun()
with col2:
    if st.button("🍽️\nYemek"): st.session_state.secili_sayfa = "yemek"; st.rerun()
with col3:
    if st.button("☕\nKahve"): st.session_state.secili_sayfa = "kahve"; st.rerun()
with col4:
    if st.button("🏖️\nBeach"): st.session_state.secili_sayfa = "beach"; st.rerun()

col5, col6, col7, col8 = st.columns(4)
with col5:
    if st.button("🍸\nKokteyl"): st.session_state.secili_sayfa = "kokteyl"; st.rerun()
with col6:
    if st.button("🎉\nEğlence"): st.session_state.secili_sayfa = "eglence"; st.rerun()
with col7:
    if st.button("🚕\nTaksi"): st.session_state.secili_sayfa = "taksi"; st.rerun()
with col8:
    if st.button("💊\nEczane"): st.session_state.secili_sayfa = "eczane"; st.rerun()

st.divider()

# --- 5. FONKSİYONLAR ---
def kart_bas(anahtar):
    if anahtar in MEKAN_VERISI:
        for m in MEKAN_VERISI[anahtar]:
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
    soru = st.chat_input("Örn: Pizza nerede yenir?")
    
    if soru:
        with st.chat_message("user"): st.write(soru)
        cevap_bulundu = False
        soru_low = soru.lower()
        
        # Akıllı Arama Mantığı (Kütüphaneyi Tarar)
        for kat, liste in MEKAN_VERISI.items():
            if kat in soru_low:
                with st.chat_message("assistant"):
                    st.write(f"Sizin için **{kat.upper()}** kategorisindeki mekanları buldum:")
                    kart_bas(kat)
                cevap_bulundu = True
                break
        
        if not cevap_bulundu:
            with st.chat_message("assistant"):
                st.write("🤖 Bu konuda henüz spesifik bir mekan kaydetmedim ama yukarıdaki menülerden tüm listemize ulaşabilirsiniz!")

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
    st.markdown("### 🎉 Eğlence & Publar")
    kart_bas("eglence")

elif s == "taksi":
    st.markdown("### 🚕 Taksi Çağır")
    st.markdown('<div class="venue-card"><h4>Sarımsaklı Taksi</h4><a href="tel:02663961010" style="color:#2c5364; font-weight:bold;">📞 0266 396 10 10</a></div>', unsafe_allow_html=True)

elif s == "eczane":
    st.markdown("### 💊 Nöbetçi Eczaneler")
    st.markdown('<div class="venue-card"><p>Güncel liste için tıklayın:</p><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 Eczaneleri Gör</a></div>', unsafe_allow_html=True)
