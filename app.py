import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Merkez Bankası Simülatörü", layout="centered")

st.title("🏦 Merkez Bankası Simülatörü – Ekonomiyi Sen Yönet!")

st.markdown("""
### 🎯 Amaç:
Bu simülatörde **Merkez Bankası Başkanı** sizsiniz. Faiz oranı, parasal genişleme ve rezerv yönetimi kararlarınız ile **enflasyon, işsizlik, büyüme ve döviz kuru** gibi makro göstergeler nasıl değişiyor göreceksiniz.
""")

# 🎛️ Politika Araçları
st.sidebar.header("🎛️ Politika Seçimleri")

faiz = st.sidebar.slider("Faiz Oranı (%)", min_value=0, max_value=50, value=30, step=1)
parasal_genisleme = st.sidebar.slider("Parasal Genişleme (Milyar TL)", min_value=0, max_value=1000, value=100, step=50)
rezerv = st.sidebar.slider("Rezerv (Milyar $)", min_value=0, max_value=200, value=100, step=10)

st.sidebar.markdown("---")
st.sidebar.markdown("👉 Daha düşük faiz → Büyüme ↑ ama Enflasyon ↑ ve Kur ↑")
st.sidebar.markdown("👉 Daha yüksek faiz → Enflasyon ↓ ve Kur ↓ ama İşsizlik ↑")

# 🎯 Başlangıç değerleri
usd_try = 32
enflasyon = 50
buyume = 3
issizlik = 10

# 🧠 Ekonomik Modelleme
# Faiz etkisi
usd_try -= faiz * 0.2
enflasyon -= faiz * 0.8
issizlik += faiz * 0.4
buyume -= faiz * 0.2

# Parasal genişleme etkisi
usd_try += parasal_genisleme * 0.05
enflasyon += parasal_genisleme * 0.1
buyume += parasal_genisleme * 0.05

# Rezerv etkisi
usd_try -= rezerv * 0.05
enflasyon -= rezerv * 0.02

# Limitler (mantıklı sınırlar)
usd_try = max(5, usd_try)
enflasyon = max(0, enflasyon)
issizlik = min(100, max(3, issizlik))
buyume = min(10, max(-5, buyume))

# 📊 Sonuç Ekranı
st.subheader("📊 Simülasyon Sonuçları")

col1, col2 = st.columns(2)

with col1:
    st.metric("💸 USD/TRY Kuru", f"{usd_try:.2f}")
    st.metric("🔥 Enflasyon (%)", f"{enflasyon:.1f}")

with col2:
    st.metric("📈 Büyüme (%)", f"{buyume:.1f}")
    st.metric("👷 İşsizlik (%)", f"{issizlik:.1f}")
