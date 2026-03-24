import streamlit as st
import difflib

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. AYVALIK İŞLETME KÜTÜPHANESİ ---
BILGI_BANKASI = {
    "kahve": "☕ **Kahve & Tatlı:**\n- [Pinos Cafe](https://maps.app.goo.gl/Pinos)\n- [Crow Coffee](https://maps.app.goo.gl/Crow)\n- [Ivy Ayvalık](https://maps.app.goo.gl/Ivy)\n- [Daisy Küçükköy](https://maps.app.goo.gl/Daisy)\n- [Nona Cunda](https://maps.app.goo.gl/Nona)\n- [Cafe Melin](https://maps.app.goo.gl/Melin)\n- [Declan](https://maps.app.goo.gl/Declan)\n- [AIMA](https://maps.app.goo.gl/Aima)",
    
    "pizza": "🍕 **Pizza:**\n- [Pizza Teo](https://maps.app.goo.gl/Teo)\n- [Uno Cunda](https://maps.app.goo.gl/Uno)\n- [Tino Ristorante](https://maps.app.goo.gl/Tino)\n- [Küçük İtalya](https://maps.app.goo.gl/Italya)\n- [Cunda Luna](https://maps.app.goo.gl/Luna)",
    
    "yemek": "🍽️ **Restoranlar:**\n- **Ayna Cunda (Ödüllü):** [Konum](https://maps.app.goo.gl/Ayna)\n- **L'arancia (Ödüllü):** [Konum](https://maps.app.goo.gl/Larancia)\n- **By Nihat (Ödüllü):** [Konum](https://maps.app.goo.gl/ByNihat)\n- [Ritüel 1873](https://maps.app.goo.gl/Rituel)\n- [Köşebaşı](https://maps.app.goo.gl/Kosebasi)\n- [Papaz'ın Evi](https://maps.app.goo.gl/Papaz)\n- [Ayvalık Balıkçısı](https://maps.app.goo.gl/Balikci)\n- [Karina Ayvalık](https://maps.app.goo.gl/Karina)",
    
    "kokteyl": "🍸 **Kokteyl & Alkol:**\n- [Ritüel 1873 Cunda](https://maps.app.goo.gl/Rituel)\n- [Cunda Luna](https://maps.app.goo.gl/Luna)\n- [Ciello Cunda](https://maps.app.goo.gl/Ciello)\n- [Vino Şarap Evi](https://maps.app.goo.gl/Vino)\n- [De Jong Cocktails](https://maps.app.goo.gl/DeJong)\n- [Cunda Frenk](https://maps.app.goo.gl/Frenk)\n- [Felicita Küçükköy](https://maps.app.goo.gl/Felicita)\n- [Cunda Kaktüs](https://maps.app.goo.gl/Kaktus)",
    
    "beach": "🏖️ **Beach & Plajlar:**\n**Ücretli:** [Ajlan Eos](https://maps.app.goo.gl/Ajlan), [Kesebir](https://maps.app.goo.gl/Kesebir), [Sea Resort](https://maps.app.goo.gl/Sea), [Surya](https://maps.app.goo.gl/Surya)\n**Ücretsiz:** [Sarımsaklı Plajı](https://maps.app.goo.gl/Sarimsakli), [Badavut Plajı](https://maps.app.goo.gl/Badavut)",
    
    "eğlence": "🎉 **Eğlence:**\n- [La Fuga](https://maps.app.goo.gl/LaFuga), [Kraft](https://maps.app.goo.gl/Kraft), [Afişe Sahne](https://maps.app.goo.gl/Afise), [Aksi Pub](https://maps.app.goo.gl/Aksi), [The Public House](https://maps.app.goo.gl/Public)",
    
    "wifi": "📶 **Wi-Fi:** Detayvalik_Villa | **Şifre:** `ayvalik2026`",
    "taksi": "🚕 **Sarımsaklı Taksi:** 0266 396 10 10"
}

