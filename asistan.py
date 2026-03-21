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

# --- 2. CSS: BUTONLARI KARTA DÖNÜŞTÜRME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 30px 10px; border-radius: 20px; text-align: center; margin-bottom: 25px; position: relative;
    }
    
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    /* Butonları Kart Haline Getiren CSS */
    div.stButton > button {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 1px solid #eee !important;
        padding: 40px 20px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
        width: 100% !important;
        height: 130px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.3s ease !important;
        line-height: 1.2 !important;
    }
    
    div.stButton > button:hover {
        border-color: #2c5364 !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
    }

    div.stButton > button p {
        font-weight: 700 !important;
        font-size: 16px !important;
        margin: 0 !important;
    }

    /* Streamlit sekmelerini gizle */
    .stTabs [data-baseweb="tab-list"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "rehber"

# --- 4. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. 2x2 GERÇEK BUTON MENÜSÜ (TIKLAMA GARANTİLİ) ---
col1, col2 = st.columns(2)

with col1:
    if st.button("📍\nRehber", key="btn_rehber"):
        st.session_state.active_tab = "rehber"
        st.rerun()
    
    if st.button("🎉\nEtkinlik", key="btn_etkinlik"):
        st.session_state.active_tab = "etkinlik"
        st.rerun()

with col2:
    if st.button("🤖\nAsistan", key="btn_asistan"):
        st.session_state.active_tab = "asistan"
        st.rerun()
    
    if st.button("💊\nEczane", key="btn_eczane"):
        st.session_state.active_tab = "eczane"
        st.rerun()

st.divider()

# --- 6. İÇERİK ALANI ---
tab = st.session_state.active_tab

if tab == "rehber":
    st.subheader("📍 Ayvalık Rehberi")
    st.markdown(f"""<div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #2c5364; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
    💡 <b>Günün Önerisi:</b> {random.choice(["Badavut Gün Batımı", "Tostuyevski Tost", "Pinos Kahve"])}<br><br>
    🌐 <b>Wi-Fi:</b> Detayvalik_Villa | <b>Şifre:</b> ayvalik2026
    </div>""", unsafe_allow_html=True)

elif tab == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    if "messages" not in st.session_state: st.session_state.messages = [{"role":"assistant","content":"Selam dostum! Ayvalık hakkında sorun varsa buradayım."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p := st.chat_input("Nereye gidelim?"):
        st.session_state.messages.append({"role":"user","content":p})
        # Basit yanıt mekanizması (Hızı korumak için)
        st.session_state.messages.append({"role":"assistant","content":"Harika bir soru! Ayvalık'ta bunu yapmak harika olur."})
        st.rerun()

elif tab == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif tab == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
