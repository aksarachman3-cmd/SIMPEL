import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIMPEL", page_icon="🧭", layout="centered")

# ---------- HEADER ----------
st.title("🧭 SIMPEL – Cek Bantuan Sosial yang Mungkin Anda Dapat")
st.markdown("Jawab 7 pertanyaan singkat di bawah ini. **Data Anda tidak disimpan.**")

# ---------- QUESTIONNAIRE ----------
pendapatan = st.selectbox(
    "1. Rata‑rata pendapatan keluarga per bulan?",
    ["< Rp500.000", "Rp500.000 – Rp1.000.000", "Rp1.000.000 – Rp2.000.000", "> Rp2.000.000"]
)

jumlah_anggota = st.selectbox(
    "2. Jumlah anggota keluarga (termasuk Anda)?",
    ["1", "2", "3", "4", "5 atau lebih"]
)

anak_sekolah = st.radio(
    "3. Apakah ada anak usia sekolah (7–18 tahun) di keluarga?",
    ["Ya", "Tidak"]
)

anak_balita = st.radio(
    "4. Apakah ada anak balita (0–6 tahun) atau ibu hamil?",
    ["Ya", "Tidak"]
)

lansia = st.radio(
    "5. Apakah ada anggota keluarga lanjut usia (≥60 tahun)?",
    ["Ya", "Tidak"]
)

disabilitas = st.radio(
    "6. Apakah ada anggota keluarga dengan disabilitas berat?",
    ["Ya", "Tidak"]
)

dinding_rumah = st.selectbox(
    "7. Jenis dinding terluas rumah Anda?",
    ["Tembok", "Semi permanen (setengah tembok)", "Papan/kayu", "Bambu/lainnya"]
)

# ---------- BUTTON (currently just shows answers) ----------
if st.button("🔍 Cek Bantuan yang Mungkin Saya Dapat", type="primary"):
    st.markdown("---")
    st.subheader("📋 Jawaban Anda (untuk pengecekan)")
    st.write(f"**Pendapatan:** {pendapatan}")
    st.write(f"**Jumlah anggota:** {jumlah_anggota}")
    st.write(f"**Anak sekolah:** {anak_sekolah}")
    st.write(f"**Anak balita / ibu hamil:** {anak_balita}")
    st.write(f"**Lansia:** {lansia}")
    st.write(f"**Disabilitas:** {disabilitas}")
    st.write(f"**Dinding rumah:** {dinding_rumah}")
    st.info("🔜 Di tahap berikutnya, jawaban ini akan diproses oleh model AI untuk mengecek kemungkinan bantuan.")