import streamlit as st
import google.generativeai as genai
import random

# --- 1. YAPILANDIRMA ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        if "model" not in st.session_state:
            st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. CSS: AKILLI KATMAN VE 2x2 DÜZEN ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 30px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px; position: relative;
    }
    
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    /* 2x2 Izgara */
    .menu-grid {
        display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: -135px; /* Butonların üstüne binmesi için */
    }
    
    .menu-card {
        background: white; padding: 20px 10px; border-radius: 15px; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #eee;
        height: 120px; pointer-events: none; /* Tıklamayı arkadaki butona geçir */
    }
    
    .menu-icon { font-size: 30px; display: block; margin-bottom: 5px; }
    .menu-title { font-weight: 700; color: #2c3e50; font-size: 14px; display: block; }
    .menu-sub { font-size: 9px; color: #95a5a6; display: block; }

    /* Görünmez Butonları Kartların Üzerine Yay */
    .stButton > button {
        height: 120px !important; background: transparent !important;
        color: transparent !important; border: none !important;
        width: 100% !important; box-shadow: none !important;
    }
    .stButton > button:active { background: rgba(0,0,0,0.05) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE (Sekme Takibi) ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "rehber"

# --- 4. YANIT MOTORU ---
BILGI_BANKASI = {
    "yemek": {"anahtarlar": ["yemek", "restoran", "pizza"], "cevap": "🍕 **Pizza:** Cunda Uno.\n🥪 **Tost:** Tostuyevski."},
    "tost": {"anahtarlar": ["tost", "tostçu"], "cevap": "Ayvalık'ta tost denince **Tostuyevski**!"},
    "plaj": {"anahtarlar": ["plaj", "deniz"], "cevap": "🏖️ **Öneri:** Badavut veya Ortunç Koyu."},
}

def yanıt_uret(soru):
    soru_low = soru.lower()
    for kategori, icerik in BILGI_BANKASI.items():
        if any(anahtar in soru_low for anahtar in icerik["anahtarlar"]): return icerik["cevap"]
    try:
        sys_msg = "Sen Detayvalık Villa asistanısın. Kısa cevap ver."
        response = st.session_state.model.generate_content(f"{sys_msg}\n\nSoru: {soru}")
        return response.text
    except: return "Şu an bağlantıda bir sorun var dostum."

# --- 5. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 6. 2x2 KARE MENÜ (GÖRSEL TABAKA) ---
st.markdown("""
    <div class="menu-grid">
        <div class="menu-card"><span class="menu-icon">📍</span><span class="menu-title">Rehber</span><span class="menu-sub">Lezzet & Plajlar</span></div>
        <div class="menu-card"><span class="menu-icon">🤖</span><span class="menu-title">Asistan</span><span class="menu-sub">Yapay Zeka Sohbet</span></div>
        <div class="menu-card"><span class="menu-icon">🎉</span><span class="menu-title">Etkinlik</span><span class="menu-sub">Konser & Ajanda</span></div>
        <div class="menu-card"><span class="menu-icon">💊</span><span class="menu-title">Eczane</span><span class="menu-sub">Nöbetçi Listesi</span></div>
    </div>
    """, unsafe_allow_html=True)

# --- 7. GÖRÜNMEZ BUTONLAR (İŞLEV TABAKASI) ---
col1, col2 = st.columns(2)
with col1:
    if st.button(" ", key="btn_rehber"): st.session_state.active_tab = "rehber"; st.rerun()
    if st.button(" ", key="btn_etkinlik"): st.session_state.active_tab = "etkinlik"; st.rerun()
with col2:
    if st.button(" ", key="btn_asistan"): st.session_state.active_tab = "asistan"; st.rerun()
    if st.button(" ", key="btn_eczane"): st.session_state.active_tab = "eczane"; st.rerun()

st.divider()

# --- 8. İÇERİK ALANI ---
tab = st.session_state.active_tab

if tab == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown(f"""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> {random.choice(["Badavut Gün Batımı", "Tostuyevski Tost", "Pinos Kahve"])}<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif tab == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    if "messages" not in st.session_state: st.session_state.messages = [{"role":"assistant","content":"Selam dostum! Sorunu sorabilirsin."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p := st.chat_input("Nereye gidelim?"):
        st.session_state.messages.append({"role":"user","content":p})
        with st.chat_message("user"): st.markdown(p)
        with st.chat_message("assistant"):
            c = yanıt_uret(p); st.markdown(c)
            st.session_state.messages.append({"role":"assistant","content":c})

elif tab == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif tab == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
