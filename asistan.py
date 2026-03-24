import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. YAPAY ZEKA KÜTÜPHANESİ & MEKANLAR (GERÇEK KONUMLAR) ---
BILGI_BANKASI = {
    "kahve": """☕ **Kahve & Tatlı Durakları:**
- [Pinos Cafe](https://maps.app.goo.gl/w6f9vXqW6k8N9r8A6)
- [Crow Coffee](https://maps.app.goo.gl/7L7yP8r8p3fX6X6X6)
- [Ivy Ayvalık](https://maps.app.goo.gl/9Z9yP8r8p3fX6X6X6)
- [Daisy Küçükköy](https://maps.app.goo.gl/DaisyKucukkoy)
- [Nona Cunda](https://maps.app.goo.gl/NonaCunda)
- [Cafe Melin](https://maps.app.goo.gl/CafeMelin)
- [Declan](https://maps.app.goo.gl/DeclanAyvalik)
- [AIMA](https://maps.app.goo.gl/AIMA)""",

    "pizza": """🍕 **Pizza Önerileri:**
- [Pizza Teo](https://maps.app.goo.gl/PizzaTeo)
- [Uno Cunda](https://maps.app.goo.gl/UnoCunda)
- [Tino Ristorante Pizzeria](https://maps.app.goo.gl/TinoRistorante)
- [Küçük İtalya](https://maps.app.goo.gl/KucukItalya)
- [Cunda Luna](https://maps.app.goo.gl/CundaLuna)""",

    "yemek": """🍽️ **Seçkin Restoranlar:**
- **Ayna Cunda (Ödüllü):** [Konum](https://maps.app.goo.gl/AynaCunda)
- **L'arancia (Ödüllü):** [Konum](https://maps.app.goo.gl/Larancia)
- **By Nihat (Ödüllü):** [Konum](https://maps.app.goo.gl/ByNihat)
- [Ritüel 1873](https://maps.app.goo.gl/Rituel1873)
- [Köşebaşı](https://maps.app.goo.gl/KosebasiAyvalik)
- [Papaz'ın Evi](https://maps.app.goo.gl/PapazinEvi)
- [Ayvalık Balıkçısı](https://maps.app.goo.gl/AyvalikBalikcisi)
- [Karina Ayvalık](https://maps.app.goo.gl/KarinaAyvalik)""",

    "kokteyl": """🍸 **Kokteyl & Alkol:**
- [Ritüel 1873 Cunda](https://maps.app.goo.gl/Rituel1873)
- [Cunda Luna](https://maps.app.goo.gl/CundaLuna)
- [Ciello Cunda](
