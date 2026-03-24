import streamlit as st
import difflib

# --- 1. CONFIG & SETTINGS ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. AYVALIK İŞLETME & BİLGİ BANKASI (AI KÜTÜPHANESİ) ---
# Token tasarrufu sağlayan, fuzzy matching ile çalışan kütüphane
BILGI_BANKASI = {
    # Villa Bilgileri
    "wifi": "📶 **Kablosuz Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "şifre": "📶 **Kablosuz Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "giriş": "🔑 **Giriş Saati:** 14:00  \n🚪 **Çıkış Saati:** 11:00",
    "mangal": "🍢 **Mangal Keyfi:** Bahçede serbesttir. Ekipman hazırdır.",
    "kurallar": "📜 **Ev Kuralları:** 23:00'den sonra sessizlik rica olunur.",
    
    # Kahve
    "kahve": "☕ **Önerdiğimiz Kahve Mekanları:**\n- [Pinos Cafe](https://maps.app.goo.gl/uX38UuUa7o2bL7r4A)\n- [Crow Coffe](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Ivy Ayvalık](https://maps.app.goo.gl/uR8rU8rU8rU8rU8r9)\n- [Daisy Küçükköy](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Nona Cunda](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Cafe Melin](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Declan](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [AIMA](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)",
    
    # Pizza
    "pizza": "🍕 **Önerdiğimiz Pizza Mekanları:**\n- [Pizza Teo](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Uno Cunda](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Tino Ristorante Pizzeria](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Küçük İtalya](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Cunda Luna](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)",
    
    # Yemek
    "yemek": "🍽️ **Önerdiğimiz Restoranlar:**\n- **Ayna Cunda (Ödüllü):** [Konum](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- **L'arancia (Ödüllü):** [Konum](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- **By Nihat (Ödüllü):** [Konum](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Ritüel 1873](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Köşebaşı](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Papaz'ın Evi](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Ayvalık Balıkçısı](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Karina Ayvalık](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)",
    
    # Kokteyl & Alkol
    "kokteyl": "🍸 **Önerdiğimiz Kokteyl & Alkol Mekanları:**\n- [Ritüel 1873 Cunda](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Cunda Luna](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Ciello Cunda](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Vino Şarap Evi](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [De Jong Cocktails](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Cunda Frenk](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Felicita Küçükköy](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Cunda Kaktüs](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)",
    
    # Beach
    "beach": "🏖️ **Önerdiğimiz Beach & Plajlar:**\n\n**💳 Ücretli Beachler:**\n- [Ajlan Eos Beach](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Kesebir Cunda](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Sea Resort Ayvalık](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Sea Long Ayvalık](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Surya Beach](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n\n**🆓 Ücretsiz Plajlar:**\n- [Sarımsaklı Plajları](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Badavut Plajı](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [İğdeli Plajı (Ek Öneri)](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)",
    
    # Eğlence
    "eğlence": "🎉 **Önerdiğimiz Eğlence Mekanları:**\n- [La Fuga](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Kraft](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Afişe Sahne](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [Aksi Pub](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)\n- [The Public House](https://maps.app.goo.gl/3A2aU6a8t9r7X8zB9)",

    # Taksi
    "taksi": "🚕 **Sarımsaklı Taksi:** 0266 396 10 10",
    "eczane": "💊 **Eczane:** En yakın nöbetçi eczane için resepsiyonla iletişime geçebilirsiniz."
}

# --- 3. CSS (DÜZELTİLMİŞ VE PREMIUM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .stApp { background-color: #f4f7f9; font-family: 'Inter', sans-serif; }

    /* 🌟 O MEŞHUR GRADYAN BAŞLIK KARTI */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white !important;
        padding: 35px 20px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
    }
    .main-header h1 { font-weight: 800; font-size: 30px; margin: 0; color: white !important; }
    .main-header p { font-weight: 400; font-size: 15px; opacity: 0.85; color: white !important; margin-top: 10px; }

    /* BUTON GRİDİ */
    div[data-testid="stHorizontalBlock"] { gap: 8px !important; margin-bottom: 10px !important; }

    /* GENİŞ VE DOLGUN BUTONLAR */
    div.stButton > button {
        background: white !important;
        color: #1a2a3a !important;
        border: 1px solid #eee !important;
        border-radius: 18px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
        width: 100% !important;
        height: 100px !important; 
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
        border-color: #2c5364 !important;
    }

    div.stButton > button p {
        font-weight: 700 !important;
        font-size: 15px !important;
        margin: 0 !important;
        line-height: 1.2 !important;
    }

    /* İÇERİK KUTUSU */
    .content-box {
        background: white;
        padding: 25px;
        border-radius: 20px;
        border-left: 5px solid #2c5364;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        margin-bottom: 15px;
    }
    .content-box h3 { margin-top: 0; color: #2c5364; }
    .content-box a { color: #2c5364; text-decoration: none; font-weight: 600; }
    .content-box a:hover { text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Konaklama & Keşif Rehberi</p></div>', unsafe_allow_html=True)

# --- 5. 4x2 GRİD (TOPLAM 8 MENÜ) ---
# Satır 1
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🤖\nAsistan", key="m1"): st.session_state.secili_sayfa = "asistan"; st.rerun()
with c2:
    if st.button("🍽️\nYemek", key="m2"): st.session_state.secili_sayfa = "yemek"; st.rerun()
with c3:
    if st.button("☕\nKahve", key="m3"): st.session_state.secili_sayfa = "kahve"; st.rerun()
with c4:
    if st.button("🏖️\nBeach", key="m4"): st.session_state.secili_sayfa = "beach"; st.rerun()

# Satır 2
c5, c6, c7, c8 = st.columns(4)
with c5:
    if st.button("🍸\nKokteyl", key="m5"): st.session_state.secili_sayfa = "kokteyl"; st.rerun()
with c6:
    if st.button("🎉\nEğlence", key="m6"): st.session_state.secili_sayfa = "eğlence"; st.rerun()
with c7:
    if st.button("🚕\nTaksi", key="m7"): st.session_state.secili_sayfa = "taksi"; st.rerun()
with c8:
    if st.button("📜\nKurallar",
