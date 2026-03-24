import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

# URL parametrelerini kontrol et (Buton tıklamalarını yakalamak için)
query_params = st.query_params
if "p" in query_params:
    st.session_state.secili_sayfa = query_params["p"]

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. VERİ SETİ ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}]
}

# --- 3. CSS (MOBİLİ ZORLAYAN TEK SATIR GRID) ---
st.markdown("""
    <style>
    /* Sayfa boşluklarını öldür */
    .block-container { padding: 1rem 0.4rem !important; }
    
    /* ASIL ÇÖZÜM: HTML GRID */
    .custom-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr); /* Kesinlikle 4 kolon */
        gap: 6px;
        margin-bottom: 15px;
    }
    
    .nav-btn {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 8px 2px;
        text-decoration: none;
        color: #1e293b;
        font-size: 10px;
        font-weight: 700;
        height: 65px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .nav-btn:active { background: #f1f5f9; transform: scale(0.95); }
    .emoji { font-size: 18px; margin-bottom: 4px; }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;
    }
    
    /* İşletme Kartları */
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;
    }
    .venue-link a {
        background: #2c5364; color: white !important; padding: 6px 10px; 
        border-radius: 6px; text-decoration: none; font-size: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Premium Misafir Dashboard</p></div>', unsafe_allow_html=True)

# HTML İLE 4'LÜ GRİD (Streamlit'ten bağımsız çalışır, mobilde alt alta binmez)
st.markdown(f"""
    <div class="custom-grid">
        <a href="?p=asistan" class="nav-btn" target="_self"><span class="emoji">🤖</span>Asistan</a>
        <a href="?p=yemek" class="nav-btn" target="_self"><span class="emoji">🍽️</span>Yemek</a>
        <a href="?p=kahve" class="nav-btn" target="_self"><span class="emoji">☕</span>Kahve</a>
        <a href="?p=beach" class="nav-btn" target="_self"><span class="emoji">🏖️</span>Beach</a>
        <a href="?p=kokteyl" class="nav-btn" target="_self"><span class="emoji">🍸</span>Kokteyl</a>
        <a href="?p=eglence" class="nav-btn" target="_self"><span class="emoji">🎉</span>Eğlence</a>
        <a href="?p=taksi" class="nav-btn" target="_self"><span class="emoji">🚕</span>Taksi</a>
        <a href="?p=eczane" class="nav-btn" target="_self"><span class="emoji">💊</span>Eczane</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 5. İÇERİK MANTIĞI ---
def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div><h4>{m["ad"]}</h4><p>{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank">📍 KONUM</a></div></div>', unsafe_allow_html=True)

s = st.session_state.secili_sayfa

if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    u_in = st.chat_input("Mesajınızı yazın...")
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
elif s == "kahve":
    st.markdown("##### ☕ Kahve & Tatlı")
    kart_bas("kahve")
elif s == "beach":
    st.markdown("##### 🏖️ Beach & Plaj")
    kart_bas("beach")
elif s == "kokteyl":
    st.markdown("##### 🍸 Kokteyl & Bar")
    kart_bas("kokteyl")
elif s == "eglence":
    st.markdown("##### 🎉 Eğlence")
    kart_bas("eglence")
elif s == "taksi":
    st.markdown("##### 🚕 Taksi")
    st.markdown('<div class="venue-card"><h4>Sarımsaklı Taksi</h4><div class="venue-link"><a href="tel:02663961010">📞 ARA</a></div></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown("##### 💊 Eczane")
    st.markdown('<div class="venue-card"><h4>Nöbetçi Eczaneler</h4><div class="venue-link"><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank">🔍 GÖR</a></div></div>', unsafe_allow_html=True)
