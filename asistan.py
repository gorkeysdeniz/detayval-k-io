import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Lütfen Secrets kısmına GEMINI_API_KEY ekle!")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

if "ai_model" not in st.session_state:
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_models = ['models/gemini-1.5-flash', 'models/gemini-pro']
        chosen_model = next((m for m in target_models if m in available_models), available_models[0])
        st.session_state.ai_model = genai.GenerativeModel(chosen_model)
    except Exception as e:
        st.error(f"Bağlantı Hatası: {str(e)}")

# --- 2. HAFIZA VE VERİ YÖNETİMİ ---
# Eczane bilgisini tarayıcı hafızasında tutuyoruz
if "nobetci_eczane" not in st.session_state:
    st.session_state.nobetci_eczane = "Bugün için nöbetçi eczane bilgisi henüz girilmedi."

SYSTEM_INSTRUCTION = "Sen Detayvalık Villa asistanısın. Samimi bir dostsun. İlk mesaj dışında kendini tanıtma."

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_eczane = st.tabs(["📍 Rehber", "🤖 Asistan", "💊 Nöbetçi Eczane"])

with t_rehber:
    st.info("🍴 Favoriler: Tostuyevski, Cunda Uno, Kaktüs Cunda.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Selam dostum! Ayvalık hakkında ne bilmek istersin?"}]
    
    chat_container = st.container()
    if prompt := st.chat_input("Sor bakalım..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        try:
            history = st.session_state.messages[-3:]
            context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
            response = st.session_state.ai_model.generate_content(f"{SYSTEM_INSTRUCTION}\n\n{context}\nAsistan:")
            if response.text:
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except: st.error("Bir takılma oldu.")

    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])

# --- NÖBETÇİ ECZANE GÖRÜNÜMÜ ---
with t_eczane:
    st.subheader("🏥 Güncel Nöbetçi Eczane")
    st.success(f"📌 {st.session_state.nobetci_eczane}")
    st.write("---")
    st.link_button("🔗 Resmi Listeye Git", "https://www.aeo.org.tr/NobetciEczaneler/Balikesir/Ayvalik")

# --- GİZLİ YÖNETİCİ PANELİ (SAYFANIN EN ALTI) ---
with st.expander("⚙️ Yönetici Girişi (Sadece Senin İçin)"):
    yeni_eczane = st.text_input("Bugünün nöbetçi eczanesini ve telefonunu yaz:", placeholder="Örn: Çarşı Eczanesi - 0266 XXX XX XX")
    if st.button("Bilgiyi Güncelle"):
        st.session_state.nobetci_eczane = yeni_eczane
        st.success("Bilgi güncellendi! Misafirler artık bunu görecek.")
        st.rerun()
