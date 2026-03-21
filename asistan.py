import streamlit as st
import random

# --- 1. YAPILANDIRMA ---
st.set_page_config(page_title="Detayvalık Asistanı Beta 1.2", layout="centered", page_icon="🏡")

# --- 2. SESSION STATE (Tıklanan sekmeyi takip et) ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "rehber"

# URL'den gelen komutu yakala (Tıklama hilesi için)
query_params = st.query_params
if "action" in query_params:
    st.session_state.active_tab = query_params["action"]
    st.query_params.clear() # URL'yi temizle
    st.rerun()

# --- 3. CSS: MOBİLDE BİLE BOZULMAYAN 2x2 GRID ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 25px 10px; border-radius: 20px; text-align: center; margin-bottom: 20px; position: relative;
    }
    .beta-badge { position: absolute; top: 10px; right: 15px; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 10px; font-size: 10px; }

    /* GERÇEK 2x2 GRID (Mobilde asla bozulmaz) */
    .menu-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 20px;
    }
    
    .menu-item {
        background-color: white;
        border: 1px solid #eee;
        border-radius: 15px;
        padding: 20px 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        text-decoration: none;
        color: #2c3e50;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: transform 0.1s, background-color 0.2s;
        cursor: pointer;
    }
    
    .menu-item:active {
        transform: scale(0.95);
        background-color: #f0f2f6;
    }
    
    .menu-icon { font-size: 28px; margin-bottom: 5px; }
    .menu-text { font-weight: 700; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
st.markdown(f'<div class="main-header"><div class="beta-badge">Beta 1.2</div><h1>🏠 Detayvalık Asistanı</h1><p>Ayvalık Tatil Rehberinize Hoş Geldiniz</p></div>', unsafe_allow_html=True)

# --- 5. TIKLANABİLİR 2x2 HTML MENÜ ---
# href kısmına ?action=... ekleyerek tıklamayı simüle ediyoruz
st.markdown("""
    <div class="menu-container">
        <a href="/?action=rehber" target="_self" class="menu-item">
            <span class="menu-icon">📍</span>
            <span class="menu-text">Rehber</span>
        </a>
        <a href="/?action=asistan" target="_self" class="menu-item">
            <span class="menu-icon">🤖</span>
            <span class="menu-text">Asistan</span>
        </a>
        <a href="/?action=etkinlik" target="_self" class="menu-item">
            <span class="menu-icon">🎉</span>
            <span class="menu-text">Etkinlik</span>
        </a>
        <a href="/?action=eczane" target="_self" class="menu-item">
            <span class="menu-icon">💊</span>
            <span class="menu-text">Eczane</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

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
    st.info("Sohbet ekranı yakında buraya eklenecek...")

elif tab == "etkinlik":
    st.subheader("🎉 Yaklaşan Etkinlikler")
    st.info("🎤 24 Mart: Teoman Konseri | 🎸 27 Mart: Pinhani")

elif tab == "eczane":
    st.subheader("💊 Nöbetçi Eczaneler")
    st.link_button("Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler", use_container_width=True)
