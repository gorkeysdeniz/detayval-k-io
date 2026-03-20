import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI (SECRETS KONTROLÜ) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Lütfen Streamlit Settings > Secrets kısmına GEMINI_API_KEY ekle!")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# Model Seçici (Sabit ve Hızlı Hafıza)
if "ai_model" not in st.session_state:
    try:
        # En stabil model olan flash ile devam ediyoruz
        st.session_state.ai_model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Bağlantı Hatası: {str(e)}")

# --- 2. SİSTEM TALİMATI (SENİN VERİ TABANIN) ---
SYSTEM_INSTRUCTION = """
Sen Detayvalık Villa asistanısın. Samimi, Ayvalıklı bir dostsun. 
FAVORİLERİN: Tostuyevski, Aşkın Tost Evi, Cunda Uno, Küçük İtalya, Kaktüs Cunda, Badavut Plajı.
KURAL: Sadece bildiğin sabit bilgilerle cevap ver. Bilmediğin güncel konular için (eczane vb.) 'Yan sekmedeki güncel listeye bakabilirsin dostum' de. 
İlk mesaj dışında kendini tanıtma.
"""

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_eczane = st.tabs(["📍 Rehber", "🤖 Akıllı Asistan", "💊 Nöbetçi Eczane"])

with t_rehber:
    st.info("🍴 **Önerilerimiz:** Tostuyevski, Cunda Uno, Kaktüs Cunda.")
    st.success("🌊 **Plajlar:** Badavut ve Sarımsaklı favorimiz.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba! Ayvalık Rehberine hoş geldin. Sana nasıl yardımcı olabilirim dostum?"}]

    # MESAJLARI SABİT TUTAN KONTEYNER (KAYMAYI ENGELLER)
    chat_container = st.container()

    if prompt := st.chat_input("Sor bakalım dostum..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        try:
            # Hafızayı taze tutmak için son 3 mesajı kullan
            history = st.session_state.messages[-3:]
            context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
            
            response = st.session_state.ai_model.generate_content(f"{SYSTEM_INSTRUCTION}\n\n{context}\nSoru: {prompt}\nAsistan:")
            
            if response.text:
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except:
            st.error("Ufak bir takılma oldu dostum, tekrar sorar mısın?")

    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# --- 4. NÖBETÇİ ECZANE (RESMİ VERİ) ---
with t_eczane:
    st.subheader("🏥 Güncel Nöbetçi Eczaneler")
    st.write("Dostum, Ayvalık'taki bugünkü nöbetçi eczaneleri en doğru şekilde aşağıdaki resmi listeden görebilirsin:")
    
    # Senin attığın resmi linki buraya buton olarak ekledik
    st.link_button("💊 Nöbetçi Eczane Listesini Aç", "https://www.balikesireczaciodasi.org.tr/nobetci-eczaneler")
    
    st.divider()
    st.warning("⚠️ **Hatırlatma:** Nöbetçi eczaneler her sabah saat 09:00'da değişir.")
    st.info("☎️ Acil Durumlar İçin: **112**")
