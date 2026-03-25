import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. CSS (KESİN ÇÖZÜM: TRANSPARENT OVERLAY) ---
st.markdown("""
    <style>
    .block-container { padding: 1rem 0.5rem !important; max-width: 100% !important; }
    
    /* PINTEREST GRID YAPISI */
    .p-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
        position: relative;
    }

    /* ŞIK GÖRÜNEN KUTULAR */
    .p-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        height: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        z-index: 1;
    }
    .p-icon { font-size: 24px; margin-bottom: 4px; }
    .p-text { font-size: 12px; font-weight: 700; color: #1e293b; }

    /* GERÇEK STREAMLIT BUTONLARINI GÖRÜNMEZ YAP VE KUTULARIN ÜSTÜNE KOY */
    div.stButton {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 2; /* Kutunun üstünde olsun */
    }
    div.stButton > button {
        width: 100% !important;
        height: 100px !important;
        background: transparent !important; /* Görünmez yap */
        color: transparent !important;     /* Yazıyı gizle */
        border: none !important;
        box-shadow: none !important;
    }
    
    .grid-item { position: relative; height: 100px; }

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

st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# --- 3. GRID VE BUTONLAR (İÇ İÇE) ---
# Burada butonlar kutuların tam üzerine biner, yazılarını CSS ile sildik.
def draw_button(label, icon, key, target):
    st.markdown(f"""
    <div class="grid-item">
        <div class="p-box">
            <div class="p-icon">{icon}</div>
            <div class="p-text">{label}</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("", key=key): # Boş etiketli gerçek buton
        st.session_state.secili_sayfa = target
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Grid Başlangıcı
st.markdown('<div class="p-grid">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1: draw_button("Asistan", "🤖", "b1", "asistan")
with col2: draw_button("Yemek", "🍽️", "b2", "yemek")
with col3: draw_button("Pizza", "🍕", "b3", "pizza")

col4, col5, col6 = st.columns(3)
with col4: draw_button("Kahve", "☕", "b4", "kahve")
with col5: draw_button("Beach", "🏖️", "b5", "beach")
with col6: draw_button("Kokteyl", "🍸", "b6", "kokteyl")

col7, col8, col9 = st.columns(3)
with col7: draw_button("Eğlence", "🎉", "b7", "eglence")
with col8: draw_button("Taksi", "🚕", "b8", "taksi")
with col9: draw_button("Eczane", "💊", "b9", "eczane")

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# --- 4. İÇERİK VERİSİ VE FONKSİYONLAR (DOKUNULMADI) ---
# Buradaki verilerin ve kart_bas fonksiyonun aynen kalıyor...
def kart_bas(key):
    # Senin mevcut mekan listeleme kodun buraya gelecek
    st.write(f"{key.capitalize()} için öneriler yükleniyor...")

# --- 5. GÖSTERİM ---
s = st.session_state.secili_sayfa
if s == "asistan":
    st.markdown("##### 🤖 Size Nasıl Yardımcı Olabilirim?")
    st.chat_input("Pizza, Kahve, Plaj...")
else:
    kart_bas(s)
