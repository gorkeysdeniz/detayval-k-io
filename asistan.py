import streamlit as st
import google.generativeai as genai

# --- 1. AI YAPILANDIRMASI ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    # Modelin 'Google Search' yeteneğini kullanabilmesi için yapılandırma
    genai.configure(api_key=API_KEY)
except:
    st.error("Lütfen Streamlit Settings > Secrets kısmına GEMINI_API_KEY ekle!")

st.set_page_config(page_title="Detayvalık Asistanı", layout="centered", page_icon="🏡")

# Modeli 'Google Search' (tools) desteğiyle başlatıyoruz
if "ai_model" not in st.session_state:
    try:
        # Gemini 1.5 Flash, Google Search yeteneğine sahip en hızlı modeldir
        st.session_state.ai_model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            tools=[{'google_search_retrieval': {}}] # İNTERNET ARAMA YETENEĞİ BURADA
        )
    except Exception as e:
        st.error(f"Bağlantı Hatası: {str(e)}")

# --- 2. SİSTEM TALİMATI ---
SYSTEM_INSTRUCTION = """
Sen Detayvalık Villa'nın dijital asistanısın. Samimi, yardımsever bir Ayvalıklı dostsun.
BİLGİLERİN: Tostuyevski, Cunda Uno, Kaktüs Cunda favori mekanlarındır. 
GÖREVİN: Eğer kullanıcı güncel bir bilgi (Nöbetçi eczane, hava durumu, etkinlik vb.) sorarsa Google üzerinden arama yap ve en güncel sonucu samimi bir dille aktar.
KURAL: İlk mesaj dışında kendini tanıtma.
"""

# --- 3. TASARIM ---
st.markdown("""<style>.main-header { background: linear-gradient(135deg, #1A3636 0%, #4F6F52 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-header"><h1>🏡 Detayvalık Asistanı</h1></div>', unsafe_allow_html=True)

t_rehber, t_ai, t_eczane = st.tabs(["📍 Rehber", "🤖 Akıllı Asistan", "💊 Nöbetçi Eczane"])

with t_rehber:
    st.info("🍴 Favoriler: Tostuyevski, Cunda Uno, Kaktüs Cunda.")

with t_ai:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba dostum! Ayvalık ile ilgili her şeyi bana sorabilirsin, senin için internette ufak bir araştırma bile yapabilirim!"}]

    chat_container = st.container()

    if prompt := st.chat_input("Sor bakalım dostum..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with chat_container:
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                try:
                    # Hafızayı ve arama motorunu kullanarak yanıt üret
                    history = st.session_state.messages[-3:]
                    context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
                    
                    response = st.session_state.ai_model.generate_content(f"{SYSTEM_INSTRUCTION}\n\n{context}\nSoru: {prompt}")
                    
                    if response.text:
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error("Şu an internetten bilgi alırken bir takılma oldu, lütfen tekrar sor.")

# --- NÖBETÇİ ECZANE BÖLÜMÜ ---
with t_eczane:
    st.subheader("🏥 Nöbetçi Eczane Bul")
    st.write("Dostum, 'Akıllı Asistan' sekmesine gidip **'Bugün Ayvalık'ta hangi eczane nöbetçi?'** diye sorarsan senin için hemen araştırıp bulurum!")
    st.write("---")
    st.link_button("🔗 Manuel Bakmak İstersen Tıkla", "https://www.aeo.org.tr/NobetciEczaneler/Balikesir/Ayvalik")
