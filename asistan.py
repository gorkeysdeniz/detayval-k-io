import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "🤖 Asistan"

# --- 2. CSS (BÜYÜK MENÜLER VE TEMİZ SOHBET DÜZENİ) ---
st.markdown("""
    <style>
    /* Menü butonlarını (Pills) devleştiriyoruz */
    .stPills [data-testid="stBaseButton-secondaryPill"] {
        padding: 15px 25px !important;
        font-size: 16px !important;
        border-radius: 30px !important;
        border: 1px solid #2c5364 !important;
    }
    
    .header-container {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 20px;
    }
    
    .venue-card {
        background: white; padding: 15px; border-radius: 15px; margin-bottom: 10px;
        border: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .venue-info h4 { margin: 0; font-size: 16px; color: #1e293b; }
    .venue-info p { margin: 2px 0 0 0; font-size: 13px; color: #64748b; }
    .venue-link a {
        background: #2c5364; color: white; padding: 10px 18px; border-radius: 10px;
        text-decoration: none; font-size: 12px; font-weight: bold;
    }
    
    /* ASİSTAN SOHBET KUTUSU (Menüden Ayrı) */
    .chat-box {
        background-color: #f8fafc;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        border: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TAM MEKAN VERİSİ (EĞLENCE & KOKTEYL GERİ GELDİ + GERÇEK KONUMLAR) ---
MEKAN_VERISI = {
    "kahve": [
        {"ad": "Pino's Coffee & Cakes", "oz": "Butik Kahve & Tatlı", "ln": "https://www.google.com/maps/search/?api=1&query=Pino's+Coffee+Ayvalik"},
        {"ad": "Crow Coffee Roastery", "oz": "3. Nesil Kavurma", "ln": "https://www.google.com/maps/search/?api=1&query=Crow+Coffee+Roastery+Ayvalik"},
        {"ad": "Ivy Ayvalik Coffee", "oz": "Huzurlu Bahçe", "ln": "https://www.google.com/maps/search/?api=1&query=Ivy+Ayvalik+Coffee"},
        {"ad": "Daisy Küçükköy", "oz": "Sanat & Kahve", "ln": "
