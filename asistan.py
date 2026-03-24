import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

# --- 2. DURUM TAKİBİ ---
if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 3. BİLGİ BANKASI (Token Harcatmayan Bölüm) ---
BILGI_BANKASI = {
    "wifi": "📶 **Kablosuz Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "şifre": "📶 **Kablosuz Ağ:** Detayvalik_Villa  \n🔑 **Şifre:** `ayvalik2026`",
    "giriş": "🔑 **Giriş Saati:** 14:00  \n🚪 **Çıkış Saati:** 11:00",
    "mangal": "🍢 **Mangal Keyfi:** Bahçede mangal ekipmanımız hazırdır. Lütfen kullanımdan sonra söndüğünden emin olun.",
    "plaj": "🏖️ **Deniz & Plaj:** Sarımsaklı plajı yürüyerek sadece 5 dakika mesafededir.",
    "taksi": "🚕 **Ulaşım:** Sarımsaklı Taksi: 0266 396 10 10",
    "kurallar": "📜 **Ev Düzeni:** Komşularımızı rahatsız etmemek adına 23:00'den sonra müzik sesini kısmanızı rica ederiz."
}

# --- 4. CSS (PREMİUM TASARIM) ---
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
    .main-header h1 { font-
