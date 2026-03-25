import streamlit as st

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Ayvalık Asistanı", layout="centered", page_icon="🏡")

if "secili_sayfa" not in st.session_state:
    st.session_state.secili_sayfa = "asistan"

# --- 2. ÖZEL CSS (YATAY KAYDIRILABİLİR MENÜ) ---
st.markdown("""
    <style>
    /* Mobilde kolonların alta binmesini engellemek için ana ayar */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        padding-bottom: 10px !important;
    }
    
    /* Kaydırma çubuğunu gizle */
    [data-testid="stHorizontalBlock"]::-webkit-scrollbar { display: none; }

    /* Butonların kutu yapısı */
    div.stButton > button {
        width: 85px !important;
        height: 85px !important;
        border-radius: 15px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: white !important;
        color: #1e293b !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 11px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }

    /* Seçili butonu vurgula */
    div.stButton > button:focus {
        border: 2px solid #2c5364 !important;
        background-color: #f8fafc !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: white; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 20px;
    }
    .venue-card {
        background: white; padding: 12px; border-radius: 12px; margin-bottom: 8px;
        border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BAŞLIK VE MENÜ ---
st.markdown('<div class="main-header"><h1>🏡 Ayvalık Asistanı</h1></div>', unsafe_allow_html=True)

# Tek bir satırda (row) tüm butonları yan yana diziyoruz
# Streamlit artık bunları alta atmayacak, sağa doğru kaydıracak
menu_cols = st.columns(9)

def create_tab(col, label, icon, target, key):
    with col:
        # Butonun üstünde emoji, altında yazı görünmesi için \n kullanıyoruz
        if st.button(f"{icon}\n{label}", key=key):
            st.session_state.secili_sayfa = target
            st.rerun()

create_tab(menu_cols[0], "Asistan", "🤖", "asistan", "m1")
create_tab(menu_cols[1], "Yemek", "🍽️", "yemek", "m2")
create_tab(menu_cols[2], "Pizza", "🍕", "pizza", "m3")
create_tab(menu_cols[3], "Kahve", "☕", "kahve", "m4")
create_tab(menu_cols[4], "Beach", "🏖️", "beach", "m5")
create_tab(menu_cols[5], "Kokteyl", "🍸", "kokteyl", "m6")
create_tab(menu_cols[6], "Eğlence", "🎉", "eglence", "m7")
create_tab(menu_cols[7], "Taksi", "🚕", "taksi", "m8")
create_tab(menu_cols[8], "Eczane", "💊", "eczane", "m9")

st.divider()

# --- 4. MEKAN VERİSİ VE FONKSİYONLAR (DOKUNULMADI) ---
# Mevcut MEKAN_VERISI ve kart_bas fonksiyonun buraya gelecek...

s = st.session_state.secili_sayfa

if s == "asistan":
    st.info("🤖 Size nasıl yardımcı olabilirim?")
    st.chat_input("Pizza, Taksi, Kahve...")
else:
    # kart_bas(s) fonksiyonunu burada çağırabilirsin
    st.write(f"### {s.capitalize()} Önerileri")
    # Örnek: kart_bas(s) 
