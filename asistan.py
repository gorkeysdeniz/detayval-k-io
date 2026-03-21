import streamlit as st
import google.generativeai as genai
import random

# --- 1. YAPILANDIRMA (Gemini Geri Geldi) ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        if "model" not in st.session_state:
            st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Gemini bağlantısı kurulamadı, API anahtarını kontrol et!")

st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. CSS: 2x2 IZGARA VE TIKLANABİLİR KARTLAR ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 30px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px; position: relative;
    }
    
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    .menu-grid {
        display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;
    }
    
    .menu-card {
        background: white; padding: 20px 10px; border-radius: 15px; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #eee;
        text-decoration: none !important; display: block; transition: transform 0.2s;
    }
    .menu-card:active { transform: scale(0.95); background-color: #f0f0f0; }
    
    .menu-icon { font-size: 30px; display: block; margin-bottom: 5px; }
    .menu-title { font-weight: 700; color: #2c3e50; font-size: 14px; display: block; }
    .menu-sub { font-size: 9px; color: #95a5a6; display: block; }

    .stTabs [data-baseweb="tab-list"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ASİSTAN BEYNİ (Bilgi Bankası & Yanıt Motoru) ---
BILGI_BANKASI = {
    "yemek": {"anahtarlar": ["yemek", "restoran", "pizza", "ne yiyelim"], "cevap": "🍕 **Pizza:** Cunda Uno veya Küçük İtalya.\n🥪 **Tost:** Tostuyevski (Efsanedir).\n🍝 **Akşam:** Pizza Teos veya Tino Pizza."},
    "tost": {"anahtarlar": ["tost", "tostçu", "tostuyevski"], "cevap": "Ayvalık'ta tost denince akla gelen ilk yer **Tostuyevski**!"},
    "plaj": {"anahtarlar": ["plaj", "deniz", "beach", "yüzme"], "cevap": "🏖️ **Öneri:** Badavut (Favorim!), Sarımsaklı ve Ortunç Koyu."},
}

def yanıt_uret(soru):
    soru_low = soru.lower()
    # Önce bilgi bankası
    for kategori, icerik in BILGI_BANKASI.items():
        if any(anahtar in soru_low for anahtar in icerik["anahtarlar"]):
            return icerik["cevap"]
    # Sonra Gemini
    try:
        sys_msg = "Sen Detayvalık Villa asistanı samimi bir Ayvalıklısın. Kısa ve öz cevap ver. Selam verenle selamlaş."
        response = st.session_state.model.generate_content(f"{sys_msg}\n\nSoru: {soru}")
        return response.text
    except:
        return "Dostum şu an internette bir dalgalanma var sanırım, ama rehber bilgilerim hala burada!"

# --- 4. TIKLAMA MANTIĞI ---
query_params = st.query_params
active_tab = query_params.get("tab", "rehber")

# --- 5. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 6. 2x2 KARE MENÜ ---
st.markdown(f"""
    <div class="menu-grid">
        <a href="/?tab=rehber" target="_self" class="menu-card">
            <span class="menu-icon">📍</span><span class="menu-title">Rehber</span><span class="menu-sub">Lezzet & Plajlar</span>
        </a>
        <a href="/?tab=asistan" target="_self" class="menu-card">
            <span class="menu-icon">🤖</span><span class="menu-title">Asistan</span><span class="menu-sub">Yapay Zeka Sohbet</span>
        </a>
        <a href="/?tab=etkinlik" target="_self" class="menu-card">
            <span class="menu-icon">🎉</span><span class="menu-title">Etkinlik</span><span class="menu-sub">Konser & Ajanda</span>
        </a>
        <a href="/?tab=eczane" target="_self" class="menu-card">
            <span class="menu-icon">💊</span><span class="menu-title">Eczane</span><span class="menu-sub">Nöbetçi Listesi</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 7. İÇERİK ALANI ---
if active_tab == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown(f"""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> {random.choice(["Badavut Gün Batımı", "Tostuyevski Tost", "Pinos Kahve"])}<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026<br><br>
    📜 <b>Konaklama Kurallarımız:</b><br>
    • Gece 00:00'dan sonra sessizlik rica olunur.<br>
    • Çıkarken klimaları kapatmayı unutmayın.
    </div>""", unsafe_allow_html=True)

elif active_tab == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Ayvalık hakkında ne bilmek istersin?"}]
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
    if prompt := st.chat_input("Nereye gidelim dostum?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            cevap = yanıt_uret(prompt)
            st.markdown(cevap)
            st.session_state.messages.append({"role": "assistant", "content": cevap})

elif active_tab == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif active_tab == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
