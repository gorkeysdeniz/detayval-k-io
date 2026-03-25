import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. CSS (BUTONLARI ÜST ÜSTE BİNDİREN VE YANA KAYMAYI BİTİREN KOD) ---
st.markdown("""
    <style>
    /* 1. Tüm sayfa taşmalarını engelle */
    .block-container { padding: 1rem 0.5rem !important; max-width: 100% !important; }
    html, body, [data-testid="stAppViewContainer"] { overflow-x: hidden !important; }

    /* 2. O ÇİRKİN "btn_1" YAZILARINI TAMAMEN GİZLE */
    div[data-testid="stVerticalBlock"] > div:has(button) {
        display: none !important;
    }
    
    /* 3. PINTEREST GRID TASARIMI */
    .p-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
        width: 100%;
        margin-bottom: 15px;
    }

    .p-btn {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        height: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.1s;
    }
    .p-btn:active { transform: scale(0.95); background: #f1f5f9; }
    .p-icon { font-size: 26px; margin-bottom: 2px; pointer-events: none; }
    .p-text { font-size: 13px; font-weight: 700; color: #1e293b; pointer-events: none; }

    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;
    }
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. GİZLİ TETİKLEYİCİLER (Ekranda asla yer kaplamazlar) ---
# Sadece butonlara tıklandığında Python tarafını güncellemek için varlar.
with st.container():
    if st.button("btn_asistan"): st.session_state.secili_sayfa = "asistan"
    if st.button("btn_yemek"): st.session_state.secili_sayfa = "yemek"
    if st.button("btn_pizza"): st.session_state.secili_sayfa = "pizza"
    if st.button("btn_kahve"): st.session_state.secili_sayfa = "kahve"
    if st.button("btn_beach"): st.session_state.secili_sayfa = "beach"
    if st.button("btn_kokteyl"): st.session_state.secili_sayfa = "kokteyl"
    if st.button("btn_eglence"): st.session_state.secili_sayfa = "eglence"
    if st.button("btn_taksi"): st.session_state.secili_sayfa = "taksi"
    if st.button("btn_eczane"): st.session_state.secili_sayfa = "eczane"

# --- 4. GÖRÜNEN ŞIK PANEL ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# JavaScript ile butonlara isimle değil, CSS içeriğiyle ulaşıyoruz (en garantisi bu)
def trigger(name):
    return f"""document.querySelectorAll('button p').forEach(p => {{ if(p.innerText == '{name}') p.click(); }})"""

st.markdown(f"""
    <div class="p-grid">
        <div class="p-btn" onclick="{trigger('btn_asistan')}"><div class="p-icon">🤖</div><div class="p-text">Asistan</div></div>
        <div class="p-btn" onclick="{trigger('btn_yemek')}"><div class="p-icon">🍽️</div><div class="p-text">Yemek</div></div>
        <div class="p-btn" onclick="{trigger('btn_pizza')}"><div class="p-icon">🍕</div><div class="p-text">Pizza</div></div>
        <div class="p-btn" onclick="{trigger('btn_kahve')}"><div class="p-icon">☕</div><div class="p-text">Kahve</div></div>
        <div class="p-btn" onclick="{trigger('btn_beach')}"><div class="p-icon">🏖️</div><div class="p-text">Beach</div></div>
        <div class="p-btn" onclick="{trigger('btn_kokteyl')}"><div class="p-icon">🍸</div><div class="p-text">Kokteyl</div></div>
        <div class="p-btn" onclick="{trigger('btn_eglence')}"><div class="p-icon">🎉</div><div class="p-text">Eğlence</div></div>
        <div class="p-btn" onclick="{trigger('btn_taksi')}"><div class="p-icon">🚕</div><div class="p-text">Taksi</div></div>
        <div class="p-btn" onclick="{trigger('btn_eczane')}"><div class="p-icon">💊</div><div class="p-text">Eczane</div></div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 5. İÇERİK (DOKUNULMADI) ---
MEKAN_VERISI = {
    "kahve": [{"ad": "Pinos Cafe", "oz": "Butik Kahve", "ln": "http://google.com/1"}, {"ad": "Crow Coffe", "oz": "3. Nesil Kahve", "ln": "http://google.com/2"}],
    "pizza": [{"ad": "Pizza Teo", "oz": "Odun Ateşi", "ln": "http://google.com/9"}, {"ad": "Uno Cunda", "oz": "İtalyan Klasiği", "ln": "http://google.com/10"}],
    "yemek": [{"ad": "Ayna Cunda", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/14"}, {"ad": "L'arancia", "oz": "🏅 Michelin Rehberi", "ln": "http://google.com/15"}],
    "kokteyl": [{"ad": "Ritüel 1873 Cunda", "oz": "İmza Kokteyller", "ln": "http://google.com/17"}],
    "beach": [{"ad": "Ajlan Eos Beach", "oz": "💎 Ücretli Beach", "ln": "http://google.com/28"}],
    "eglence": [{"ad": "La Fuga", "oz": "Müzik & Dans", "ln": "http://google.com/34"}]
}

def kart_bas(key):
    if key in MEKAN_VERISI:
        for m in MEKAN_VERISI[key]:
            st.markdown(f'<div class="venue-card"><div><h4 style="margin:0; font-size:14px;">{m["ad"]}</h4><p style="margin:0; font-size:11px; color:#666;">{m["oz"]}</p></div><div class="venue-link"><a href="{m["ln"]}" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-size:10px; font-weight:bold;">📍 KONUM</a></div></div>', unsafe_allow_html=True)

# --- 6. SAYFA MANTIĞI ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    u_in = st.chat_input("Pizza, Kahve, Plaj...")
    if u_in:
        # Chat kodların buraya gelecek
        pass
elif s == "taksi":
    st.markdown('<div class="venue-card"><h4>🚕 Sarımsaklı Taksi</h4><a href="tel:02663961010" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">📞 ARA</a></div>', unsafe_allow_html=True)
elif s == "eczane":
    st.markdown('<div class="venue-card"><h4>💊 Nöbetçi Eczaneler</h4><a href="https://www.aeo.org.tr/NobetciEczaneler" target="_blank" style="background:#2c5364; color:white; padding:8px 12px; border-radius:8px; text-decoration:none; font-weight:bold;">🔍 GÖR</a></div>', unsafe_allow_html=True)
else:
    st.markdown(f"##### ✨ {s.capitalize()} Önerileri")
    kart_bas(s)