# --- 3. CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; font-family: 'Inter', sans-serif; }
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white !important; padding: 30px; border-radius: 20px; text-align: center; margin-bottom: 20px;
    }
    div.stButton > button {
        background: white !important; color: #1a2a3a !important;
        border: 1px solid #eee !important; border-radius: 15px !important;
        width: 100% !important; height: 95px !important; font-weight: 700 !important;
    }
    .content-box { background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #2c5364; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. BAŞLIK ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1><p>Seçkin Mekanlar & Konaklama Rehberi</p></div>', unsafe_allow_html=True)

# --- 5. 4x2 BUTONLAR ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🤖\nAsistan", key="b1"): st.session_state.secili_sayfa = "asistan"; st.rerun()
with c2:
    if st.button("🍽️\nYemek", key="b2"): st.session_state.secili_sayfa = "yemek"; st.rerun()
with c3:
    if st.button("☕\nKahve", key="b3"): st.session_state.secili_sayfa = "kahve"; st.rerun()
with c4:
    if st.button("🏖️\nBeach", key="b4"): st.session_state.secili_sayfa = "beach"; st.rerun()

c5, c6, c7, c8 = st.columns(4)
with c5:
    if st.button("🍸\nKokteyl", key="b5"): st.session_state.secili_sayfa = "kokteyl"; st.rerun()
with c6:
    if st.button("🎉\nEğlence", key="b6"): st.session_state.secili_sayfa = "eğlence"; st.rerun()
with c7:
    if st.button("🚕\nTaksi", key="b7"): st.session_state.secili_sayfa = "taksi"; st.rerun()
with c8:
    if st.button("📜\nKurallar", key="b8"): st.session_state.secili_sayfa = "kurallar"; st.rerun()

st.divider()

# --- 6. İÇERİKLER ---
s = st.session_state.secili_sayfa

if s == "asistan":
    st.subheader("🤖 Akıllı Asistan")
    p = st.chat_input("Örn: nerede kahve içilir?")
    if p:
        with st.chat_message("user"): st.write(p)
        f = False
        for k in p.lower().split():
            match = difflib.get_close_matches(k, BILGI_BANKASI.keys(), n=1, cutoff=0.5)
            if match:
                with st.chat_message("assistant"): st.success(BILGI_BANKASI[match[0]])
                f = True; break
        if not f:
            with st.chat_message("assistant"): st.info("🤖 Bu konuyu hemen inceliyorum...")

elif s == "yemek":
    st.markdown(f'<div class="content-box"><h3>🍽️ Restoranlar</h3>{BILGI_BANKASI["yemek"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="content-box"><h3>🍕 Pizza</h3>{BILGI_BANKASI["pizza"]}</div>', unsafe_allow_html=True)

elif s == "kahve":
    st.markdown(f'<div class="content-box"><h3>☕ Kahve</h3>{BILGI_BANKASI["kahve"]}</div>', unsafe_allow_html=True)

elif s == "beach":
    st.markdown(f'<div class="content-box"><h3>🏖️ Plajlar</h3>{BILGI_BANKASI["beach"]}</div>', unsafe_allow_html=True)

elif s == "kokteyl":
    st.markdown(f'<div class="content-box"><h3>🍸 Kokteyl & Alkol</h3>{BILGI_BANKASI["kokteyl"]}</div>', unsafe_allow_html=True)

elif s == "eğlence":
    st.markdown(f'<div class="content-box"><h3>🎉 Eğlence</h3>{BILGI_BANKASI["eğlence"]}</div>', unsafe_allow_html=True)

elif s == "taksi":
    st.markdown(f'<div class="content-box"><h3>🚕 Taksi</h3>{BILGI_BANKASI["taksi"]}</div>', unsafe_allow_html=True)

elif s == "kurallar":
    st.markdown('<div class="content-box"><h3>📜 Kurallar</h3>- Giriş: 14:00 | Çıkış: 11:00<br>- 23:00 Sessizlik rica olunur.</div>', unsafe_allow_html=True)
