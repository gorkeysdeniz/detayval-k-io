import streamlit as st
from datetime import datetime, timedelta
import random

# --- 1. AYARLAR & TASARIM ---
st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

st.markdown("""
    <style>
    .main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab"] { height: 70px; font-size: 18px !important; font-weight: bold; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# --- 2. VERİ TABANI (Buraya İstediğin Zaman Ekleme Yapabilirsin) ---
VERI_TABANI = {
    "tost": {
        "etiketler": ["tost", "tostçu", "acıktım", "kahvaltı", "tostuyevski"],
        "cevap": "Dostum Ayvalık'ta tost denince akla gelen ilk yer **Tostuyevski**! Ayrıca **Aşkın Tost Evi** ve **Tadım Tost Evi** de efsanedir. Afiyet olsun!"
    },
    "cafe": {
        "etiketler": ["cafe", "kahve", "tatlı", "kafe", "coffee", "çay"],
        "cevap": "Keyifli bir mola için seçeneklerin çok! \n\n• **Pinos Cafe:** Sarımsaklı'da, villaya çok yakındır. \n• **Nona Cunda:** Tatlı ve kahve keyfi için ideal. \n• **Crew Coffee:** Cunda'da yeni nesil kahve noktası. \n• **Kaktüs Cunda:** Benim favori mekanım!"
    },
    "pizza": {
        "etiketler": ["pizza", "pizzacı", "italyan", "makarna", "piza"],
        "cevap": "İtalyan esintisi arıyorsan şunlar nokta atışıdır: \n\n• **Cunda Uno:** Klasikleşmiş, mutlaka gitmelisin. \n• **Küçük İtalya (Küçükköy):** Atmosferi harikadır. \n• **Pizza Teos** ve **Tino Pizza Ristorante** de diğer güçlü seçenekler."
    },
    "kokteyl": {
        "etiketler": ["kokteyl", "alkol", "gece", "bar", "eğlence", "içki", "müzik"],
        "cevap": "Cunda'nın akşamları bir başkadır dostum: \n\n• **Ciello Cunda:** Şık ve lezzetli kokteyller. \n• **Luna Cunda:** Geceyi bitirmek için birebir. \n• **Rituel 1873:** Tarihi dokuda müzik keyfi."
    },
    "plaj": {
        "etiketler": ["plaj", "deniz", "beach", "yüzme", "kum", "güneş"],
        "cevap": "**Ücretsiz Plajlar:** Badavut (Benim favorim!), Sarımsaklı ve Ortunç Koyu. \n\n**Ücretli Beachler:** Ayvalık Sea Long, Ajlan, Kesebir ve Scala Beach."
    },
    "villa": {
        "etiketler": ["villa", "oda", "yatak", "kapasite", "ev", "kaç kişi"],
        "cevap": "Villamız 3 oda, 5-6 yatak ve 2 çekyat kapasitesine sahip. Rahat rahat yayılabilirsiniz dostum!"
    }
}

ETKINLIKLER = [
    {"tarih": "2026-03-24", "sanatci": "Teoman"},
    {"tarih": "2026-03-27", "sanatci": "Pinhani"}
]

# --- 3. AKILLI CEVAP MOTORU (HIZLI & KOTA DOSTU) ---
def asistan_cevap_ver(soru):
    soru = soru.lower()
    
    # Kelime kelime kontrol et (Yazım hataları toleransı için)
    for anahtar, icerik in VERI_TABANI.items():
        for etiket in icerik["etiketler"]:
            if etiket in soru:
                return icerik["cevap"]
    
    # Hiçbir şey bulamazsa samimi bir yönlendirme yap
    return "Dostum bunu henüz bilmiyorum ama istersen bizi arayabilirsin veya 'plaj', 'pizza', 'kahve' gibi anahtar kelimelerle tekrar sorabilirsin! 😊"

# --- 4. SEKMELER ---
t_rehber, t_ai, t_etkinlik, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "🎉 Etkinlik", "💊 Eczane"])

with t_rehber:
    st.info("💡 **Günün Tavsiyesi:** Badavut'ta gün batımını izlemeden dönme!")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Ayvalık hakkında ne bilmek istersin? (Örn: Pizza, Plaj, Kahve...)"}]
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("Sor bakalım..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # Saniyeler içinde yerel cevap üretilir
        cevap = asistan_cevap_ver(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(cevap)
        st.session_state.messages.append({"role": "assistant", "content": cevap})

with t_etkinlik:
    st.subheader("📅 Yaklaşan Konserler")
    bugun = datetime.now()
    on_gun = bugun + timedelta(days=10)
    for k in ETKINLIKLER:
        kt = datetime.strptime(k["tarih"], "%Y-%m-%d")
        if bugun <= kt <= on_gun:
            st.success(f"🎤 {k['sanatci']} - {kt.strftime('%d.%m.%Y')}")

with t_eczane:
    st.link_button("💊 Nöbetçi Eczane Listesi", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
