import streamlit as st
import time

# --- 1. AYARLAR & TASARIM ---
st.set_page_config(page_title="Detayvalık Misafir Asistanı", layout="centered", page_icon="🏡")

# Mobil Odaklı Şık Tasarım (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #FDFDFD; }
    .main-header { 
        background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); 
        color: white; padding: 25px; border-radius: 20px; text-align: center; 
        margin-bottom: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .info-card { 
        background: white; padding: 20px; border-radius: 15px; 
        border-left: 6px solid #D6BD98; margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .wa-button {
        background-color: #25D366; color: white !important; padding: 12px 20px;
        border-radius: 10px; text-decoration: none; font-weight: bold;
        display: inline-block; text-align: center; width: 100%; margin-top: 10px;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #f0f2f6; border-radius: 10px 10px 0 0; padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. KARŞILAMA EKRANI ---
st.markdown("""
    <div class="main-header">
        <h1>🏡 Detayvalık'a Hoş Geldiniz</h1>
        <p>Ege'nin kalbinde, huzur dolu bir tatil sizi bekliyor.</p>
    </div>
    """, unsafe_allow_html=True)

# Sekmeler (Tablar)
t_ana, t_rehber, t_ai = st.tabs(["✨ Hızlı Bilgi", "📍 Ayvalık Rehberi", "🤖 Akıllı Asistan"])

# --- TAB 1: ANA SAYFA (KRİTİK BİLGİLER) ---
with t_ana:
    st.markdown("### 🔑 Konaklama Detayları")
    st.markdown("""
    <div class="info-card">
        🌐 <b>Wi-Fi Adı:</b> Detayvalik_Guest<br>
        🔑 <b>Wi-Fi Şifre:</b> ayvalik2026<br><br>
        🕒 <b>Giriş:</b> 14:00 | 🕒 <b>Çıkış:</b> 11:00
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📜 Ev Kurallarımız"):
        st.write("• Ev içerisinde sigara içilmemesini rica ederiz.🚭")
        st.write("• Evcil hayvan kabul edilmemektedir.🐾")
        st.write("• Gece 00:00'dan sonra yüksek ses yasağı mevcuttur.🤫")
        st.write("• Çöplerinizi sabah 09:00'da bahçe kapısı önüne bırakabilirsiniz.")

    st.markdown('<a href="https://wa.me/905XXXXXXXXX" class="wa-button">📱 Ev Sahibine Soru Sor</a>', unsafe_allow_html=True)

# --- TAB 2: AYVALIK REHBERİ (SENİN TAVSİYELERİN) ---
with t_rehber:
    st.markdown("### 🍴 Lezzet Durakları")
    st.info("🥪 **Ayvalık Tostu:** Sarımsaklı merkezdeki 'X Kantin' gerçek Ayvalık tostunun adresidir.")
    st.success("🐟 **Cunda Balıkçıları:** Akşam yemeği için 'Y Restoran' favorimizdir.")
    
    st.markdown("### 🏖️ Plaj & Doğa")
    st.warning("🌊 **Badavut:** Rüzgarlı havalarda denizin en sakin olduğu yerdir.")
    st.write("📍 **Şeytan Sofrası:** Gün batımını izlemeden sakın dönmeyin!")

# --- TAB 3: YAPAY ZEKA ASİSTANI (GİRİŞ CÜMLESİ DÜZENLENDİ) ---
with t_ai:
    st.markdown("### 🤖 Detayvalık Akıllı Asistan")
    
    # Giriş Cümlesi (İstediğin Resmi Format)
    st.write("---")
    st.write("**Merhaba, Detayvalık.io Ayvalık Rehberine hoş geldin. Ayvalık ile ilgili (yeme-içme, mekanlar, etkinlikler) ve Detayvalık Villa hakkında merak ettiğin tüm soruları bana sorabilirsin.**")
    st.write("---")
    
    # Sohbet Geçmişi Başlatma
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mesajları Görüntüle
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Kullanıcıdan Girdi Al
    if prompt := st.chat_input("Dostum aklına takılan ne varsa sor..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Yanıtı (Simülasyon - Adım 4'te Gerçek Beyin Takılacak)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = "Selam dostum! Bu sorunu hemen cevaplayacağım ama önce yapay zeka beynimin (API) bağlanmasını bekliyorum. Gece operasyonu devam ediyor! 😊"
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
