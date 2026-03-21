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

# --- 2. CSS: 2x2 GRID VE BUTON TASARIMI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    /* Ana Başlık */
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px; position: relative;
    }
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    /* Butonları Kare Karta Dönüştürme */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
        width: 100% !important;
        height: 140px !important; /* Kare formu için yükseklik */
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.2s ease !important;
        margin-bottom: 10px !important;
    }
    
    div.stButton > button:active {
        transform: scale(0.95) !important;
        background-color: #f0f2f6 !important;
    }

    /* Buton içindeki metin düzeni */
    div.stButton > button p {
        font-weight: 700 !important;
        font-size: 16px !important;
        white-space: pre-wrap !important;
        text-align: center !important;
        line-height: 1.4 !important;
    }

    /* Orijinal Streamlit sekmelerini gizle */
    .stTabs [data-baseweb="tab-list"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "rehber"

# --- 4. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 BUTON GRİDİ (MOBİL UYUMLU) ---
col1, col2 = st.columns(2)

with col1:
    if st.button("📍\n\nRehber", key="btn_rehber"):
        st.session_state.active_tab = "rehber"
        st.rerun()
    
    if st.button("🎉\n\nEtkinlik", key="btn_etkinlik"):
        st.session_state.active_tab = "etkinlik"
        st.rerun()

with col2:
    if st.button("🤖\n\nAsistan", key="btn_asistan"):
        st.session_state.active_tab = "asistan"
        st.rerun()
    
    if st.button("💊\n\nEczane", key="btn_eczane"):
        st.session_state.active_tab = "eczane"
        st.rerun()

st.divider()

# --- 6. İÇERİK ALANI ---
tab = st.session_state.active_tab

if tab == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown(f"""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> {random.choice(["Badavut'ta gün batımı!", "Tostuyevski'de bir karışık!", "Cunda sahilinde yürüyüş!"])}<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif tab == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role":"assistant","content":"Selam dostum! Ayvalık hakkında ne bilmek istersin?"}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
            
    if p := st.chat_input("Nereye gidelim dostum?"):
        st.session_state.messages.append({"role":"user","content":p})
        st.rerun() # Mesajı hemen listeye eklemek için

elif tab == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif tab == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
