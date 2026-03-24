import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. VERİ YAPISI (Kartlar için Liste Formatına Geçtik) ---
MEKAN_VERISI = {
    "yemek": [
        {"ad": "Ayna Cunda", "ozellik": "🏅 Ödüllü Restoran", "link": "https://maps.app.goo.gl/Ayna"},
        {"ad": "L'arancia", "ozellik": "🏅 Ödüllü Restoran", "link": "https://maps.app.goo.gl/Larancia"},
        {"ad": "By Nihat", "ozellik": "🏅 Ödüllü Restoran", "link": "https://maps.app.goo.gl/ByNihat"},
        {"ad": "Ritüel 1873", "ozellik": "Ege Mutfağı", "link": "https://maps.app.goo.gl/Rituel"},
        {"ad": "Köşebaşı", "ozellik": "Kebap & Et", "link": "https://maps.app.goo.gl/Kosebasi"},
        {"ad": "Papaz'ın Evi", "ozellik": "Tarihi Atmosfer", "link": "https://maps.app.goo.gl/Papaz"},
        {"ad": "Ayvalık Balıkçısı", "ozellik": "Taze Deniz Ürünleri", "link": "https://maps.app.goo.gl/Balikci"},
        {"ad": "Karina Ayvalık", "ozellik": "Sahil Restoranı", "link": "https://maps.app.goo.gl/Karina"}
    ],
    "pizza": [
        {"ad": "Pizza Teo", "ozellik": "Odun Ateşi", "link": "https://maps.app.goo.gl/Teo"},
        {"ad": "Uno Cunda", "ozellik": "İtalyan Esintisi", "link": "https://maps.app.goo.gl/Uno"},
        {"ad": "Tino Ristorante", "ozellik": "Gurme Pizza", "link": "https://maps.app.goo.gl/Tino"},
        {"ad": "Küçük İtalya", "ozellik": "Napoliten", "link": "https://maps.app.goo.gl/Italya"},
        {"ad": "Cunda Luna", "ozellik": "Keyifli Bahçe", "link": "https://maps.app.goo.gl/Luna"}
    ],
    "kahve": [
        {"ad": "Pinos Cafe", "ozellik": "Butik Kahve", "link": "#"},
        {"ad": "Crow Coffee", "ozellik": "3. Nesil Kahve", "link": "#"},
        {"ad": "Ivy Ayvalık", "ozellik": "Bahçeli Mekan", "link": "#"},
        {"ad": "Daisy Küçükköy", "ozellik": "Sanatla İç İçe", "link": "#"}
    ],
    "beach": [
        {"ad": "Ajlan Eos Beach", "ozellik": "💎 Ücretli / Premium", "link": "#"},
        {"ad": "Kesebir Cunda", "ozellik": "💎 Ücretli / Aile", "link": "#"},
        {"ad": "Sarımsaklı Plajı", "ozellik": "🆓 Ücretsiz / Halk", "link": "#"},
        {"ad": "Badavut Plajı", "ozellik": "🆓 Ücretsiz / Sakin", "link": "#"}
    ]
}

# --- 3. CSS (KART TASARIMI) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
    
    /* Üst Başlık */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }

    /* İşletme Kartı */
    .venue-card {
        background: white;
        padding: 18px;
        border-radius: 15px;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        border: 1px solid #edf2f7;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: 0.3s;
    }
    .venue-card:hover { transform: translateY(-2px); box-shadow: 0 8px 15px rgba(0,0,0,0.05); }
    
    .venue-info h4 { margin: 0; color: #1a202c; font-size: 18px; }
    .venue-info p { margin: 4px 0 0 0; color: #718096; font-size: 14px; }
    
    .venue-link a {
        background: #2c5364;
        color: white !important;
        padding: 8px 16px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 600;
        font-size: 13px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. DASHBOARD (BUTONLAR) ---
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Dashboard</h1><p>Premium Misafir Deneyimi</p></div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🤖\nAsistan"): st.session_state.secili_sayfa = "asistan"; st.rerun()
with c2:
    if st.button("🍽️\nYemek"): st.session_state.secili_sayfa = "yemek"; st.rerun()
with c3:
    if st.button("☕\nKahve"): st.session_state.secili_sayfa = "kahve"; st.rerun()
with c4:
    if st.button("🏖️\nBeach"): st.session_state.secili_sayfa = "beach"; st.rerun()

st.divider()

# --- 5. KARTLI İÇERİK MOTORU ---
s = st.session_state.secili_sayfa

def kart_olustur(kategori_adi):
    if kategori_adi in MEKAN_VERISI:
        for mekan in MEKAN_VERISI[kategori_adi]:
            st.markdown(f"""
                <div class="venue-card">
                    <div class="venue-info">
                        <h4>{mekan['ad']}</h4>
                        <p>{mekan['ozellik']}</p>
                    </div>
                    <div class="venue-link">
                        <a href="{mekan['link']}" target="_blank">📍 Konum</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

if s == "asistan":
    st.subheader("🤖 Akıllı Asistan")
    p = st.chat_input("Nerede yemek yiyebilirim?")
    if p:
        st.info("🤖 Aradığınız konuyu butonlardan veya aşağıdaki rehberden inceleyebilirsiniz.")

elif s == "yemek":
    st.markdown("### 🍽️ Restoranlar")
    kart_olustur("yemek")
    st.markdown("---")
    st.markdown("### 🍕 Pizza Önerileri")
    kart_olustur("pizza")

elif s == "kahve":
    st.markdown("### ☕ Kahve & Tatlı")
    kart_olustur("kahve")

elif s == "beach":
    st.markdown("### 🏖️ Plaj & Beachler")
    kart_olustur("beach")
