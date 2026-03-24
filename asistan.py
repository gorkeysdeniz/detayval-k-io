import streamlit as st
import difflib  # Yanlış yazımları anlamak için (0 Token maliyet)

# --- 1. BİLGİ BANKASI (AI'ya gitmeden cevaplanacaklar) ---
# Burayı dilediğin kadar uzatabilirsin
BILGI_BANKASI = {
    "wifi": "📶 **Wi-Fi Bilgileri:**\nAğ Adı: Detayvalik_Villa\nŞifre: `ayvalik2026`",
    "internet": "📶 **Wi-Fi Bilgileri:**\nAğ Adı: Detayvalik_Villa\nŞifre: `ayvalik2026`",
    "şifre": "📶 **Wi-Fi Bilgileri:**\nAğ Adı: Detayvalik_Villa\nŞifre: `ayvalik2026`",
    "giriş": "🔑 **Giriş/Çıkış Saatleri:**\nGiriş: 14:00\nÇıkış: 11:00",
    "konum": "📍 **Adres:** Sarımsaklı Mevkii, No:9. Google Maps üzerinden 'Detayvalık' olarak aratabilirsiniz.",
    "mangal": "🍢 **Mangal:** Bahçede mangal ekipmanımız mevcuttur. Lütfen güvenlik için kullandıktan sonra közleri kontrol ediniz.",
    "plaj": "🏖️ **Plaj:** Sarımsaklı plajına yürüyerek 5 dakika mesafededir."
}

# --- 2. HİBRİT CEVAP FONKSİYONU ---
def asistan_cevap(soru):
    soru_temiz = soru.lower()
    kelimeler = soru_temiz.split()
    
    # Adım 1: Bilgi Bankasında "Fuzzy" (Bulanık) arama yap
    for k in kelimeler:
        # %60 benzerlik yakalarsa AI'ya gitmeden cevabı yapıştırır
        eslesme = difflib.get_close_matches(k, BILGI_BANKASI.keys(), n=1, cutoff=0.6)
        if eslesme:
            return BILGI_BANKASI[eslesme[0]], False # False = AI kullanılmadı

    # Adım 2: Eğer yukarıda bulunamazsa AI'ya yönlendir (Burada API devreye girecek)
    return "🤖 Bu soruyu Yapay Zekaya soruyorum...", True # True = AI gerekiyor

# --- 6. İÇERİK ALANI (ASİSTAN KISMI GÜNCELLEME) ---
# Senin kodundaki 'elif sayfa == "asistan":' kısmını bununla değiştiriyoruz:

elif sayfa == "asistan":
    st.subheader("🤖 Detayvalık AI Asistan")
    
    # Mesaj geçmişini tutmak istersen (Basit versiyon)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Geçmiş mesajları göster
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Kullanıcıdan soru al
    if prompt := st.chat_input("Sorunu yaz dostum (Örn: ntrenr şifresi)..."):
        # Kullanıcı mesajını ekrana bas
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Cevabı üret
        cevap, ai_lazim = asistan_cevap(prompt)
        
        with st.chat_message("assistant"):
            if ai_lazim:
                # BURAYA API ÇAĞRISI GELECEK
                # Örn: response = get_gemini_response(prompt)
                st.warning("⚠️ Bilgi bankasında bulunamadı, AI limiti kontrol ediliyor...")
                st.write(cevap) 
            else:
                st.success("✅ Bilgi bankasından yanıtlandı (0 Token)")
                st.write(cevap)
        
        st.session_state.messages.append({"role": "assistant", "content": cevap})
